# CLAUDE.md — dandelin.github.io

## Project Overview

개인 학술 웹사이트 (wonjae.kim). [al-folio](https://github.com/alshedivat/al-folio) v0.16.3 기반.

- **소스 브랜치:** `main` (upstream deploy.yml 트리거와 일치)
- **배포:** GitHub Actions → `gh-pages` 브랜치 → GitHub Pages
- **도메인:** `wonjae.kim` (CNAME 파일로 설정)
- **upstream remote:** `upstream` → `alshedivat/al-folio`
- **백업:** `source-archive` 브랜치에 마이그레이션 이전 원본 보존

## Architecture & Key Decisions

### upstream 추적 가능한 구조

- upstream al-folio 파일 수정 최소화 → `git merge upstream/main` 시 충돌 최소화
- 개인화는 `_config.yml` 값 변경, `_data/*.yml`, `_pages/about.md` 본문, `_bibliography/papers.bib`에만 집중
- 예상 충돌 파일: `_config.yml`, `_data/socials.yml` (단순 값 충돌)
- **이미 수정된 upstream 파일:** `_layouts/bib.liquid` (인용배지 인라인, venue fallback), `_sass/_themes.scss` (다크모드 테이블 FOUC), `_includes/head.liquid` (다크모드 초기화)

### 댓글 시스템

- **Giscus** 사용 (Disqus에서 전환)
- repo: `dandelin/dandelin.github.io`, category: `General`
- 포스트 front matter에 `giscus_comments: true` 사용 (구 `comments: true` 아님)

### 한국어 이름 표시

- `_pages/about.md`의 `subtitle` 필드: `김<b>원재</b> · ML/HCI Research Scientist`
- upstream 파일 수정 없이 subtitle 방식으로 구현

## Directory Structure

```
_bibliography/papers.bib    # 논문 BibTeX (abbr, pdf, html, abstract, selected 필드)
_data/socials.yml           # 소셜 링크 (email, github, twitter, linkedin, scholar, cv)
_data/venues.yml            # 학회 약어→색상 매핑 (NeurIPS, ICML, ECCV 등 20개)
_news/announcement_*.md     # 뉴스 항목 (25개, inline layout)
_posts/*.md                 # 블로그 포스트 (9개, 한국어 다수)
_pages/about.md             # 메인 페이지 (프로필, 뉴스, selected papers, latest posts)
_pages/publications.md      # 논문 목록 (group_by: year 자동 그룹핑)
_pages/cv.md                # CV (PDF 임베드, /cv/ 경로)
_pages/blog.md              # 블로그 목록
_pages/news.md              # 뉴스 전체 목록
assets/pdf/papers/          # 논문 PDF 27개
assets/pdf/cv.pdf           # CV
assets/img/prof_pic5.jpg    # 현재 사용 중인 프로필 사진
assets/img/favicon.ico      # 파비콘
CNAME                       # 커스텀 도메인
```

## \_config.yml Key Settings

```yaml
first_name: Wonjae
middle_name: (Dan)
last_name: Kim
url: https://wonjae.kim
baseurl: # 빈값 (루트 서빙)
max_width: 800px
future: true # GitHub Actions UTC 빌드 → KST 당일 포스트 누락 방지
search_enabled: false # Cmd+K 검색 비활성화
bib_search: false # publications 필터 텍스트박스 비활성화
max_author_limit: # 비움 → 전체 저자 표시
google_analytics: UA-47120899-4
imagemagick.enabled: false # 로컬 빌드 편의 (CI에서는 imagemagick 설치됨)
scholar.last_name: [Kim]
scholar.first_name: [Wonjae]
scholar.group_by: year
```

## Common Tasks

### 새 클론 후 초기 설정

```bash
bundle install
git config core.hooksPath .githooks   # prettier pre-commit 훅 활성화
```

### upstream 업데이트

```bash
git fetch upstream --tags
git checkout main
git merge upstream/main   # 충돌 시 _config.yml, _data/*.yml 값만 조정
git push origin main
```

### 새 논문 추가

1. `_bibliography/papers.bib`에 BibTeX 추가 (abbr, pdf, html, abstract, selected 필드)
2. PDF를 `assets/pdf/papers/`에 추가
3. `_data/venues.yml`에 새 학회 약어가 있으면 추가

### 새 블로그 포스트 추가

- `_posts/YYYY-MM-DD-title.md` 생성
- front matter: `layout: post`, `title`, `date`, `description`, `giscus_comments: true`
- 비공개: `published: false` 추가

### 새 뉴스 추가

- `_news/announcement_N.md` (다음 번호)
- front matter: `layout: post`, `date`, `inline: true`

## Build & Deploy

- push to `main` → `.github/workflows/deploy.yml` 자동 실행
- Ruby 3.3.5, Jekyll, imagemagick, purgecss 사용
- 결과물 `_site/` → `gh-pages` 브랜치에 배포
- deploy.yml은 `paths` 필터 사용 — `.yml`, `.liquid`, `.md`, `assets/**` 등 변경 시만 트리거
- deploy 워크플로우 확인: `gh api 'repos/dandelin/dandelin.github.io/actions/workflows/222827438/runs?per_page=3'`
- prettier CI도 push마다 실행 — `npx prettier . --write`로 포맷 유지 (package.json에 @shopify/prettier-plugin-liquid 포함)

### 로컬 빌드 (선택)

```bash
bundle install
bundle exec jekyll serve
```

## Customizations (upstream 대비)

- **인용배지 인라인:** `_layouts/bib.liquid` — Google Scholar 배지를 badges div에서 제목 옆 인라인으로 이동
- **venue fallback:** `_layouts/bib.liquid` — `@misc` 타입에 `booktitle`/`journal` fallback 추가
- **인용수 lookup 수정:** `_layouts/bib.liquid` — `site.scholar_userid` → `site.data.socials.scholar_userid`
- **다크모드 테이블 FOUC 수정:** `_sass/_themes.scss` — `html[data-theme="dark"] .table { color: var(--global-text-color) }`
- **다크모드 초기화:** `_includes/head.liquid` — inline script로 `data-theme` 즉시 설정
- **CV 임베드:** `_pages/cv.md` — redirect 제거, PDF `<embed>` 사용

## Notes

- `_posts` 파일명에 공백이 있는 파일 2개 존재 (copy 접미사) — 둘 다 `published: false`
- 블로그 포스트 대부분 한국어 또는 한영 혼합
- `_data/coauthors.yml`은 제거됨 (사용하지 않음)
- collections에서 `books`, `projects`, `teachings` 제거됨 — 해당 페이지/디렉토리 없음
- `source-archive` 브랜치: 마이그레이션 이전 원본 백업 — 당분간 유지
- `future: true` 설정: GitHub Actions가 UTC로 빌드하므로 KST 당일 포스트 누락 방지용
