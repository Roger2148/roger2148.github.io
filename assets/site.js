// Mobile menu toggle
function toggleMenu() {
    const t = document.querySelector('.nav-toggle'), m = document.querySelector('.nav-mobile');
    if (t) t.classList.toggle('active');
    if (m) m.classList.toggle('active');
}

// Close mobile menu on resize
window.addEventListener('resize', () => {
    if (window.innerWidth >= 768) {
        const t = document.querySelector('.nav-toggle'), m = document.querySelector('.nav-mobile');
        if (t) t.classList.remove('active');
        if (m) m.classList.remove('active');
    }
});

// Toggle section collapse
function toggleSection(sectionId) {
    const header = document.querySelector(`#${sectionId} .section-header`);
    const content = document.querySelector(`#${sectionId} .section-content`);

    header.classList.toggle('collapsed');
    content.classList.toggle('collapsed');
}

// Auto-convert all sections to collapsible on page load
document.addEventListener('DOMContentLoaded', function () {
    const sections = document.querySelectorAll('section[id]:not(#about):not(#more):not([data-static])');

    sections.forEach(section => {
        const sectionId = section.id;
        const container = section.querySelector('.container');

        if (!container) return;

        // Find the title elements
        const label = container.querySelector('.section-label');
        const title = container.querySelector('h2');

        if (!label || !title) return;

        // Check if already has section-header (skip if yes)
        if (container.querySelector('.section-header')) return;

        // Create header wrapper
        const header = document.createElement('div');
        header.className = 'section-header';
        header.onclick = () => toggleSection(sectionId);

        const titleWrapper = document.createElement('div');
        titleWrapper.className = 'section-title-wrapper';
        titleWrapper.appendChild(label);
        titleWrapper.appendChild(title);

        const icon = document.createElement('div');
        icon.className = 'section-collapse-icon';
        icon.innerHTML = '<div class="icon-minus"></div><div class="icon-chevron"></div>';

        header.appendChild(titleWrapper);
        header.appendChild(icon);

        // Wrap content
        const contentWrapper = document.createElement('div');
        contentWrapper.className = 'section-content';

        // Move all children except the newly created header into content wrapper
        while (container.firstChild) {
            if (container.firstChild === header) break;
            contentWrapper.appendChild(container.firstChild);
        }

        // Insert header and content into container
        container.insertBefore(header, container.firstChild);
        container.appendChild(contentWrapper);
    });
});

// Smooth scroll for Safari
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        const href = this.getAttribute('href');
        if (href === '#' || href.length < 2) return;
        e.preventDefault();
        const target = document.querySelector(href);
        if (target) {
            target.scrollIntoView({ behavior: 'smooth' });
        }
    });
});


// Activities: fanned photo stack -> lightbox
(function () {
    let lb, img, cap;
    function ready() {           // the overlay markup sits at the end of <body>, after this script
        if (!lb) { lb = document.getElementById('lightbox'); if (!lb) return false; img = lb.querySelector('img'); cap = lb.querySelector('figcaption'); }
        return true;
    }
    document.addEventListener('click', function (e) {
        if (!ready()) return;
        const card = e.target.closest('.stack-card');
        if (card) {
            img.src = card.dataset.full; img.alt = card.dataset.caption || '';
            cap.textContent = card.dataset.caption || '';
            lb.classList.add('is-open'); document.body.style.overflow = 'hidden';
            return;
        }
        if (e.target.closest('#lightbox')) {
            lb.classList.remove('is-open'); document.body.style.overflow = ''; img.src = '';
        }
    });
    document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape' && ready() && lb.classList.contains('is-open')) {
            lb.classList.remove('is-open'); document.body.style.overflow = ''; img.src = '';
        }
    });
})();

// Publication filtering
function filterPublications(category) {
    const publications = document.querySelectorAll('#publications .pub-item');
    const buttons = document.querySelectorAll('.pub-filter-btn');

    // Update active button
    buttons.forEach(btn => btn.classList.remove('active'));
    event.target.classList.add('active');

    // Filter publications
    publications.forEach(pub => {
        if (pub.getAttribute('data-show') === 'false') {
            return; // Keep manually hidden items hidden
        }

        if (category === 'all') {
            pub.style.display = 'block';
        } else {
            if (pub.getAttribute('data-category') === category) {
                pub.style.display = 'block';
            } else {
                pub.style.display = 'none';
            }
        }
    });
}

// Toggle project card expansion
function toggleProject(event, link) {
    event.preventDefault();
    const card = link.closest('.project-card');
    const shortDesc = card.querySelector('.project-short');
    const fullDesc = card.querySelector('.project-full');
    const isExpanded = card.getAttribute('data-expanded') === 'true';

    if (isExpanded) {
        // Collapse
        fullDesc.style.display = 'none';
        shortDesc.style.display = 'block';
        card.setAttribute('data-expanded', 'false');
    } else {
        // Expand
        fullDesc.style.display = 'block';
        shortDesc.style.display = 'none';
        card.setAttribute('data-expanded', 'true');
    }
}

