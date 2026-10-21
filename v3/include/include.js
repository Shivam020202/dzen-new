/**
 * D'Zen Derma - Dynamic Partials Include Loader
 * Loads include/header.html and include/footer.html into #site-header and #site-footer.
 * When changes are made to header.html or footer.html, every page reflects them automatically.
 */
(function () {
    'use strict';

    // Fallback embedded markup for offline or direct file:/// access where CORS blocks fetch
    const EMBEDDED_HEADER = `<!-- ═══════ Floating Pill Navbar v3 ═══════ -->
<nav id="pill-nav" class="pnav" aria-label="Main navigation">
    <!-- Left: Book Now -->
    <div class="pnav__left">
        <a href="../newthree.html#book" class="pnav__cta">
            Book
            <img src="nemonic1.png" class="btn-icon" alt="icon" />
        </a>
    </div>

    <!-- Center: logo -->
    <a href="index.html" class="pnav__logo" aria-label="Home">
        <img src="../images/logo1.png" alt="D'Zen Derma" />
    </a>

    <!-- Right: hamburger -->
    <div class="pnav__right">
        <button class="pnav__burger" id="pnav-burger" aria-label="Open menu">
            <span></span><span></span><span></span>
        </button>
    </div>
</nav>

<!-- Mobile drawer -->
<div class="pnav-overlay" id="pnav-overlay"></div>
<aside class="pnav-drawer" id="pnav-drawer" aria-label="Menu">
    <button class="pnav-drawer__close" id="pnav-close" aria-label="Close menu">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
            stroke-linecap="round">
            <path d="M18 6L6 18M6 6l12 12" />
        </svg>
    </button>
    <ul class="pnav-drawer__list">
        <li><a href="our-philosophy.html">Who we are <span>→</span></a></li>
        <li><a href="treatments.html">Treatments <span>→</span></a></li>
        <li><a href="concerns.html">Concerns <span>→</span></a></li>
        <li><a href="treatments.html#cat-wellness">Medicine &amp; Wellness Programmes <span>→</span></a></li>
        <li><a href="dzen-signatures.html">Signature Treatments <span>→</span></a></li>
        <li><a href="pre-bridal.html">Bridal Programs <span>→</span></a></li>
        <li><a href="men.html">Men's Aesthetics <span>→</span></a></li>
        <li><a href="workshops-training.html">Workshops &amp; Training <span>→</span></a></li>
        <li><a href="media.html">Press &amp; Media <span>→</span></a></li>
    </ul>
</aside>`;

    const EMBEDDED_FOOTER = `<!-- ═══════════════════════════════════════════════════════════
     CTA + FOOTER OVERLAP SECTION
     ═══════════════════════════════════════════════════════════ -->
<div class="footer-stack-root">
    <!-- CTA Card -->
    <div class="footer-cta-card-wrapper">
        <div class="footer-cta-card">
            <div class="section-header text-center mb-4">
                <span class="section-subtitle">BEGIN YOUR JOURNEY</span>
                <div class="nemonic-separator mx-auto mb-3">
                    <div class="nemonic-line"></div>
                    <img src="logo-header.png" alt="nemonic" class="nemonic-icon" />
                    <div class="nemonic-line"></div>
                </div>
            </div>
            <h2 class="footer-cta-heading">Ready to reveal your most radiant self?</h2>
            <p class="footer-cta-sub">Join thousands who've discovered the art of effortless confidence — crafted for your skin, your story.</p>
            <a href="../newthree.html#book" class="dz-cta footer-cta-btn">
                <span>Book a Consultation</span>
                <img src="nemonic1.png" class="btn-icon" alt="icon" />
            </a>
        </div>
    </div>

    <!-- Footer Reveal Wrapper -->
    <div class="footer-reveal-wrapper">
        <footer class="site-footer" aria-label="Site footer">
            <div class="footer-top">
                <!-- Brand column -->
                <div class="footer-brand">
                    <h2 class="footer-logo-text">D'ZEN DERMA</h2>
                    <p class="footer-tagline">
                        Where the finest techniques in aesthetic medicine reveal your most luminous, confident self. Crafted for your skin, your story.
                    </p>
                    <div class="footer-socials">
                        <a href="https://instagram.com/dzenderma" class="footer-social-icon" aria-label="Instagram" target="_blank" rel="noopener">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">
                                <rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect>
                                <circle cx="12" cy="12" r="4"></circle>
                                <circle cx="17.5" cy="6.5" r="0.5" fill="currentColor" stroke="none"></circle>
                            </svg>
                        </a>
                    </div>
                </div>

                <!-- Nav columns -->
                <div class="footer-nav-col">
                    <ul class="footer-nav-list">
                        <li><a href="index.html">HOME</a></li>
                        <li><a href="about.html">ABOUT US</a></li>
                        <li><a href="treatments.html">TREATMENTS</a></li>
                        <li><a href="#">WELLNESS PROGRAMS</a></li>
                        <li><a href="../concerns.html">CONCERN</a></li>
                    </ul>
                </div>
                <div class="footer-nav-col">
                    <ul class="footer-nav-list">
                        <li><a href="#">MEMBERSHIPS</a></li>
                        <li><a href="#">GIFT CARD</a></li>
                        <li><a href="#">CAREERS</a></li>
                        <li><a href="contact.html">CONTACT</a></li>
                    </ul>
                </div>

                <!-- Contact info column -->
                <div class="footer-contact-col">
                    <div class="footer-contact-row">
                        <div class="footer-contact-item">
                            <span class="footer-contact-label">Gurgaon Clinic</span>
                            <span class="footer-contact-value">Golf Course Road, Sector 28, Gurugram</span>
                        </div>
                        <div class="footer-contact-item">
                            <span class="footer-contact-label">Delhi Clinic</span>
                            <span class="footer-contact-value">Vikram Vihar, Lajpat Nagar 4, New Delhi</span>
                        </div>
                        <div class="footer-contact-item">
                            <span class="footer-contact-label">Phone &amp; WhatsApp</span>
                            <a href="tel:+919878885046" class="footer-contact-value footer-contact-link">+91-9878885046</a>
                        </div>
                        <div class="footer-contact-item">
                            <span class="footer-contact-label">Email</span>
                            <a href="mailto:rahul@dzenderma.com" class="footer-contact-value footer-contact-link">rahul@dzenderma.com</a>
                        </div>
                    </div>
                </div>
            </div>

            <div class="footer-divider"></div>

            <div class="footer-bottom">
                <p class="footer-copyright">© 2026, D'Zen Derma | All Rights Reserved | All prices are exclusive of tax</p>
                <div class="footer-legal-links">
                    <a href="#">Privacy Policy</a>
                    <a href="#">Terms &amp; Conditions</a>
                    <a href="#">Booking &amp; Cancellation Policy</a>
                </div>
            </div>

            <div class="footer-bottom-strip"></div>
        </footer>
    </div>
</div>

<!-- Embossed Brand Section -->
<section class="embossed-section" id="brandSection">
    <div class="embossed-grain"></div>
    <div class="embossed-lighting"></div>

    <!-- Book Now Pill Button -->
    <a href="../newthree.html#book" class="book-pill-btn" aria-label="Book appointment">
        BOOK NOW
        <img src="nemonic1.png" alt="icon" class="btn-icon">
    </a>

    <!-- Debossed Typography Block -->
    <div class="typography-stage">
        <h1 class="deboss-wordmark" id="wordmark">D'ZEN DERMA</h1>
        <p class="deboss-tagline">Elevating You Inside Out</p>
    </div>
</section>
`;

    // Initialize Pill Navigation interactions
    function initPillNav() {
        const nav = document.getElementById('pill-nav');
        if (!nav) return;

        const burger = document.getElementById('pnav-burger');
        const closeBtn = document.getElementById('pnav-close');
        const drawer = document.getElementById('pnav-drawer');
        const overlay = document.getElementById('pnav-overlay');

        if (!burger || !drawer) return;

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

        // Skip if already populated
        if (container.children && container.children.length > 0) {
            if (typeof callback === 'function') callback();
            return;
        }

        let loaded = false;
        const isHttp = window.location.protocol === 'http:' || window.location.protocol === 'https:';

        if (isHttp) {
            const candidatePaths = [
                'include/' + filename,
                'includes/' + filename,
                '../include/' + filename,
                '../includes/' + filename
            ];
            for (const path of candidatePaths) {
                try {
                    const res = await fetch(path + '?v=' + Date.now());
                    if (res.ok) {
                        const html = await res.text();
                        container.innerHTML = html;
                        loaded = true;
                        break;
                    }
                } catch (err) {
                    // Try next candidate
                }
            }
        }

        // On file:/// or fallback, initialize embedded HTML if container is empty
        if (!loaded) {
            const fallback = filename === 'header.html' ? EMBEDDED_HEADER : EMBEDDED_FOOTER;
            if (fallback && (!container.innerHTML || container.innerHTML.trim() === '')) {
                container.innerHTML = fallback;
            }
        }

        if (typeof callback === 'function') {
            callback();
        }
    }

    // Run loader
    function initIncludes() {
        loadPartial('site-header', 'header.html', initPillNav);
        loadPartial('site-footer', 'footer.html');
    }

    // Run immediately if containers are already in DOM, else on DOMContentLoaded
    if (document.getElementById('site-header') || document.getElementById('site-footer')) {
        initIncludes();
    } else if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initIncludes);
    } else {
        initIncludes();
    }
})();
