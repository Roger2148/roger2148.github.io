# Skill: Update Heng Zhang's personal website

How to make incremental changes to https://roger2148.github.io (repo `roger2148.github.io`,
branch `master`, deployed by GitHub Pages on push).

When Heng says "I have a new X, update the web", find X in the **Playbooks** below,
ask only for the fields marked **ask** that were not already given, make the edit,
check it locally, then commit and push when asked.

---

## 1. Site map

Four pages plus five research-topic pages. All share `assets/site.css`, `assets/site.js`
and one header (the nav). Every page ends with the same `#contact` block.

| page | nav label | sections (in order) |
|---|---|---|
| `index.html` | About me | hero (photo, name, links, three "doors"), `#about`, `#experience`, `#education`, `#more`, `#contact` |
| `research.html` | As a Researcher | `#activities`, `#research` (5 topic cards), `#publications`, `#presentations`, `#funding`, `#contact` |
| `developer.html` | As a Developer | `#projects` (one `article.dev-project` per project), `#contact` |
| `music.html` | As a Music Lover | `#music` (featured Bilibili player), `#covers` (playlist), `#artists`, `#contact` |
| `topic-sode.html`, `topic-vision.html`, `topic-xenovert.html`, `topic-reservoir.html`, `topic-temporal.html` | (under As a Researcher) | `#topic` (paragraph + media), `#related` (links to works), `#contact` |

**The nav is duplicated in all 9 HTML files.** Any change to a menu (new item, renamed
item, reordered items, changed count in a hint) must be applied to every file. Use a
script with `replace`/regex over `index.html research.html developer.html music.html topic-*.html`;
never edit one file by hand and forget the others.

Menu markup, desktop (inside `<div class="nav">`):
```html
<div class="nav__group"><a class="nav__item" href="PAGE.html" aria-haspopup="true">LABEL<svg …chevron…></svg></a>
  <div class="nav-menu"><ul>
    <li><a href="PAGE.html#SECTION"><span class="nav-menu__num">01</span><span><span class="nav-menu__label">Item</span><span class="nav-menu__sub">one-line hint</span></span></a></li>
  </ul></div></div>
```
Phone menu (inside `<div class="nav-mobile">`):
```html
<div class="nav-mobile__group"><a class="nav-mobile__title" href="PAGE.html">LABEL</a><a href="PAGE.html#SECTION" onclick="toggleMenu()">Item</a>…</div>
```

Assets:

| folder | holds | rule |
|---|---|---|
| `assets/activities/` | photos and posters for Activities cards | JPEG, long side ≤ 1600 px, EXIF orientation baked in |
| `assets/video/` | research demo videos + poster frames (`name.mp4` + `name.jpg`) | H.264 1080p, CRF 26, `+faststart`; drop silent audio |
| `assets/dev/` | developer page media (screenshots, demo clips, YouTube thumbnail) | same rules |
| `assets/music/` | Bilibili covers `BVxxxx.jpg` (640×400), `avatar.jpg`, `artists/*.jpg` (240×240) | downloaded once, served locally |
| `assets/temp/` | **originals, git-ignored** | never commit; put raw files here |
| `slide/` | research topic card images | |

Local preview: `cd ~/Documents/GitHub/roger2148.github.io && python3 -m http.server 8070 --bind 127.0.0.1`
then open http://127.0.0.1:8070/. Open pages over HTTP, not as `file://` (YouTube embeds refuse `file://`, error 153).

Deploy: `git add -A && git commit -m "…" && git push origin master`. Pages is live about a minute later.
Check with `curl -s https://roger2148.github.io/research.html | grep -c "<some new string>"`.

---

## 2. Media recipes (run from the repo root)

**Photo → web JPEG with orientation fixed** (Pillow lives in conda env `bcpnn_local`):
```bash
sips -s format jpeg -s formatOptions 82 -Z 1600 "assets/temp/IN.jpg" --out assets/activities/OUT.jpg
conda run -n bcpnn_local python -c "
from PIL import Image, ImageOps; f='assets/activities/OUT.jpg'
im=ImageOps.exif_transpose(Image.open(f)).convert('RGB'); im.save(f, quality=82, optimize=True); print(im.size)"
```
Record the printed `(width, height)`: the Activities card needs it as `--ar: W / H`.
HEIC and Sony ARW inputs work with the same `sips` command. Phone photos often carry
EXIF orientation 6; without the Pillow step they come out sideways.

