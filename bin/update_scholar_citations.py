#!/usr/bin/env python

import os
import signal
import sys
import time
import yaml
from datetime import datetime
from scholarly import scholarly, ProxyGenerator

# Ensure print output appears immediately in CI (non-TTY) environments
sys.stdout.reconfigure(line_buffering=True)

# Per-attempt timeout (seconds). scholarly.set_timeout doesn't reliably prevent hangs.
ATTEMPT_TIMEOUT = 60


class AttemptTimeout(Exception):
    pass


def _attempt_timeout_handler(signum, frame):
    raise AttemptTimeout()


def load_scholar_user_id() -> str:
    """Load the Google Scholar user ID from the configuration file."""
    config_file = "_data/socials.yml"
    if not os.path.exists(config_file):
        print(f"Configuration file {config_file} not found.")
        sys.exit(1)
    try:
        with open(config_file, "r") as f:
            config = yaml.safe_load(f)
        scholar_user_id = config.get("scholar_userid")
        if not scholar_user_id:
            print("No 'scholar_userid' found in _data/socials.yml.")
            sys.exit(1)
        return scholar_user_id
    except yaml.YAMLError as e:
        print(f"Error parsing YAML file {config_file}: {e}")
        sys.exit(1)


SCHOLAR_USER_ID: str = load_scholar_user_id()
OUTPUT_FILE: str = "_data/citations.yml"
MAX_ATTEMPTS = 3


def load_existing_data() -> dict | None:
    """Load existing citation data if available."""
    if not os.path.exists(OUTPUT_FILE):
        return None
    try:
        with open(OUTPUT_FILE, "r") as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(f"Warning: Could not read {OUTPUT_FILE}: {e}")
        return None


def fetch_author_data(attempt: int) -> dict | None:
    """Fetch author data from Google Scholar, using proxy on retry.

    Each attempt is guarded by SIGALRM so a hanging connection
    cannot block the entire script.
    """
    if attempt == 0:
        print("Attempt 1: direct connection...")
    else:
        print(f"Attempt {attempt + 1}: using free proxy...")
        try:
            pg = ProxyGenerator()
            pg.FreeProxies()
            scholarly.use_proxy(pg)
        except Exception as e:
            print(f"  Proxy setup failed: {e}")
            return None

    scholarly.set_timeout(30)
    scholarly.set_retries(2)

    # Set per-attempt alarm so a hung connection doesn't eat the whole budget
    if hasattr(signal, "SIGALRM"):
        signal.signal(signal.SIGALRM, _attempt_timeout_handler)
        signal.alarm(ATTEMPT_TIMEOUT)

    try:
        author = scholarly.search_author_id(SCHOLAR_USER_ID)
        author_data = scholarly.fill(author, sections=["publications"])
        if hasattr(signal, "SIGALRM"):
            signal.alarm(0)  # cancel alarm on success
        if author_data and "publications" in author_data:
            return author_data
        print("  No publications found in author data.")
        return None
    except AttemptTimeout:
        print(f"  Timed out after {ATTEMPT_TIMEOUT}s.")
        return None
    except Exception as e:
        if hasattr(signal, "SIGALRM"):
            signal.alarm(0)
        print(f"  Failed: {e}")
        return None


def extract_citations(author_data: dict) -> dict:
    """Extract citation data from author data."""
    papers = {}
    for pub in author_data["publications"]:
        pub_id = pub.get("author_pub_id") or pub.get("pub_id")
        if not pub_id:
            continue
        title = pub.get("bib", {}).get("title", "Unknown Title")
        year = pub.get("bib", {}).get("pub_year", "Unknown Year")
        citations = pub.get("num_citations", 0)
        papers[pub_id] = {"title": title, "year": year, "citations": citations}
        print(f"  {title} ({year}) - Citations: {citations}")
    return papers


def get_scholar_citations() -> None:
    """Fetch and update Google Scholar citation data."""
    print(f"Scholar ID: {SCHOLAR_USER_ID}")
    today = datetime.now().strftime("%Y-%m-%d")
    existing_data = load_existing_data()

    # Skip if already updated today
    if (
        existing_data
        and existing_data.get("metadata", {}).get("last_updated") == today
    ):
        print(f"Already updated today ({today}). Skipping.")
        return

    # Try fetching with retries
    author_data = None
    for attempt in range(MAX_ATTEMPTS):
        author_data = fetch_author_data(attempt)
        if author_data:
            break
        if attempt < MAX_ATTEMPTS - 1:
            wait = 5 * (attempt + 1)
            print(f"  Waiting {wait}s before retry...")
            time.sleep(wait)

    if not author_data:
        if existing_data:
            print(
                f"All {MAX_ATTEMPTS} attempts failed. Keeping existing data from {existing_data.get('metadata', {}).get('last_updated', 'unknown')}."
            )
            return
        else:
            print(f"All {MAX_ATTEMPTS} attempts failed and no existing data.")
            sys.exit(1)

    # Extract and compare
    print("Extracting citation data...")
    papers = extract_citations(author_data)

    if existing_data and existing_data.get("papers") == papers:
        print("No changes in citation data.")
        return

    # Write updated data
    citation_data = {"metadata": {"last_updated": today}, "papers": papers}
    try:
        with open(OUTPUT_FILE, "w") as f:
            yaml.dump(citation_data, f, width=1000, sort_keys=True)
        print(f"Citation data saved to {OUTPUT_FILE}")
    except Exception as e:
        print(f"Error writing to {OUTPUT_FILE}: {e}")
        sys.exit(1)


if __name__ == "__main__":
    try:
        get_scholar_citations()
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)
