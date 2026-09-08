# Skill: Update Personal Website

This skill defines how to update Heng Zhang's personal website.

The site is four pages that share `assets/site.css`, `assets/site.js` and one nav
(two-level hover menus on desktop, grouped list in the phone menu). The nav markup
is duplicated in every page's `<header>`; when you add a section, add its entry to
the matching menu in **all four files**.

| page | contents |
|---|---|
| `index.html` (About me) | hero, `#about`, `#experience`, `#education`, `#more`, `#contact` |
| `research.html` (As a Researcher) | `#activities`, `#research`, `#publications`, `#presentations`, `#funding`, `#contact` |
| `developer.html` (As a Developer) | `#projects` with one `<article class="dev-project" id="…">` per project (media left, text right; add `dev-project--flip` to swap), `#contact` |
| `music.html` (As a Music Lover) | `#music` featured Bilibili player, `#covers` playlist of `.music-tile` buttons (data-bvid/name/sub/date/dur/views; cover in `assets/music/<bvid>.jpg`), `#contact` |

`#contact` (Get in Touch) is repeated at the bottom of every page; the "Contact" nav item links to it on the current page.
When the user says they have new info to add, use the relevant section below to know exactly what to ask for, then make the edit.

---

## How to Use This Skill

1. User says something like "I have a new funding" or "add a publication"
2. Ask the user for the required fields listed under that section (only the ones missing)
3. Edit `index.html` following the pattern described
4. Optionally commit and push if the user requests it

---

## Sections & Required Info

---

### Funding
**Location in file**: `research.html` → `<section id="funding">` → inside `<ul class="funding-list">`

**Pattern**: Each item is a `<li class="funding-item">` with collapsed/expanded state.

**Ask for**:
- Grant/award name (full)
- Short display name (used in collapsed view)
- Description / topic of the grant
- Your role (e.g., Principal Investigator, Co-Investigator, Research Collaborator)
- Total amount (¥ or other currency)
- Year range (e.g., 2025–2026)

**HTML template**:
```html
<li class="funding-item" data-expanded="false">
  <div class="funding-collapsed">
    <span class="funding-short">[SHORT NAME] ([YEAR RANGE])</span>
    <a href="#" class="read-more-link">Read more</a>
  </div>
  <div class="funding-full" style="display:none;">
    <div class="funding-grant">[FULL GRANT NAME]</div>
    <p>[DESCRIPTION / TOPIC]</p>
    <div class="funding-meta">
      <span class="funding-amount">[AMOUNT]</span>
      <span>[ROLE]</span>
    </div>
    <a href="#" class="read-less-link">Show less</a>
  </div>
</li>
```

---

### Publication
**Location in file**: `research.html` → `<section id="publications">` → inside `<div class="pub-list">`

**Pattern**: Each item is a `<li class="pub-item">` with type badge, title, authors, venue, and optional links.

**Ask for**:
- Type: `under-review` | `journal` | `conference` | `review`
- Title
- Authors (list, your name will be bolded)
- Venue (journal or conference name, year, IF if applicable)
- Link to paper (optional)
- Whether to show by default (`data-show="true"` or `"false"`)

**HTML template**:
```html
<li class="pub-item" data-category="[TYPE]" data-show="true">
  <span class="pub-type">[TYPE LABEL]</span>
  <h3 class="pub-title">[TITLE]</h3>
  <p class="pub-authors">[AUTHORS — bold your name with <strong>]</strong></p>
  <p class="pub-venue">[VENUE, YEAR] [IF: X.XX]</p>
  <div class="pub-links">
    <a href="[URL]" target="_blank">Paper</a>
  </div>
</li>
```

---

### Experience (Career)
**Location in file**: `index.html` → `<section id="experience">` → inside `<div class="timeline">`

**Pattern**: Each item is a `<div class="timeline-item">` with date, title, org, description.

**Ask for**:
- Date range (e.g., April 2025 – Present)
- Job title
- Organization name
- 1–2 sentence description