**Video → web MP4** (silent source: add `-an`; keep audio: `-c:a aac -b:a 96k`):
```bash
ffmpeg -y -i "assets/temp/IN.mp4" -vf "scale=-2:1080" -c:v libx264 -preset slow -crf 26 -pix_fmt yuv420p -an -movflags +faststart assets/video/OUT.mp4
ffmpeg -y -ss 2 -i assets/video/OUT.mp4 -frames:v 1 -q:v 4 assets/video/OUT.jpg   # poster frame
```
Check whether audio is real before keeping it: `ffmpeg -i IN.mp4 -vn -af volumedetect -f null - 2>&1 | grep mean_volume` (about −91 dB means silent).
Typical result: a 100 MB screen recording becomes 2 to 11 MB.

**Bilibili video list** (public API, no login; the space page itself needs login):
```bash
UA="Mozilla/5.0"; curl -s -c cj.txt -A "$UA" https://www.bilibili.com/ -o /dev/null
curl -s -b cj.txt -A "$UA" "https://api.bilibili.com/x/polymer/web-space/seasons_archives_list?mid=26533739&season_id=8435205&page_num=1&page_size=30"
```
(`mid` 26533739 = Pikaaaaaaachu; `season_id` 8435205 = 合集·Fujii Kaze; list all collections with
`…/seasons_series_list?mid=26533739&page_num=1&page_size=20`.) Each archive gives `bvid`, `title`,
`pubdate`, `duration`, `stat.view`, `pic`. Cover: `curl -A "$UA" -H "Referer: https://www.bilibili.com/" "<pic>@640w_400h_1c.jpg" -o assets/music/<bvid>.jpg`.
Embed URL used by the player: `https://player.bilibili.com/player.html?bvid=<bvid>&page=1&high_quality=1&danmaku=0&autoplay=1`.

**YouTube channel avatar + subscriber count** (for the artists row):
```bash
curl -s -A "Mozilla/5.0" -b "CONSENT=YES+cb; SOCS=CAI" https://www.youtube.com/@HANDLE -o page.html
grep -o 'property="og:image" content="[^"]*"' page.html | head -1      # avatar URL; change =s900 to =s240
grep -o '"[0-9.,]*[KM]* subscribers"' page.html | head -1
```

**YouTube video → click-to-load embed**: only the video id is needed; thumbnail is `https://i.ytimg.com/vi/<id>/maxresdefault.jpg`.

**Screenshot of a live page** (for a site-preview card): headless Chrome,
`"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --window-size=1600,900 --force-device-scale-factor=1.5 --virtual-time-budget=12000 --screenshot=out.png URL`, then crop with Pillow.

---

## 3. Playbooks

Each playbook: where, what to **ask**, the template, and side effects (nav, other pages).

### 3.1 New paper (submitted / under review)
**Where**: `research.html` → `#publications` → `div.pub-list`, newest first (top). Group comments like `<!-- 2026 Under Review -->` are only guides.

**Ask**: title · authors (in order) · venue · year · status label (`Soon to Submit`, `Under Review`, `In Submission`) · link (optional) · which research topic it belongs to.

```html
<div class="pub-item" data-show="true" data-category="under-review">
    <p class="pub-type">Under Review</p>
    <p class="pub-title">TITLE</p>
    <p class="pub-authors">A, B, Heng Zhang, C</p>
    <p class="pub-venue">VENUE, YEAR</p>
    <div class="pub-links"><a href="URL" target="_blank">Paper Link</a></div>   <!-- optional -->
</div>
```
`data-category` drives the filter tabs: `under-review` | `journal` | `conference` | `review`. `data-show="false"` hides an item.

**Also**: add a row to the matching `topic-*.html` → `#related` → `div.pres-list` (template in 3.10).
If it is a topic's main paper, mention it in the topic paragraph.

### 3.2 Paper accepted / published
**Where**: the existing `pub-item` in `research.html`.

**Ask**: final venue string (journal, volume/pages or conference name, year, IF if wanted) · DOI/URL · category (journal / conference / review).

Change `data-category`, the `.pub-type` text, `.pub-venue`, and add or replace the `pub-links` anchor.
Then update the same title in every `topic-*.html` related-works row (`.pres-meta` text) and, if present, the Activities card text (any "under review" wording).

