# roger2148.github.io

Heng Zhang's personal site, served by GitHub Pages from `master`.

- Pages: `index.html` (About me), `research.html`, `developer.html`, `music.html`, plus `topic-*.html` for the five research topics.
- Shared style and script: `assets/site.css`, `assets/site.js`; inline translation (zh-Hans / zh-Hant / ja) by `assets/lang.js` with dictionaries in `assets/i18n/`. The nav is duplicated in every page.
- Favicon and social card: `assets/brand/` (regenerate with `make_brand.py`).
- Raw photos and videos go in `assets/temp/` (git-ignored); web-sized copies live under `assets/`.

**Updating the site:** see [`skills/update-website.md`](skills/update-website.md). It lists, for every
kind of change (new paper, paper accepted, talk or poster, activity photos, topic page, developer project,
Bilibili cover, favourite artist, funding, CV lines), where it goes, what information to supply, the exact
markup, and the media conversion commands.

Preview locally: `python3 -m http.server 8070 --bind 127.0.0.1` then open http://127.0.0.1:8070/.
