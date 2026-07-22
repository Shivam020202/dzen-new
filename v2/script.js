/* =========================================================
   D'Zen Derma - v2 Extract Scripts
   Contains controllers for Navbar and Hero Slider sections
   ========================================================= */

(function () {
    'use strict';

    /* =========================================================
       FLOATING PILL NAVBAR v3 — Controller
       ========================================================= */
    const nav = document.getElementById('pill-nav');
    if (nav) {
        const burger  = document.getElementById('pnav-burger');
        const closeBtn = document.getElementById('pnav-close');
        const drawer  = document.getElementById('pnav-drawer');
        const overlay = document.getElementById('pnav-overlay');

        /* ── Mobile drawer ── */
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

        burger?.addEventListener('click', openDrawer);
        closeBtn?.addEventListener('click', closeDrawer);
        overlay?.addEventListener('click', closeDrawer);
        document.addEventListener('keydown', e => { if (e.key === 'Escape') closeDrawer(); });

        /* ── Scroll: opaque + hide/reveal ── */
        let lastY = 0;
        let ticking = false;

        function onScroll() {
            if (ticking) return;
            ticking = true;
            requestAnimationFrame(() => {
                const y = window.scrollY;
                // Scrolled state (more opaque)
                nav.classList.toggle('is-scrolled', y > 30);
                lastY = y;
                ticking = false;
            });
        }

        window.addEventListener('scroll', onScroll, { passive: true });
        onScroll();
    }

    /* =========================================================
       HERO SLIDER — Interactive Slider Controller
       ========================================================= */
    const slider = document.querySelector('.hero-slider');
    if (slider) {
        const slides = document.querySelectorAll('.hero-slide');
        const dots = document.querySelectorAll('.hero-dot');
        const prevBtn = document.querySelector('.hero-nav-btn.prev-btn');
        const nextBtn = document.querySelector('.hero-nav-btn.next-btn');
        let currentSlide = 0;
        const slideCount = slides.length;

        if (slideCount > 0) {
            function goToSlide(index) {
                slides.forEach((slide, i) => {
                    slide.classList.remove('active');
                    if (dots && dots[i]) {
                        dots[i].classList.remove('active');
                    }
                });
                
                if (slides[index]) {
                    slides[index].classList.add('active');
                }
                
                if (dots && dots[index]) {
                    dots[index].classList.add('active');
                }
                currentSlide = index;
            }

            function nextSlide() {
                const next = (currentSlide + 1) % slideCount;
                goToSlide(next);
            }

            function prevSlide() {
                const prev = (currentSlide - 1 + slideCount) % slideCount;
                goToSlide(prev);
            }

            let slideInterval = setInterval(nextSlide, 6000);

            function resetAutoplay() {
                clearInterval(slideInterval);
                slideInterval = setInterval(nextSlide, 6000);
            }

            if (prevBtn) {
                prevBtn.addEventListener('click', function () {
                    prevSlide();
                    resetAutoplay();
                });
            }

            if (nextBtn) {
                nextBtn.addEventListener('click', function () {
                    nextSlide();
                    resetAutoplay();
                });
            }

            if (dots && dots.length > 0) {
                dots.forEach((dot, index) => {
                    dot.addEventListener('click', function () {
                        goToSlide(index);
                        resetAutoplay();
                    });
                });
            }
            
            // Pause auto-sliding on hover
            const heroSection = document.querySelector('.hero');
            if (heroSection) {
                heroSection.addEventListener('mouseenter', () => {
                    clearInterval(slideInterval);
                });
                heroSection.addEventListener('mouseleave', () => {
                    slideInterval = setInterval(nextSlide, 6000);
                });
            }
        }
    }

    /* =========================================================
       ABOUT V2 — Scroll Reveal Animation
       ========================================================= */
    const reveals = document.querySelectorAll('.about-v2__reveal');
    if (reveals.length > 0) {
        if (!('IntersectionObserver' in window)) {
            reveals.forEach(r => r.classList.add('is-visible'));
        } else {
            const observer = new IntersectionObserver((entries) => {
                entries.forEach((entry) => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('is-visible');
                        observer.unobserve(entry.target);
                    }
                });
            }, { threshold: 0.1, rootMargin: '0px 0px -8% 0px' });

            reveals.forEach((reveal) => observer.observe(reveal));
        }
    }

    /* =========================================================
       FOUNDER TAB SLIDER — Doctors/Team Slider
       ========================================================= */
    const tabs = document.querySelectorAll('.founder-tab');
    const cards = document.querySelectorAll('.founder-card');
    const founderSlider = document.querySelector('.founder-slider');
    
    if (tabs.length > 0 && cards.length > 0) {
        let currentIndex = 0;
        let autoTimer = null;
        const INTERVAL = 3000;

        function goTo(index) {
            tabs.forEach(function (t) { 
                t.classList.remove('active'); 
                t.setAttribute('aria-selected', 'false'); 
            });
            cards.forEach(function (c) { 
                c.classList.remove('active'); 
            });
            
            if (tabs[index]) {
                tabs[index].classList.add('active');
                tabs[index].setAttribute('aria-selected', 'true');
            }
            if (cards[index]) {
                cards[index].classList.add('active');
            }
            currentIndex = index;
        }

        function next() {
            goTo((currentIndex + 1) % cards.length);
        }

        function startAuto() {
            stopAuto();
            autoTimer = setInterval(next, INTERVAL);
        }

        function stopAuto() {
            if (autoTimer) { 
                clearInterval(autoTimer); 
                autoTimer = null; 
            }
        }

        tabs.forEach(function (tab) {
            tab.addEventListener('click', function () {
                const targetSlide = parseInt(this.dataset.slide || this.getAttribute('data-slide'), 10);
                goTo(targetSlide);
                startAuto();
            });
        });

        if (founderSlider) {
            founderSlider.addEventListener('mouseenter', stopAuto);
            founderSlider.addEventListener('mouseleave', startAuto);
        }

        startAuto();
    }

    /* =========================================================
       OUR EXPERTISE (SERVICE ARCH) CAROUSEL — Scroll controls
       ========================================================= */
    const track = document.getElementById('service-arch-track');
    const prevBtn = document.querySelector('.service-arch-btn-prev');
    const nextBtn = document.querySelector('.service-arch-btn-next');

    if (track && prevBtn && nextBtn) {
        const scrollByCard = (direction) => {
            const card = track.querySelector('.service-arch-card');
            if (!card) return;
            const gap = 18;
            const cardWidth = card.getBoundingClientRect().width + gap;
            track.scrollBy({ left: direction * cardWidth, behavior: 'smooth' });
        };

        prevBtn.addEventListener('click', () => scrollByCard(-1));
        nextBtn.addEventListener('click', () => scrollByCard(1));
    }

    /* =========================================================
       FELLOW DOCTORS TRAINING — Scroll Reveal Animation
       ========================================================= */
    const trainerReveals = document.querySelectorAll('.trainer-v2__reveal');
    if (trainerReveals.length > 0) {
        const isInViewport = (el) => {
            const rect = el.getBoundingClientRect();
            const vh = window.innerHeight || document.documentElement.clientHeight;
            return rect.top < vh * 0.85 && rect.bottom > 0;
        };

        // Reveal elements already in viewport on load
        trainerReveals.forEach((el) => {
            if (isInViewport(el)) {
                el.classList.add('is-visible');
            }
        });

        // Safety fallback: reveal all after 1.5s in case observer misses them
        setTimeout(() => {
            trainerReveals.forEach((el) => {
                if (!el.classList.contains('is-visible')) {
                    el.classList.add('is-visible');
                }
            });
        }, 1500);

        if (!('IntersectionObserver' in window)) {
            trainerReveals.forEach((el) => el.classList.add('is-visible'));
        } else {
            const observer = new IntersectionObserver((entries) => {
                entries.forEach((entry) => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('is-visible');
                        observer.unobserve(entry.target);
                    }
                });
            }, { threshold: 0.1, rootMargin: '0px 0px -4% 0px' });

            trainerReveals.forEach((el) => observer.observe(el));
        }
    }

    /* =========================================================
       TESTIMONIALS MODERN SECTION — Modal & Responsive Scaling
       ========================================================= */
    const reviewsData = [
        {
            name: "Priya Sharma",
            treatment: "Acne Scar Treatment",
            location: "Mumbai",
            quote: "My acne scars faded in 8 weeks — and the team actually listened to me. For the first time in years, I recognised the person in the mirror.",
            img: "https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=500&h=600&fit=crop&q=80"
        },
        {
            name: "Rohan Mehta",
            treatment: "Pigmentation Care",
            location: "Delhi",
            quote: "Even-tone I never thought possible. Three sessions in, my skin looked rested and more even. Truly professional expertise.",
            img: "https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?w=500&h=600&fit=crop&q=80"
        },
        {
            name: "Ananya Reddy",
            treatment: "Acne Journey",
            location: "Hyderabad",
            quote: "Felt heard for the first time. They mapped a 12-week plan around my wedding and didn't push a single product I didn't need.",
            img: "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=500&h=600&fit=crop&q=80"
        },
        {
            name: "Kavya Iyer",
            treatment: "Routine Builder",
            location: "Bengaluru",
            quote: "They built a plan around my life, not the other way around. The 4-step routine actually fits my 6am yoga schedule.",
            img: "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=500&h=600&fit=crop&q=80"
        },
        {
            name: "Dr. Amit Patel",
            treatment: "Anti-Aging Care",
            location: "Ahmedabad",
            quote: "As a medical professional, I was skeptical. But D'Zen's science-backed integrative approach blew me away. Superb results.",
            img: "https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?w=500&h=600&fit=crop&q=80"
        },
        {
            name: "Meera Jasmine",
            treatment: "HydraFacial Glow",
            location: "Chennai",
            quote: "The instant glow after the signature HydraFacial was unbelievable. Perfect for my shoot days. The sanctuary is so calming.",
            img: "https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=500&h=600&fit=crop&q=80"
        },
        {
            name: "Vikram Malhotra",
            treatment: "Hair Restoration",
            location: "Pune",
            quote: "Highly professional team. The hair thinning treatments have shown noticeable density results within 3 months. Life-changing.",
            img: "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=500&h=600&fit=crop&q=80"
        },
        {
            name: "Siddharth Roy",
            treatment: "Laser Grooming",
            location: "Kolkata",
            quote: "Virtually painless laser sessions. The technology they use is state-of-the-art. Highly recommend D'Zen to everyone.",
            img: "https://images.unsplash.com/photo-1580489944761-15a19d654956?w=500&h=600&fit=crop&q=80"
        },
        {
            name: "Neha Sen",
            treatment: "Skin Tightening",
            location: "Gurgaon",
            quote: "The sagging skin around my jawline is visibly firmer. No downtime, no pain. Just pure expertise from the doctors.",
            img: "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=500&h=600&fit=crop&q=80"
        },
        {
            name: "Aarav Kapoor",
            treatment: "Eczema Wellness",
            location: "Mumbai",
            quote: "Their wellness counseling combined with skin treatments healed my stress eczema. They treat the root cause, not just symptoms.",
            img: "https://images.unsplash.com/photo-1501196354995-cbb51c65aaea?w=500&h=600&fit=crop&q=80"
        },
        {
            name: "Ritu Verma",
            treatment: "Scar Revision",
            location: "Jaipur",
            quote: "After my accident scar, I lost all self-esteem. The laser scar revision sessions have smoothed it out so much it is barely visible.",
            img: "https://images.unsplash.com/photo-1531746020798-e6953c6e8e04?w=500&h=600&fit=crop&q=80"
        },
        {
            name: "Aditi Rao",
            treatment: "Brightening Peel",
            location: "Kochi",
            quote: "My hyperpigmentation is completely gone. My skin feels fresh, breathing, and renewed. Thank you D'Zen Derma!",
            img: "https://images.unsplash.com/photo-1492562080023-ab3db95bfbce?w=500&h=600&fit=crop&q=80"
        }
    ];

    const testimonialModal = document.getElementById('testimonial-modal');
    if (testimonialModal) {
        const modalImg = document.getElementById('modal-img');
        const modalQuote = document.getElementById('modal-quote');
        const modalAuthor = document.getElementById('modal-author');
        const modalTreatment = document.getElementById('modal-treatment');
        const modalLocation = document.getElementById('modal-location');

        const testimonialCards = document.querySelectorAll('.testimonial-card:not(.empty-card)');
        const btnClose = document.getElementById('modal-btn-close');
        const overlayClose = document.getElementById('modal-overlay-close');
        const btnOpenFirst = document.getElementById('open-first-testimonial-btn');
        const testimonialWrapper = document.querySelector('.testimonials-card-wall-wrapper');

        function openModal(index) {
            const data = reviewsData[index];
            if (!data) return;

            if (modalImg) {
                modalImg.src = data.img;
                modalImg.alt = data.name;
            }
            if (modalQuote) modalQuote.textContent = "“" + data.quote + "”";
            if (modalAuthor) modalAuthor.textContent = data.name;
            if (modalTreatment) modalTreatment.textContent = data.treatment;
            if (modalLocation) modalLocation.textContent = data.location;

            testimonialModal.classList.add('is-active');
            testimonialModal.setAttribute('aria-hidden', 'false');
            document.body.style.overflow = 'hidden';
        }

        function closeModal() {
            testimonialModal.classList.remove('is-active');
            testimonialModal.setAttribute('aria-hidden', 'true');
            document.body.style.overflow = '';
        }

        testimonialCards.forEach(card => {
            card.addEventListener('click', function () {
                const index = parseInt(this.getAttribute('data-index'), 10);
                openModal(index);
            });
        });

        if (btnClose) btnClose.addEventListener('click', closeModal);
        if (overlayClose) overlayClose.addEventListener('click', closeModal);

        if (btnOpenFirst) {
            btnOpenFirst.addEventListener('click', function (e) {
                e.preventDefault();
                openModal(0);
            });
        }

        document.addEventListener('keydown', function (e) {
            if (e.key === 'Escape' && testimonialModal.classList.contains('is-active')) {
                closeModal();
            }
        });

        function adjustScale() {
            if (testimonialWrapper) {
                const viewportWidth = window.innerWidth;
                const scale = viewportWidth < 1340 ? (viewportWidth / 1340) : 1;
                testimonialWrapper.style.setProperty('--testimonials-scale', scale);
            }
        }

        window.addEventListener('resize', adjustScale);
        adjustScale();
        window.addEventListener('load', adjustScale);
    }

    /* =========================================================
       SIGNATURE SERVICES — Scroll-linked Panel Reveal
       ========================================================= */
    const sigPanels = document.querySelectorAll('.sig-panel');
    if (sigPanels.length > 0) {
        let isMobile = window.matchMedia('(max-width: 900px)').matches;

        function revealSigPanels() {
            const vh = window.innerHeight;

            sigPanels.forEach(function (panel) {
                const rect = panel.getBoundingClientRect();
                const panelMid = rect.top + rect.height / 2;

                if (panelMid < vh * 0.88 && rect.bottom > 0) {
                    panel.classList.add('is-visible');
                } else if (!isMobile && rect.top > vh * 1.1) {
                    panel.classList.remove('is-visible');
                }
            });
        }

        revealSigPanels();

        let sigTicking = false;
        window.addEventListener('scroll', function () {
            if (!sigTicking) {
                requestAnimationFrame(function () {
                    revealSigPanels();
                    sigTicking = false;
                });
                sigTicking = true;
            }
        }, { passive: true });

        window.addEventListener('resize', function () {
            isMobile = window.matchMedia('(max-width: 900px)').matches;
            revealSigPanels();
        }, { passive: true });
    }

    /* =========================================================
       SIGNATURE SERVICES — Blob Hole Reveal (scroll-driven)
       A cream curtain over the section has a blob-shaped hole that
       grows from the centre as the section scrolls into view.
       ========================================================= */
    (function () {
        const zone = document.getElementById('sigServicesZone');
        const curtain = document.getElementById('sigReveal');
        if (!zone || !curtain) return;

        const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
        if (prefersReduced) { curtain.classList.add('is-done'); return; }

        // Reveal completes over this fraction of a viewport of scrolling
        // once the section top hits the top of the screen.
        const REVEAL_DISTANCE = 0.9; // × viewport height

        let ticking = false;

        function easeOutCubic(t) { return 1 - Math.pow(1 - t, 3); }

        function updateReveal() {
            const rect = zone.getBoundingClientRect();
            const vh = window.innerHeight;
            const distance = vh * REVEAL_DISTANCE;

            // How far the section top has scrolled past the top of the viewport.
            const scrolledPast = -rect.top;
            let progress = scrolledPast / distance;
            progress = Math.min(Math.max(progress, 0), 1);

            // Section not yet reached → keep curtain closed & mounted.
            if (rect.top > vh || rect.bottom < 0) {
                if (progress <= 0) {
                    curtain.classList.remove('is-done');
                    curtain.style.setProperty('--sig-reveal', '0');
                }
                return;
            }

            const eased = easeOutCubic(progress);
            curtain.style.setProperty('--sig-reveal', eased.toFixed(4));

            // Fully open → unmount so it never blocks anything.
            if (progress >= 1) {
                curtain.classList.add('is-done');
            } else {
                curtain.classList.remove('is-done');
            }
        }

        updateReveal();

        window.addEventListener('scroll', function () {
            if (!ticking) {
                requestAnimationFrame(function () {
                    updateReveal();
                    ticking = false;
                });
                ticking = true;
            }
        }, { passive: true });

        window.addEventListener('resize', updateReveal, { passive: true });
    })();

    /* =========================================================
       TESTIMONIALS — Tabs (Video / Google Reviews) + click-to-play
       ========================================================= */
    (function () {
        const tabs = document.querySelector('.tst-tabs');
        if (!tabs) return;

        const tabBtns = tabs.querySelectorAll('.tst-tab');
        const panelVideo = document.getElementById('tstPanelVideo');
        const panelReviews = document.getElementById('tstPanelReviews');

        function activate(name) {
            tabs.setAttribute('data-active', name);
            tabBtns.forEach(function (btn) {
                const isActive = btn.getAttribute('data-tab') === name;
                btn.classList.toggle('is-active', isActive);
                btn.setAttribute('aria-selected', isActive ? 'true' : 'false');
            });
            if (panelVideo && panelReviews) {
                const showVideo = name === 'video';
                panelVideo.classList.toggle('is-active', showVideo);
                panelReviews.classList.toggle('is-active', !showVideo);
                panelVideo.hidden = !showVideo;
                panelReviews.hidden = showVideo;
            }
        }

        tabBtns.forEach(function (btn) {
            btn.addEventListener('click', function () {
                activate(btn.getAttribute('data-tab'));
            });
        });

        // default state
        activate('video');

        // Click-to-play: swap poster for an autoplaying embed
        document.querySelectorAll('.tst-video-card').forEach(function (card) {
            card.addEventListener('click', function () {
                if (card.classList.contains('is-playing')) return;
                const src = card.getAttribute('data-video');
                if (!src) return;
                const iframe = document.createElement('iframe');
                const sep = src.indexOf('?') === -1 ? '?' : '&';
                iframe.src = src + sep + 'autoplay=1&rel=0&playsinline=1';
                iframe.setAttribute('allow',
                    'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture');
                iframe.setAttribute('allowfullscreen', '');
                iframe.setAttribute('title', 'Client testimonial video');
                card.appendChild(iframe);
                card.classList.add('is-playing');
            });
        });
    })();

    /* =========================================================
       FLOATING BOTTOM ACTION BAR — Scroll Controller
       ========================================================= */
    (function () {
        const bar = document.getElementById('bottomActionBar');
        if (!bar) return;

        const MOBILE_BREAKPOINT = 768;
        const HIDE_THRESHOLD = 200; // pixels scrolled before we even consider showing
        let isVisible = false;
        let lastScrollY = window.pageYOffset;
        let ticking = false;

        const isMobile = function () {
            return window.innerWidth < MOBILE_BREAKPOINT;
        };

        // On mobile, the bar is always visible
        function applyMobileState() {
            if (isMobile()) {
                bar.classList.add('is-visible');
                isVisible = true;
            }
        }
        applyMobileState();

        // Desktop: show when scrolling down, hide when scrolling up
        function update() {
            if (isMobile()) {
                ticking = false;
                return;
            }

            const currentY = window.pageYOffset;
            const delta = currentY - lastScrollY;

            // Hides itself when user is at the top of the page
            if (currentY <= HIDE_THRESHOLD) {
                if (isVisible) {
                    bar.classList.remove('is-visible');
                    isVisible = false;
                }
            }
            // Visible only when scrolling down (delta > 0) past threshold
            else if (delta > 2) {
                if (!isVisible) {
                    bar.classList.add('is-visible');
                    isVisible = true;
                }
            }
            // Hide when scrolling up
            else if (delta < -2) {
                if (isVisible) {
                    bar.classList.remove('is-visible');
                    isVisible = false;
                }
            }

            lastScrollY = currentY;
            ticking = false;
        }

        window.addEventListener('scroll', function () {
            if (!ticking) {
                requestAnimationFrame(update);
                ticking = true;
            }
        }, { passive: true });

        let resizeTimer;
        window.addEventListener('resize', function () {
            clearTimeout(resizeTimer);
            resizeTimer = setTimeout(applyMobileState, 120);
        });
    })();

    /* =========================================================
       GENERAL SCROLL REVEAL OBSERVER
       ========================================================= */
    const revealItems = document.querySelectorAll('.reveal');
    if (revealItems.length > 0) {
        if ('IntersectionObserver' in window) {
            const revealObserver = new IntersectionObserver(function(entries) {
                entries.forEach(function(entry) {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('visible');
                        revealObserver.unobserve(entry.target);
                    }
                });
            }, { threshold: 0.15, rootMargin: '0px 0px -50px 0px' });

            revealItems.forEach(function(el) {
                revealObserver.observe(el);
            });
        } else {
            revealItems.forEach(function(el) {
                el.classList.add('visible');
            });
        }
    }

    /* =========================================================
       PHILOSOPHY SECTION - STRIP TAB LOGIC
       ========================================================= */
    (function () {
        const tabBtns = document.querySelectorAll('.philosophy-tab-btn');
        const contentPanels = document.querySelectorAll('.philosophy-content-panel');
        
        if (tabBtns.length > 0 && contentPanels.length > 0) {
            tabBtns.forEach(btn => {
                btn.addEventListener('click', () => {
                    // Remove active from all buttons
                    tabBtns.forEach(b => b.classList.remove('is-active'));
                    // Add active to clicked
                    btn.classList.add('is-active');
                    
                    const index = btn.getAttribute('data-index');
                    
                    // Hide all panels
                    contentPanels.forEach(panel => {
                        panel.classList.remove('is-active');
                    });
                    
                    // Show target panel
                    const targetPanel = document.getElementById('phil-panel-' + index);
                    if (targetPanel) {
                        targetPanel.classList.add('is-active');
                    }
                });
            });
        }
    })();

    /* =========================================================
       SCRIBBLE UNDERLINE — draw-in on scroll
       ========================================================= */
    (function () {
        const scribbles = document.querySelectorAll('.scribble');
        if (!scribbles.length) return;

        // No observer support → leave underlines visible (CSS default), skip animation.
        if (!('IntersectionObserver' in window)) return;

        // Flag the page as animation-capable: this hides the strokes so they can draw in.
        document.documentElement.classList.add('scribble-anim');

        const observer = new IntersectionObserver((entries, obs) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('is-drawn');
                    obs.unobserve(entry.target);
                }
            });
        }, { threshold: 0.6, rootMargin: '0px 0px -8% 0px' });

        scribbles.forEach((el) => observer.observe(el));
    })();
})();
