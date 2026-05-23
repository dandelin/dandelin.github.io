#!/usr/bin/env python
"""Update Google Scholar citation counts in _data/citations.yml.

Strategy:
1. Try scholarly (Google Scholar direct) once with a short timeout.
   Google Scholar IP-blocks Azure / GitHub Actions ranges so this often fails.
2. Always run an OpenAlex per-paper fallback (no IP block, no auth).
3. Merge: scholarly > max(existing, openalex). Never decrease a value —
   protects against the case where scholar fails and OpenAlex returns a
   smaller number than the last successful scholar fetch.

Bibliography metadata is read from _bibliography/papers.bib so missing
entries get added automatically when a new paper lands with a
`google_scholar_id` field.
"""

import json
import os
import re
import signal
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime

import yaml

# Ensure print output appears immediately in CI (non-TTY) environments
sys.stdout.reconfigure(line_buffering=True)

OUTPUT_FILE = "_data/citations.yml"
BIB_FILE = "_bibliography/papers.bib"
SOCIALS_FILE = "_data/socials.yml"

SCHOLARLY_TIMEOUT = 30
OPENALEX_TIMEOUT = 15
OPENALEX_POLITE_DELAY = 0.3  # seconds between OpenAlex calls


def load_scholar_user_id() -> str:
    if not os.path.exists(SOCIALS_FILE):
        print(f"Configuration file {SOCIALS_FILE} not found.")
        sys.exit(1)
    with open(SOCIALS_FILE) as f:
        config = yaml.safe_load(f) or {}
    user_id = config.get("scholar_userid")
    if not user_id:
        print(f"No 'scholar_userid' in {SOCIALS_FILE}.")
        sys.exit(1)
    return user_id


def load_polite_mailto() -> str:
    """OpenAlex 'polite pool' mailto. Falls back to a noreply if email is unset."""
    try:
        with open(SOCIALS_FILE) as f:
            cfg = yaml.safe_load(f) or {}
        email = (cfg.get("email") or "").strip()
        if email and "@" in email:
            return email
    except Exception:
        pass
    return "dandelin@users.noreply.github.com"


def load_existing() -> dict:
    if not os.path.exists(OUTPUT_FILE):
        return {}
    try:
        with open(OUTPUT_FILE) as f:
            return yaml.safe_load(f) or {}
    except Exception as e:
        print(f"Warning: couldn't read {OUTPUT_FILE}: {e}")
        return {}


# ---------------------------------------------------------------------------
# Bibliography parsing
# ---------------------------------------------------------------------------

_ENTRY_RE = re.compile(r"@\w+\{([^,]+),(.*?)(?=\n@\w+\{|\Z)", re.DOTALL)


def _field(body: str, name: str) -> str | None:
    """Extract a {braced} field value from a single bib entry body."""
    pat = re.compile(
        rf"\b{re.escape(name)}\s*=\s*\{{([^{{}}]*(?:\{{[^{{}}]*\}}[^{{}}]*)*)\}}",
        re.IGNORECASE,
    )
    m = pat.search(body)
    return m.group(1).strip() if m else None


def parse_bib(path: str) -> list[dict]:
    """Return list of {cite_key, scholar_id, title, year} for entries with google_scholar_id."""
    if not os.path.exists(path):
        return []
    with open(path) as f:
        content = f.read()
    entries: list[dict] = []
    for m in _ENTRY_RE.finditer(content):
        cite_key = m.group(1).strip()
        body = m.group(2)
        scholar_id = _field(body, "google_scholar_id")
        if not scholar_id:
            continue
        entries.append(
            {
                "cite_key": cite_key,
                "scholar_id": scholar_id,
                "title": _field(body, "title") or "",
                "year": _field(body, "year") or "",
            }
        )
    return entries


# ---------------------------------------------------------------------------
# Stage 1: scholarly (Google Scholar direct)
# ---------------------------------------------------------------------------


class AttemptTimeout(Exception):
    pass


def _alarm_handler(signum, frame):
    raise AttemptTimeout()


def try_scholarly(user_id: str, timeout: int = SCHOLARLY_TIMEOUT) -> dict | None:
    """Single attempt at Google Scholar via scholarly.

    Returns {pub_id: {title, year, citations}} on success, None on failure.
    Hard-bounded by SIGALRM so a hanging connection can't eat the workflow budget.
    """
    try:
        from scholarly import scholarly
    except ImportError as e:
        print(f"  scholarly not installed: {e}")
        return None

    scholarly.set_timeout(timeout)
    scholarly.set_retries(1)

    if hasattr(signal, "SIGALRM"):
        signal.signal(signal.SIGALRM, _alarm_handler)
        signal.alarm(timeout)

    try:
        author = scholarly.search_author_id(user_id)
        author = scholarly.fill(author, sections=["publications"])
        if hasattr(signal, "SIGALRM"):
            signal.alarm(0)
        if not author or "publications" not in author:
            print("  scholarly: no publications field")
            return None
        out: dict[str, dict] = {}
        for pub in author["publications"]:
            pid = pub.get("author_pub_id") or pub.get("pub_id")
            if not pid:
                continue
            bib = pub.get("bib", {}) or {}
            out[pid] = {
                "title": bib.get("title", "Unknown Title"),
                "year": bib.get("pub_year", "Unknown Year"),
                "citations": int(pub.get("num_citations", 0) or 0),
            }
        return out
    except AttemptTimeout:
        print(f"  scholarly: timed out after {timeout}s")
        return None
    except Exception as e:
        if hasattr(signal, "SIGALRM"):
            signal.alarm(0)
        print(f"  scholarly: failed ({e.__class__.__name__}: {e})")
        return None