### 3.3 New talk or poster
**Where**: `research.html` → `#presentations` → `div.pres-list`, newest first.

**Ask**: title · Talk or Poster · event name · city, country · date · poster number (optional).

```html
<div class="pres-item">
    <span class="pres-badge">Poster</span>          <!-- or Talk -->
    <p class="pres-title">TITLE</p>
    <p class="pres-meta">EVENT (Poster 3P-465), VENUE, CITY, COUNTRY, MONTH D, YYYY</p>
</div>
```
**Also**: usually a photo card (3.4) and a related-works row on the topic page (3.10).

### 3.4 New activity card (photos of a poster, talk, event, launch)
**Where**: `research.html` → `#activities` → `div.activities-grid`, newest first. Cards alternate sides:
first card photos right, second has `activity-card--flip` (photos left), and so on. After inserting at the top,
re-alternate the `--flip` class down the list.

**Ask**: kicker (e.g. `Poster · NEURO2026`) · title · meta line (event · place · date, short) · one casual sentence · 1 to 3 images (poster PDF/PNG and/or photos), and which one should be in front.

Convert each image with the photo recipe (section 2) into `assets/activities/<event>_<n>.jpg` and note W×H.

```html
<div class="activity-card">
    <div class="activity-content">
        <p class="activity-kicker">KICKER</p>
        <h3>TITLE</h3>
        <p class="activity-meta">EVENT · PLACE · DATE</p>
        <p>ONE SENTENCE.</p>
    </div>
    <div class="activity-preview" aria-hidden="true">
        <button class="stack-card stack-card--portrait" style="--ar: 1130 / 1600" type="button" data-full="assets/activities/FILE.jpg" data-caption="CAPTION"><img src="assets/activities/FILE.jpg" alt="CAPTION" loading="lazy"></button>
        <button class="stack-card stack-card--landscape" style="--ar: 1600 / 1066" type="button" data-full="…" data-caption="…"><img src="…" alt="…" loading="lazy"></button>
        <button class="stack-card stack-card--portrait" …></button>
    </div>
</div>
```
Stack slots by order: 1st = back (top-left), 2nd = **front** (right, highest z-index), 3rd = bottom-left.
Put the poster first and the best photo second. Class by orientation: `--portrait` (h > w), `--landscape`, `--square`.
`--ar` is the image's real width / height. Clicking a card opens it in the lightbox, which is already wired.

To flag a card as new: add class `activity-card--new` and `<span class="activity-new">New</span>` as the first child. Remove both from the previous "new" card.

For a flat single image (a website screenshot) use `activity-preview activity-preview--flat` containing an `a.site-preview` (copy the companion-site card).

### 3.5 New research topic page
**Ask**: title · slug · one paragraph · related works (titles already on the site) · media (videos / images / placeholder) · card image for the research grid.

Copy `topic-reservoir.html` (it has the placeholder media), change `<title>`, the `#topic` content, and the `#related` rows.
Media blocks:
```html
<div class="topic-media">                      <!-- add topic-media--single for one item, topic-media--rows to stack -->
    <figure class="topic-media__item"><video controls preload="metadata" playsinline poster="assets/video/X.jpg"><source src="assets/video/X.mp4" type="video/mp4"></video><figcaption>CAPTION</figcaption></figure>
    <div class="topic-media__item media-placeholder"><div><strong>Media placeholder</strong>Text</div></div>
</div>
```
**Also**: a `project-card` in `research.html` → `#research` → `.projects-grid` with `<h3><a class="project-title-link" href="topic-SLUG.html">TITLE</a></h3>`, an image in `slide/`, and one short sentence. The nav needs no change (topic pages are reached from the cards); `site.js` highlights "As a Researcher" for any `topic-*.html`.

### 3.6 New developer project
**Where**: `developer.html` → `#projects` → `div.dev-list`. Order is curated, not chronological; ask where it goes.

**Ask**: name · kicker (`Open source · Local AI app`) · **your role / credit** (cards lead with credit, not with the product) · one or two sentences · links (GitHub, site) · tech tags · media: a YouTube id, a video file, or a screenshot.