**HTML template**:
```html
<div class="timeline-item">
  <div class="timeline-date">[DATE RANGE]</div>
  <h3 class="timeline-title">[JOB TITLE]</h3>
  <div class="timeline-org">[ORGANIZATION]</div>
  <p class="timeline-desc">[DESCRIPTION]</p>
</div>
```

---

### Education
**Location in file**: `index.html` → `<section id="education">` → inside `<div class="timeline">`

**Same pattern as Experience.**

**Ask for**:
- Date range
- Degree (e.g., Ph.D. in AI & Information Science)
- School name
- 1–2 sentence description (thesis, focus, etc.)

---

### Research Project
**Location in file**: `research.html` → `<section id="research">` → inside `<div class="projects-grid">`

**Pattern**: Each card is a `<div class="project-card">` with image, title, short and full descriptions.

**Ask for**:
- Project title
- Image filename (place image in root or an `images/` folder)
- Short description (1–2 sentences, shown by default)
- Full description (full paragraph, shown on "Read more")
- Number of publications/submissions linked (optional)

**HTML template**:
```html
<div class="project-card">
  <div class="project-image">
    <img src="[IMAGE PATH]" alt="[TITLE]">
  </div>
  <div class="project-content">
    <h3>[TITLE]</h3>
    <div class="project-short">
      <p>[SHORT DESCRIPTION] <a href="#" class="read-more-link">Read more</a></p>
    </div>
    <div class="project-full" style="display:none;">
      <p>[FULL DESCRIPTION]</p>
      <a href="#" class="read-less-link">Show less</a>
    </div>
  </div>
</div>
```

---

### Activity (photo card)
**Location in file**: `research.html` → `<section id="activities">` → inside `<div class="activities-grid">`, newest first.

**Ask for**: kicker (e.g. "Poster · NEURO2026"), title, meta line (venue · place · date), one sentence, 1–3 photos.
Put web-sized JPEGs (≤1600 px long side) in `assets/activities/`; originals stay out of git.

**HTML template** (`--ar` = image width / height; class by orientation: portrait / landscape / square; add `activity-card--flip` to put the photos on the left):
```html
<div class="activity-card">
  <div class="activity-content">
    <p class="activity-kicker">[KICKER]</p>
    <h3>[TITLE]</h3>
    <p class="activity-meta">[VENUE · PLACE · DATE]</p>
    <p>[ONE SENTENCE]</p>
  </div>
  <div class="activity-preview" aria-hidden="true">
    <button class="stack-card stack-card--portrait" style="--ar: 1130 / 1600" type="button" data-full="assets/activities/[FILE]" data-caption="[CAPTION]"><img src="assets/activities/[FILE]" alt="[CAPTION]" loading="lazy"></button>
  </div>
</div>
```

---

### Presentation
**Location in file**: `research.html` → `<section id="presentations">` → inside `<div class="pres-list">`, newest first. Compact rows: badge (Talk / Poster), title, one meta line.

**Ask for**:
- Title
- Type: Oral or Poster
- Presenters / authors
- Event/venue name, city, country
- Date (e.g., Oct 23, 2025)

**HTML template**:
```html
<div class="pres-item">
  <span class="pres-badge">[Talk/Poster]</span>
  <p class="pres-title">[TITLE]</p>
  <p class="pres-meta">[VENUE], [CITY], [COUNTRY], [DATE]</p>
</div>
```

---

### Hero (Name, Title, Tagline, Photo)
**Location in file**: `index.html` → `<section class="hero">`

**Ask for**:
- New job title / affiliation (if changed)
- New tagline (optional, 1–2 sentences)
- New profile photo filename (place in root directory)

---

### About (Bio & Skills)
**Location in file**: `index.html` → `<section id="about">`

**Ask for**:
- Updated bio paragraph(s)
- Any new skill tags to add (shown as inline badges)

---

## Notes

- Items within each section are listed **newest first** (top of list = most recent).
- Styles live in `assets/site.css`, scripts in `assets/site.js`; pages contain markup only.
- After editing, the user can commit with: `git add -A && git commit -m "..."` and push to deploy.
- Images should be placed in the repo root or an `images/` subfolder, then referenced by relative path.
