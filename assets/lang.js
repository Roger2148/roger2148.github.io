/* lang.js — inline translation (same design as the paper site).
 *
 * The English page is the source of truth and is never edited by this script.
 * For another language a dictionary (assets/i18n/<lang>.json) maps the English
 * innerHTML of each leaf text element (SVGs tokenised as {svg0}, {svg1}, …) to a
 * translated innerHTML with the same inline tags. Switching back to English
 * restores every touched node verbatim from a cache. Anything not found in the
 * dictionary stays English (names, paper titles, song titles, venues).
 *
 * Language choice: a menu pick is stored (localStorage 'site-lang') and wins;
 * otherwise the browser's preferred languages are matched; otherwise English.
 *
 * window.__I18N = { get, set, t, collect, apply } — collect() lists this page's keys.
 */
(function () {
  const KEY = 'site-lang', CODES = { en: 'EN', 'zh-Hans': '简', 'zh-Hant': '繁', ja: 'JA' };
  const TEXT_TAGS = new Set(['H1', 'H2', 'H3', 'H4', 'H5', 'P', 'LI', 'TD', 'TH', 'DT', 'DD', 'FIGCAPTION', 'BUTTON', 'LABEL', 'SUMMARY', 'BLOCKQUOTE']);
  const SEL = '.section-label,.nav-menu__label,.nav-menu__sub,.nav__item,.nav-mobile__title,.nav-mobile a,.hero-path__label,'
    + '.activity-kicker,.activity-meta,.activity-new,.pres-badge,.pres-meta,.pub-type,.timeline-date,.timeline-org,'
    + '.music-tile__meta,.artist__tags,.dev-meta,.dev-links a,.funding-short,.funding-grant,.funding-meta,.funding-amount,'
    + '.site-preview__badge,.site-preview__caption,.dev-media__caption,.music-now__meta,.music-now__link,.topic-back,'
    + '.hero-title,.hero-tagline,.hero-links a,.contact-item-label,.contact-socials a,.project-title-link,.read-more,.read-less,'
    + '.music-channel,.skill-tag,.about-skills span,.contact-item a';
  const INLINE = new Set(['A', 'SPAN', 'STRONG', 'EM', 'B', 'I', 'SUB', 'SUP', 'CODE', 'BR', 'SMALL', 'ABBR', 'MARK', 'KBD', 'WBR', 'TIME',
    'svg', 'path', 'circle', 'line', 'rect', 'polygon', 'g', 'text', 'use', 'defs', 'marker', 'tspan', 'polyline', 'ellipse', 'stop', 'linearGradient', 'radialGradient']);
  const SKIP = 'script,style,pre,code,iframe,video,textarea,input,select,noscript,canvas,[data-i18n-skip],.nav-lang,'
    + '.nav-logo,.hero-text h1,.pub-title,.pub-authors,.pub-venue,.pub-links,.pres-title,.activity-content h3,'
    + '.music-tile__name,.music-now h3,.artist__name,.artist__jp,.dev-project h3,.lightbox';

  function detect() {
    const prefs = (navigator.languages && navigator.languages.length) ? navigator.languages : [navigator.language || ''];
    for (const raw of prefs) {
      const t = String(raw).toLowerCase();
      if (t.startsWith('ja')) return 'ja';
      if (t.startsWith('zh')) return /hant|-tw|-hk|-mo/.test(t) ? 'zh-Hant' : 'zh-Hans';
      if (t.startsWith('en')) return 'en';
    }
    return 'en';
  }
  let lang = null;
  try { lang = localStorage.getItem(KEY); } catch (e) {}
  if (!lang || !CODES[lang]) lang = detect();

  const dicts = {};                       // lang -> {key: translation}
  const originals = new WeakMap();        // element -> original innerHTML
  const touched = new Set();              // elements currently translated
  let titleOriginal = null;

  const norm = (s) => s.replace(/\s+/g, ' ').trim();
  function inlineOnly(el) {
    for (const c of el.querySelectorAll('*')) if (!INLINE.has(c.tagName)) return false;
    return true;
  }
  function keyOf(el) {
    const clone = el.cloneNode(true); let i = 0;
    clone.querySelectorAll('svg').forEach((s) => s.replaceWith(document.createTextNode('{svg' + (i++) + '}')));
    return norm(clone.innerHTML);
  }
  function isCand(el) { return (TEXT_TAGS.has(el.tagName) || el.matches(SEL)) && inlineOnly(el); }
  function candidates(root) {
    const out = [];
    (function walk(el) {
      if (el.nodeType !== 1) return;
      if (el.matches(SKIP) || el.closest(SKIP)) return;
      if (isCand(el) && !el.querySelector(SEL)) { out.push(el); return; }
      for (const c of el.children) walk(c);
    })(root || document.body);
    return out;
  }
  function meaningful(el) {
    const t = norm(el.textContent); return t.length >= 2 && !/^[\d\W_]+$/.test(t);
  }

  function translateEl(el, dict) {
    const k = keyOf(el); const t = dict[k];
    if (!t) return;
    if (!originals.has(el)) originals.set(el, el.innerHTML);
    const svgs = Array.from(el.querySelectorAll('svg')).map((s) => s.outerHTML);
    el.innerHTML = t.replace(/\{svg(\d+)\}/g, (m, i) => svgs[Number(i)] || '');
    touched.add(el);
  }
  function restoreAll() {
    touched.forEach((el) => { if (originals.has(el)) el.innerHTML = originals.get(el); });
    touched.clear();
    if (titleOriginal !== null) { document.title = titleOriginal; titleOriginal = null; }
  }
  function loadDict(l) {
    if (dicts[l]) return Promise.resolve(dicts[l]);
    return fetch('assets/i18n/' + l + '.json').then((r) => r.ok ? r.json() : {}).then((d) => (dicts[l] = d)).catch(() => (dicts[l] = {}));
  }
  function labels() {
    document.documentElement.lang = lang;
    document.documentElement.dataset.lang = lang;
    document.querySelectorAll('.nav-lang__code').forEach((el) => { el.textContent = CODES[lang]; });
    document.querySelectorAll('a[data-lang], button[data-lang]').forEach((el) => {
      const on = el.dataset.lang === lang;
      el.setAttribute('aria-checked', String(on));
      el.classList.toggle('is-active', on);
    });
  }
  let applying = false;
  function applyAll(root) {
    if (lang === 'en') return;
    const dict = dicts[lang]; if (!dict) return;
    applying = true;
    try {
      candidates(root).forEach((el) => { if (meaningful(el)) translateEl(el, dict); });
      if (!root && dict[titleOriginal === null ? document.title : titleOriginal]) {
        if (titleOriginal === null) titleOriginal = document.title;
        document.title = dict[titleOriginal];
      }
    } finally { applying = false; }
  }
  function apply() {
    labels();
    if (lang === 'en') { restoreAll(); document.dispatchEvent(new CustomEvent('langchange', { detail: lang })); return; }
    loadDict(lang).then(() => { restoreAll(); applyAll(); document.dispatchEvent(new CustomEvent('langchange', { detail: lang })); });
  }
  function set(l) { if (!CODES[l]) return; lang = l; try { localStorage.setItem(KEY, l); } catch (e) {} apply(); }
  function t(s) { const d = lang !== 'en' && dicts[lang]; return (d && d[s]) || s; }

  // content that scripts render later (lightbox captions, music meta): translate new nodes too
  let pending = null;
  new MutationObserver((muts) => {
    if (applying || lang === 'en' || !dicts[lang]) return;
    let added = false;
    for (const m of muts) if (m.addedNodes && m.addedNodes.length) { added = true; break; }
    if (!added || pending) return;
    pending = setTimeout(() => { pending = null; applyAll(); }, 250);
  }).observe(document.body, { childList: true, subtree: true });

  function closeMenus() {
    document.querySelectorAll('.nav-lang.is-open').forEach((g) => {
      g.classList.remove('is-open');
      const b = g.querySelector('.nav-lang__btn'); if (b) b.setAttribute('aria-expanded', 'false');
    });
  }
  document.addEventListener('click', (e) => {
    const el = e.target.closest('a[data-lang], button[data-lang]');
    if (el) {
      e.preventDefault(); set(el.dataset.lang); closeMenus();
      const btn = el.closest('.nav-lang') && el.closest('.nav-lang').querySelector('.nav-lang__btn');
      if (btn) btn.blur();
      return;
    }
    const btn = e.target.closest('.nav-lang__btn');       // tap toggle (touch devices have no hover)
    if (btn) {
      const g = btn.closest('.nav-lang'); const open = !g.classList.contains('is-open');
      closeMenus(); if (open) { g.classList.add('is-open'); btn.setAttribute('aria-expanded', 'true'); }
      return;
    }
    if (!e.target.closest('.nav-lang')) closeMenus();
  });
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape') closeMenus(); });

  function collect() {                    // extraction helper for building dictionaries
    const seen = new Set(), strings = [];
    candidates().forEach((el) => { if (!meaningful(el)) return; const k = keyOf(el); if (!seen.has(k)) { seen.add(k); strings.push(k); } });
    return { title: document.title, strings };
  }
  window.__I18N = { get: () => lang, set, t, collect, apply };
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', apply); else apply();
})();