// Toggle funding item expansion
function toggleFunding(event, link) {
    event.preventDefault();
    const item = link.closest('.funding-item');
    const collapsedDiv = item.querySelector('.funding-collapsed');
    const fullDiv = item.querySelector('.funding-full');
    const isExpanded = item.getAttribute('data-expanded') === 'true';

    if (isExpanded) {
        // Collapse
        fullDiv.style.display = 'none';
        collapsedDiv.style.display = 'block';
        item.setAttribute('data-expanded', 'false');
    } else {
        // Expand
        fullDiv.style.display = 'block';
        collapsedDiv.style.display = 'none';
        item.setAttribute('data-expanded', 'true');
    }
}

// Scroll indicator opacity control
const scrollIndicator = document.getElementById('scrollIndicator');
const backToTop = document.getElementById('backToTop');

window.addEventListener('scroll', function () {
    if (!scrollIndicator || !backToTop) return;
    const scrollTop = window.pageYOffset || document.documentElement.scrollTop;

    // Scroll indicator: fade out when scrolling down
    const fadeDistance = window.innerHeight * 0.35;
    const opacity = Math.max(0, 0.6 - (scrollTop / fadeDistance) * 0.6);
    scrollIndicator.style.opacity = opacity;

    // Back-to-top button: fade in when scrolled 20% of page
    const docHeight = document.documentElement.scrollHeight - window.innerHeight;
    const scrollPercent = scrollTop / docHeight;

    if (scrollPercent > 0.2) {
        backToTop.classList.add('visible');
    } else {
        backToTop.classList.remove('visible');
    }
});

// Mark the current page in the nav
(function () {
    let page = (location.pathname.split('/').pop() || 'index.html').toLowerCase();
    if (page.startsWith('topic-')) page = 'research.html';   // topic pages belong to the researcher section
    document.querySelectorAll('.nav__item[href], .nav-mobile__title[href]').forEach((a) => {
        const target = a.getAttribute('href').split('#')[0].toLowerCase();
        if (target === page) a.classList.add('is-active');
    });
})();

// Click-to-load YouTube embeds (privacy-enhanced domain, autoplay on click)
document.addEventListener('click', function (e) {
    const box = e.target.closest('.yt-lite');
    if (!box || box.querySelector('iframe')) return;
    const id = box.dataset.yt; if (!id) return;
    const f = document.createElement('iframe');
    f.src = 'https://www.youtube-nocookie.com/embed/' + id + '?autoplay=1&rel=0';
    f.title = box.dataset.title || 'YouTube video';
    f.allow = 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share';
    f.allowFullscreen = true;
    f.referrerPolicy = 'strict-origin-when-cross-origin';   // YouTube needs an origin Referer, else error 153
    f.setAttribute('referrerpolicy', 'strict-origin-when-cross-origin');
    box.appendChild(f);
});

// Music page: click-to-load Bilibili player + playlist that swaps the featured video
(function () {
    const stage = document.getElementById('bili-stage'); if (!stage) return;
    const cover = document.getElementById('bili-cover'), title = document.getElementById('bili-title'), meta = document.getElementById('bili-meta'), link = document.getElementById('bili-link');
    function play(bvid) {
        stage.dataset.bvid = bvid;
        let f = stage.querySelector('iframe');
        if (!f) { f = document.createElement('iframe'); f.allowFullscreen = true; f.setAttribute('allow', 'autoplay; fullscreen; picture-in-picture'); f.setAttribute('scrolling', 'no'); stage.appendChild(f); }
        f.src = 'https://player.bilibili.com/player.html?bvid=' + bvid + '&page=1&high_quality=1&danmaku=0&autoplay=1';
        stage.classList.add('is-playing');
    }
    stage.addEventListener('click', function () { if (!stage.classList.contains('is-playing')) play(stage.dataset.bvid); });
    document.querySelectorAll('.music-tile').forEach(function (t) {
        t.addEventListener('click', function () {
            const d = t.dataset;
            document.querySelectorAll('.music-tile.is-current').forEach(function (x) { x.classList.remove('is-current'); });
            t.classList.add('is-current');
            if (cover) cover.src = 'assets/music/' + d.bvid + '.jpg';
            if (title) title.textContent = d.name;
            const tr = (s) => (window.__I18N ? window.__I18N.t(s) : s);
            if (meta) meta.textContent = (d.sub ? tr(d.sub) + ' · ' : '') + tr(d.date) + ' · ' + d.dur + ' · ' + Number(d.views).toLocaleString() + ' ' + tr('views');
            if (link) link.href = 'https://www.bilibili.com/video/' + d.bvid;
            play(d.bvid);
            document.getElementById('music').scrollIntoView({ behavior: 'smooth', block: 'start' });
        });
    });
})();