```html
<article class="dev-project" id="SLUG">
    <div class="dev-media">
        <!-- YouTube (loads only on click): -->
        <div class="yt-lite" data-yt="VIDEO_ID" data-title="VIDEO TITLE"><img src="assets/dev/SLUG_thumb.jpg" alt="" loading="lazy"><button type="button" class="yt-lite__play" aria-label="Play">…copy the play svg from #olden-flames…</button></div>
        <!-- or local video: -->
        <video controls preload="metadata" playsinline poster="assets/dev/SLUG.jpg"><source src="assets/dev/SLUG.mp4" type="video/mp4"></video>
        <!-- or image: --> <img src="assets/dev/SLUG.png" alt="">
        <p class="dev-media__caption">CAPTION</p>
    </div>
    <div class="dev-content">
        <p class="activity-kicker">KICKER</p>
        <h3>NAME</h3>
        <p class="dev-meta">My role: … · one-line descriptor</p>
        <p>SENTENCES.</p>
        <div class="dev-links"><a href="URL" target="_blank" rel="noopener">GitHub &nearr;</a></div>
        <ul class="dev-tags"><li>Tag</li><li>Tag</li></ul>
    </div>
</article>
```
Add `dev-project--flip` to put media on the right (currently all cards have media on the left).

**Also**: add the project to the "As a Developer" menu in **all 9 files**: a desktop `nav-menu` li with the next `nav-menu__num`, and a phone `nav-mobile__group` link. Keep labels short.

### 3.7 New Bilibili cover
**Where**: `music.html` → `#covers` → `div.music-grid`, newest first.

**Ask**: the video link or BV id (everything else comes from the API) · display song name · optional note (`Ballad ver.`, `Live at …`).

Steps: fetch the archive with the API recipe (section 2) to get `pubdate`, `duration`, `stat.view`, `pic`; download the cover to `assets/music/<bvid>.jpg`; insert:
```html
<button type="button" class="music-tile" data-bvid="BV…" data-name="SONG" data-sub="NOTE OR EMPTY" data-date="Mon YYYY" data-dur="M:SS" data-views="NNN" title="ORIGINAL TITLE">
    <span class="music-tile__cover"><img src="assets/music/BV….jpg" alt="" loading="lazy"><span class="music-tile__dur">M:SS</span></span>
    <span class="music-tile__name">SONG</span>
    <span class="music-tile__meta">NOTE · Mon YYYY</span>            <!-- omit "NOTE · " when empty -->
</button>
```
Update the count in the lede ("17 covers so far") and in the nav hint "All 17 covers on Bilibili" (all 9 files).
To change the default featured video: set `#bili-stage[data-bvid]`, `#bili-cover[src]`, `#bili-title`, `#bili-meta`, `#bili-link[href]`, and move `is-current` to that tile.

### 3.8 New favourite artist
**Where**: `music.html` → `#artists` → `div.artists-grid`.

**Ask**: name · Japanese/native name · YouTube handle or channel URL · three short lines (style, mood, subscriber count).

Fetch the avatar and count with the YouTube recipe (section 2) into `assets/music/artists/<key>.jpg` (240 px), then:
```html
<a class="artist" href="https://www.youtube.com/@HANDLE" target="_blank" rel="noopener">
    <span class="artist__photo"><img src="assets/music/artists/KEY.jpg" alt="NAME" loading="lazy"></span>
    <span class="artist__name">NAME<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 17 17 7M9 7h8v8" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
    <span class="artist__jp">NATIVE NAME</span>
    <span class="artist__tags">Line 1<br>Line 2<br>N.NM on YouTube</span>
</a>
```
Verify the channel is the official one (channel title, plausible subscriber count) before linking; handles that look right can belong to fans.

### 3.9 Funding, experience, education, bio, hero, contact
- **Funding**: `research.html` → `#funding` → `.funding-list`, newest first. **Ask**: full grant name, year range, one-line description, amount, role.
  ```html
  <div class="funding-item" data-expanded="false">
      <div class="funding-collapsed"><p class="funding-short">NAME • YYYY–YYYY</p><p class="funding-read-more"><a href="#" class="read-more" onclick="toggleFunding(event, this)">Read more</a></p></div>
      <div class="funding-full" style="display: none;"><p class="funding-grant">NAME • YYYY–YYYY</p><p class="funding-meta">DESCRIPTION</p><p class="funding-amount">¥AMOUNT • ROLE</p><p class="funding-read-more"><a href="#" class="read-less" onclick="toggleFunding(event, this)">Show less</a></p></div>
  </div>
  ```
