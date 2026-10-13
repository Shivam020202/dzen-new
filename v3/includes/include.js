/**
 * D'Zen Derma - Dynamic Partials Include Loader
 * Loads include/header.html and include/footer.html into #site-header and #site-footer.
 * When changes are made to header.html or footer.html, every page reflects them automatically.
 */
(function () {
    'use strict';

    // Auto-detect include directory path relative to current page
    function getIncludePath(filename) {
        // Current directory is same level as include/
        return 'include/' + filename;
    }

    // Initialize Pill Navigation interactions
    function initPillNav() {
        const nav = document.getElementById('pill-nav');
        if (!nav) return;

        const burger = document.getElementById('pnav-burger');
        const closeBtn = document.getElementById('pnav-close');
        const drawer = document.getElementById('pnav-drawer');
        const overlay = document.getElementById('pnav-overlay');

        if (!burger || !drawer) return;

        // Clean previous listeners if re-initialized
        if (burger._hasPnavListener) return;
        burger._hasPnavListener = true;

        function openDrawer() {
            drawer?.classList.add('is-open');
            overlay?.classList.add('is-open');
            burger?.classList.add('is-active');
        }
        function closeDrawer() {
            drawer?.classList.remove('is-open');
            overlay?.classList.remove('is-open');
            burger?.classList.remove('is-active');
        }

        burger.addEventListener('click', function (e) {
            e.stopPropagation();
            if (drawer.classList.contains('is-open')) closeDrawer();
            else openDrawer();
        });

        closeBtn?.addEventListener('click', function (e) {
            e.stopPropagation();
            closeDrawer();
        });

        overlay?.addEventListener('click', function (e) {
            e.stopPropagation();
            closeDrawer();
        });

        document.addEventListener('keydown', function (e) {
            if (e.key === 'Escape') closeDrawer();
        });

        // Scroll listener for sticky & opaque transition
        let ticking = false;
        function onScroll() {
            if (ticking) return;
            ticking = true;
            requestAnimationFrame(function () {
                const y = window.scrollY;
                nav.classList.toggle('is-scrolled', y > 30);
                ticking = false;
            });
        }

        window.addEventListener('scroll', onScroll, { passive: true });
        onScroll();

        // Highlight active page link in the drawer
        const currentFile = window.location.pathname.split('/').pop() || 'index.html';
        const drawerLinks = drawer.querySelectorAll('.pnav-drawer__list a');
        drawerLinks.forEach(function (link) {
            const href = link.getAttribute('href');
            if (href && (href === currentFile || href.endsWith('/' + currentFile))) {
                link.classList.add('active');
            }
        });
    }

    // Expose init function globally so script.js can also call it
    window.initPillNav = initPillNav;

    // Fetch and inject an include snippet
    async function loadPartial(containerId, filename, callback) {
        const container = document.getElementById(containerId);
        if (!container) return;

        // If served over HTTP/HTTPS, fetch dynamically to get live updates
        const isHttp = window.location.protocol === 'http:' || window.location.protocol === 'https:';

        if (isHttp) {
            try {
                const url = getIncludePath(filename) + '?v=' + Date.now();
                const res = await fetch(url);
                if (res.ok) {
                    const html = await res.text();
                    container.innerHTML = html;
                    if (typeof callback === 'function') callback();
                    return;
                }
            } catch (err) {
                console.warn('[D\'Zen Include] Could not fetch ' + filename + ':', err);
            }
        }

        // On file:/// or fallback, initialize whatever content is already in the DOM
        if (typeof callback === 'function') {
            callback();
        }
    }

    // Run loader
    function initIncludes() {
        loadPartial('site-header', 'header.html', initPillNav);
        loadPartial('site-footer', 'footer.html');
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initIncludes);
    } else {
        initIncludes();
    }
})();