# ---------------------------------------------------------------------------
# Stage 2: OpenAlex per-paper fallback
# ---------------------------------------------------------------------------


def _normalize_title(s: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]", " ", (s or "").lower())).strip()


def _title_similarity(a: str, b: str) -> float:
    """Jaccard similarity over normalized word tokens. 0.0 if either side empty."""
    ta = {tok for tok in _normalize_title(a).split() if len(tok) > 2}
    tb = {tok for tok in _normalize_title(b).split() if len(tok) > 2}
    if not ta or not tb:
        return 0.0
    return len(ta & tb) / len(ta | tb)


# Refuse to return a "best guess" — OpenAlex search relevance happily ranks
# unrelated review papers above the real paper when the query has generic words.
# False positives inflate citation counts, which is worse than a missing entry.
TITLE_SIMILARITY_THRESHOLD = 0.5


def _pick_match(target_title: str, target_year: str, works: list[dict]) -> dict | None:
    """Return the OpenAlex result confidently identified as the same paper, else None.

    Requires both:
      - Jaccard token overlap ≥ TITLE_SIMILARITY_THRESHOLD against target title.
      - publication_year within ±1 of target year (if target year is known).
    """
    if not works:
        return None
    target_year_int: int | None = None
    if target_year and re.fullmatch(r"\d{4}", str(target_year).strip()):
        target_year_int = int(target_year.strip())

    target_norm = _normalize_title(target_title)
    best_score = 0.0
    best: dict | None = None
    for w in works:
        if target_year_int is not None:
            wy = w.get("publication_year")
            if wy and abs(int(wy) - target_year_int) > 1:
                continue
        cand_title = w.get("title", "")
        cand_norm = _normalize_title(cand_title)
        # Strong prefix/substring match (catches cases like target
        # "ChartSense: Interactive data extraction from chart images" vs
        # OpenAlex stored title "ChartSense" — short but unambiguous).
        if len(cand_norm) >= 6 and (
            cand_norm in target_norm or target_norm in cand_norm
        ):
            return w
        score = _title_similarity(target_title, cand_title)
        if score > best_score:
            best_score = score
            best = w
    if best_score >= TITLE_SIMILARITY_THRESHOLD:
        return best
    return None


def fetch_openalex(title: str, year: str, mailto: str) -> int | None:
    """Return cited_by_count for one paper, or None if not findable."""
    if not title:
        return None
    params: dict[str, str] = {
        "search": title,
        "per-page": "5",
        "mailto": mailto,
    }
    if year and re.fullmatch(r"\d{4}", str(year).strip()):
        params["filter"] = f"publication_year:{year.strip()}"
    url = "https://api.openalex.org/works?" + urllib.parse.urlencode(params)
    try:
        req = urllib.request.Request(
            url, headers={"User-Agent": f"dandelin-citation-updater (mailto:{mailto})"}
        )
        with urllib.request.urlopen(req, timeout=OPENALEX_TIMEOUT) as resp:
            data = json.load(resp)
    except urllib.error.HTTPError as e:
        print(f"    OpenAlex HTTP {e.code}: {title[:50]}")
        return None
    except Exception as e:
        print(f"    OpenAlex error ({e.__class__.__name__}): {title[:50]}")
        return None
    works = data.get("results", []) or []
    match = _pick_match(title, year, works)
    if not match:
        return None
    return int(match.get("cited_by_count", 0) or 0)


def stage_openalex(bib_entries: list[dict], mailto: str) -> dict[str, int]:
    """Returns {scholar_id: cited_by_count} for each successfully resolved paper."""
    out: dict[str, int] = {}
    for entry in bib_entries:
        cited = fetch_openalex(entry["title"], entry["year"], mailto)
        if cited is None:
            print(f"  ✗ {entry['title'][:60]} ({entry['year']}) — no match")
        else:
            out[entry["scholar_id"]] = cited
            print(f"  ✓ {entry['title'][:60]} ({entry['year']}) → {cited}")
        time.sleep(OPENALEX_POLITE_DELAY)
    return out


# ---------------------------------------------------------------------------
# Merge + write
# ---------------------------------------------------------------------------