- **Experience / Education**: `index.html` → `#experience` / `#education` → `.timeline`, newest first. **Ask**: date range, title or degree, organisation, one or two sentences.
  ```html
  <div class="timeline-item"><span class="timeline-date">Mon YYYY — Present</span><h3 class="timeline-title">TITLE</h3><p class="timeline-org">ORG</p><p class="timeline-desc">TEXT</p></div>
  ```
- **Bio, skills, languages, teaching**: `index.html` → `#about` / `#more`; plain paragraphs and lists.
- **Hero**: `index.html` → `section.hero`: `.hero-title` (position), `.hero-tagline`, `.hero-links` (profile buttons), `.hero-paths` (the three doors; keep exactly three, labels in `.hero-path__label`). The photo is `profile_photo.jpeg`.
- **Contact**: `#contact` is copied into every page; change it in all 9 files.

### 3.10 Related-works row (topic pages)
`topic-*.html` → `#related` → `div.pres-list`, newest first:
```html
<a class="pres-item topic-work" href="research.html#publications">     <!-- or #presentations -->
    <span class="pres-badge">Paper</span>                               <!-- Paper / Talk / Poster -->
    <p class="pres-title">TITLE</p>
    <p class="pres-meta">VENUE, YEAR</p>
</a>
```

---

## 3.11 Translations (zh-Hans, zh-Hant, ja)
The site has inline translation like the paper site: `assets/lang.js` swaps the text of leaf
elements using `assets/i18n/<lang>.json`, keyed by the **English innerHTML** of each element
(whitespace collapsed, `&` as `&amp;`, SVGs as `{svg0}`). English is the source and is never
edited by the script; switching back restores the original nodes. The visitor's browser language
picks the start language; a choice from the globe menu is stored and wins. Names, paper titles,
venues, song titles and tech names deliberately stay English (see `SKIP` in `lang.js`).

**Every time English text changes or is added, its key changes**, so the dictionaries need an entry:

1. Serve the site, open the page, and in the console run `window.__I18N.collect()` (in English) to see the exact keys; or run the headless collector below for all pages at once.
2. Add `E("<exact English key>", "<zh-Hans>", "<ja>")` in `assets/i18n/build_i18n.py` (section by page). Keep the same inline tags (`<br>`, `<a …>`, `<strong>`) in the values.
3. Rebuild: `conda run -n bcpnn_local python assets/i18n/build_i18n.py` → writes `zh-Hans.json`, `zh-Hant.json` (OpenCC + `OVERRIDE_HANT`), `ja.json`.
4. Check: with the page in English, `collect().strings.filter(s => !dict[s])` against each JSON should list only strings meant to stay English.

Dynamic strings assembled by `site.js` (music "views", month labels, playlist notes) go through `window.__I18N.t()`; the dictionary has every `Mon YYYY` for 2025–2027 and each playlist note, so new covers only need a note entry if the note is new.

Key collector for all nine pages: serve the site and open `http://127.0.0.1:8070/assets/i18n/collect.html`.
It lists every key not yet in `zh-Hans.json` (lightbox captions included) and dumps the full key list as JSON.

Strings to leave English: add the class to `SKIP` in `lang.js` (whole element) or simply omit the key from the dictionary (element stays as is).

## 4. Checks before pushing

1. Serve locally and load every touched page; check the phone width too (nav, cards, no horizontal scroll).
2. If the nav changed: `grep -c "NEW LABEL" index.html research.html developer.html music.html topic-*.html` must show 1 in every file.
3. New media: file sizes sane (`du -sh assets/*`), nothing from `assets/temp/` staged (`git status`).
4. Video, YouTube and Bilibili players: press play once in a real browser after deploy; headless checks cannot verify playback.
5. If any English text changed: dictionaries rebuilt (3.11) and the page checked once in 日本語 or 中文.
6. Commit message: one line saying what changed, plus bullets if several things.

## 5. Style notes (keep the voice)
- Activities and developer cards are short and casual, first person, one sentence; the formal venue strings live in Presentations.
- Developer cards lead with Heng's role or credit, not with a product description.
- Names, paper titles and event names stay as printed by the venue; song titles use the artist's spelling.
- Desktop type is scaled to 90% via `html { font-size: 90% }` at 768 px and wider; pixel-sized things (photo, door icons) were tuned by hand and do not scale with it.