def merge(
    user_id: str,
    existing_papers: dict[str, dict],
    scholarly_data: dict[str, dict] | None,
    openalex_data: dict[str, int],
    bib_entries: list[dict],
) -> dict[str, dict]:
    """Merge sources with safety: never decrease an existing citation count."""
    merged: dict[str, dict] = {k: dict(v) for k, v in (existing_papers or {}).items()}

    # 1. Scholarly is authoritative when present. Overwrite directly (scholarly
    #    handles "paper merged on Scholar" edge cases that we'd otherwise miss).
    if scholarly_data:
        for k, v in scholarly_data.items():
            merged[k] = dict(v)

    # 2. OpenAlex supplements: fill missing entries; for existing entries,
    #    take max(current, openalex) so a fallback never reduces a known count.
    bib_by_sid = {e["scholar_id"]: e for e in bib_entries}
    for scholar_id, openalex_cited in openalex_data.items():
        full_key = f"{user_id}:{scholar_id}"
        bib = bib_by_sid.get(scholar_id, {})
        if full_key in merged:
            cur = merged[full_key]
            cur_cited = int(cur.get("citations", 0) or 0)
            merged[full_key] = {
                "title": cur.get("title") or bib.get("title", "Unknown"),
                "year": cur.get("year") or bib.get("year", "Unknown"),
                "citations": max(cur_cited, int(openalex_cited)),
            }
        else:
            merged[full_key] = {
                "title": bib.get("title", "Unknown"),
                "year": bib.get("year", "Unknown"),
                "citations": int(openalex_cited),
            }
    return merged


def write_yaml(papers: dict[str, dict], today: str) -> None:
    out = {"metadata": {"last_updated": today}, "papers": papers}
    with open(OUTPUT_FILE, "w") as f:
        yaml.dump(out, f, width=1000, sort_keys=True)


def report_diff(existing: dict[str, dict], merged: dict[str, dict]) -> None:
    added = sorted(set(merged) - set(existing))
    removed = sorted(set(existing) - set(merged))
    changed = [
        k for k in sorted(set(existing) & set(merged))
        if existing[k] != merged[k]
    ]
    print(f"\n✓ {len(merged)} entries total. +{len(added)} added, ~{len(changed)} changed, -{len(removed)} removed.")
    for k in added[:5]:
        c = merged[k].get("citations", "?")
        print(f"  + {k} (cited={c}) {merged[k].get('title','')[:50]}")
    for k in changed[:10]:
        old = existing[k].get("citations", "?")
        new = merged[k].get("citations", "?")
        if old != new:
            print(f"  ~ {k}: {old} → {new}  {merged[k].get('title','')[:50]}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> None:
    user_id = load_scholar_user_id()
    today = datetime.now().strftime("%Y-%m-%d")
    mailto = load_polite_mailto()

    existing = load_existing()
    existing_papers = existing.get("papers", {}) or {}

    print(f"Scholar ID: {user_id}")
    print(f"OpenAlex mailto: {mailto}")
    print(f"Existing entries: {len(existing_papers)}")
    print(f"Today: {today}")

    bib_entries = parse_bib(BIB_FILE)
    print(f"Bibliography entries with google_scholar_id: {len(bib_entries)}")

    # ── Stage 1: scholarly direct
    print("\n=== Stage 1: scholarly (Google Scholar direct) ===")
    scholarly_data = try_scholarly(user_id)
    if scholarly_data:
        print(f"  scholarly returned {len(scholarly_data)} papers.")
    else:
        print("  scholarly unavailable — falling back to OpenAlex.")

    # ── Stage 2: OpenAlex per-paper (always run; cheap and supplements scholarly)
    print("\n=== Stage 2: OpenAlex per-paper ===")
    openalex_data = stage_openalex(bib_entries, mailto)
    print(f"  OpenAlex resolved {len(openalex_data)}/{len(bib_entries)} papers.")

    # If neither source returned anything AND we have existing data, keep it.
    if not scholarly_data and not openalex_data:
        if existing_papers:
            print("\nBoth sources failed. Keeping existing data.")
            return
        print("\nBoth sources failed and no existing data — exiting with error.")
        sys.exit(1)

    # ── Stage 3: merge + write
    print("\n=== Stage 3: merge ===")
    merged = merge(user_id, existing_papers, scholarly_data, openalex_data, bib_entries)

    # Bump last_updated even if papers dict is identical IF either source
    # actually returned data — this lets us see "yes, the workflow ran cleanly".
    # But we only commit if the YAML content changes (the workflow's git diff
    # gate handles that), so updating last_updated when content is otherwise
    # unchanged would create a spurious commit.  Preserve the existing
    # last_updated when papers are unchanged.
    if existing_papers == merged:
        print("No change in citation data.")
        return

    write_yaml(merged, today)
    report_diff(existing_papers, merged)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Unexpected error: {e.__class__.__name__}: {e}")
        sys.exit(1)
