# D'Zen Derma — Master Page Generation Prompt

> Paste into Claude Code from the repo root. Run STEP 0 first, alone, and wait for the token report before continuing.

---

## ROLE

You are the lead frontend engineer + SEO content architect for **D'Zen Derma**, a concept-driven Aesthetic Dermatology & Integrative Wellness brand (Delhi + Gurgaon). You are building a 145+ page Astro site. Brand line: _"Elevating You, Inside Out."_ Core idea: **Balance** — internal health ↔ external appearance, regeneration ↔ refinement, minimalism ↔ measurable results.

Tone of the brand: editorial luxury, not medical directory. Science-first, never salesy. Think Aesop / Kinfolk, not a clinic brochure.

---

## STEP 0 — EXTRACT THE DESIGN SYSTEM (DO THIS FIRST, ALONE)

**Do not write any page yet.**

1. Read `/v2/index.html` in full. Also read any CSS it links or inlines.
2. Extract and report back, as a table:
   - Every CSS custom property (`--*`): name, value, where used
   - Colour palette: exact hex values + semantic role (bg, surface, ink, muted, accent, gold, border, overlay)
   - Typography: font families, `@font-face` / import sources, the full type scale (size, weight, line-height, letter-spacing) for h1–h6, body, eyebrow/label, caption
   - Spacing scale, border-radius scale, shadow scale
   - Breakpoints
   - Reusable component patterns already present (buttons, cards, eyebrow labels, section headers, dividers, hero, header, secondary bar, footer)
   - Animation/transition conventions (easing curves, durations, scroll reveals)
3. Write the findings to `src/styles/tokens.css` as the single source of truth. Every later page consumes these variables.

**Hard rule: invent no colours, no fonts, no shadows.** If `/v2/index.html` doesn't define something you need, stop and ask. Do not approximate.

Then stop and show me the token report before proceeding.

---

## STEP 1 — ARCHITECTURE

Stack: **Astro** + hand-written **HTML5/CSS3** + **Sanity.io** headless CMS. Deploy: Vercel. Zero JS by default; islands only where genuinely needed (gallery filter, mobile nav, secondary bar).

Build the pages **data-driven, not hand-written**. One template per category, one content file per page, dynamic routes generate the rest.

```
src/
  content/
    treatments/     # one .md/.json per treatment  (54 files)
    concerns/       # one per concern              (52 files)
    functional/     # one per FM service           (10 files)
    wellness/       # one per programme            (6 files)
    regenerative/   # one per pillar               (3 files)
  layouts/
    BaseLayout.astro
    TreatmentLayout.astro
    ConcernLayout.astro
    FunctionalLayout.astro
    WellnessLayout.astro
    RegenerativeLayout.astro
  components/       # section-level, all token-driven
  pages/
    treatments/[category]/[slug].astro
    concerns/[area]/[slug].astro
    functional-medicine/[slug].astro
    wellness-programmes/[slug].astro
    regenerative-aesthetics/[slug].astro
  styles/tokens.css
```

Define a Zod content schema per collection so every entry is validated and no page ships with missing sections.

---

## STEP 2 — NAVIGATION (non-negotiable brand rule)

- Primary header = **6 editorial labels only**: Home · Who We Are · Explore Concerns · Treatments · D'Zen Experience · The Journal. Plus a gold `BOOK CONSULTATION` button.
- **Zero treatment names in the primary nav. No dropdowns. No mega-menus. Ever.**
- Secondary bar: single strip, ~36px tall, appears only when contextually relevant (on a category hover or when on a category page). Treatment names in fine, spaced serif, muted/ambient. Micro-tooltip or card preview on hover. Never a list, never a dropdown.
- Mobile: secondary bar collapses to a horizontally scrollable chip row — a contextual index, not a menu.
- Contexts to support: `treatments` (Face | Body | Ageing | Hair), `concerns` (By Area: Face · Body · Ageing · Hair · Wellness), `experience` (Signatures · Integrative Programmes · Pre-Bridal · Regenerative · For Men · Training).
- Footer: 4 columns — Quick Links · Treatments · Wellness · Contact (Delhi + Gurgaon) — plus brand block and legal row.

---

## STEP 3 — TEMPLATES

Every page in a category uses the **identical section order and identical components**. Only content differs. No bespoke one-off layouts. Consistency is the product.

### TEMPLATE A — Treatment (54 pages)

1. **Hero** — treatment name, one-line editorial positioning, eyebrow (category), primary + WhatsApp CTA, hero image slot
2. **What Is [Treatment]** — 150–200 words, plain-language definition
3. **How It Works** — mechanism of action, 3–4 step visual sequence
4. **Who Is It For** — ideal candidate profile + who it's _not_ for (builds trust)
5. **Concerns Addressed** — chip grid, each chip links to its `/concerns/...` page
6. **The D'Zen Protocol** — how D'Zen does it differently; ties treatment to internal health/balance philosophy
7. **Expected Results** — realistic timeline, sessions needed, longevity of results, downtime
8. **Before & After Gallery** — filterable slot
9. **FAQs** — 6–8 Q&A, written from real search intent (cost, pain, downtime, safety, session count, suitability)
10. **Related Treatments** — 3–4 cards
11. **Book Consultation** — form block
12. **WhatsApp CTA** — floating + inline

### TEMPLATE B — Concern (52 pages)

1. **Hero** — concern name + empathetic editorial line
2. **Understanding [Concern]** — what it actually is, 150–200 words
3. **Why It Happens** — causes, split into _external_ (environmental, topical) and _internal_ (hormonal, gut, nutritional, stress). **This split is the D'Zen differentiator — always include both.**
4. **Types / Grades / Stages** — where clinically applicable
5. **The D'Zen Diagnostic Approach** — how it's assessed, not just treated
6. **Recommended Treatments** — cards linking to `/treatments/...`
7. **The Inside-Out Layer** — the functional medicine / wellness angle; links to `/functional-medicine/...` or `/wellness-programmes/...`
8. **Expected Journey** — realistic timeline
9. **Before & After Gallery**
10. **FAQs** — 6–8
11. **Related Concerns** — 3–4 cards
12. **Book Consultation + WhatsApp CTA**

### TEMPLATE C — Functional Medicine (10 pages)

Hero → What Is It → The Science → What It Treats → The Protocol (session structure, duration, frequency) → Who It's For → Expected Outcomes → Safety & Contraindications → Related Aesthetic Treatments (the inside-out bridge) → FAQs → Book + WhatsApp

### TEMPLATE D — Wellness Programme (6 pages)

Hero → The Programme Philosophy → What's Included (modular breakdown) → The Timeline (week-by-week or phase-by-phase) → Diagnostics Involved → Who It's For → Expected Outcomes → Testimonials slot → Related Programmes → FAQs → Book + WhatsApp

### TEMPLATE E — Regenerative Aesthetics (3 pages)

Hero → What Is Regenerative [Skin/Hair/Ageing] → Why Regeneration ≠ Correction → The Modalities → The D'Zen Regenerative Protocol → Results Timeline → Who It's For → Before & After → FAQs → Book + WhatsApp

---

## STEP 4 — CONTENT RULES

Content is the deliverable. Thin pages fail the entire build.

- **Length:** treatment/concern pages 1,200–1,800 words. FM/wellness/regenerative 1,000–1,500 words. Never under 900.
- **Primary keyword:** in H1, title tag, meta description, first 100 words, one H2, and the URL. Natural density — no stuffing.
- **Secondary + long-tail:** work in naturally across H2s and body (e.g. "hydrafacial cost in delhi", "is microneedling painful", "how many sessions of laser toning").
- **Locality:** Delhi and Gurgaon woven into copy naturally on every page. Never keyword-stuffed. Phase 2 will add dedicated location pages — do not cannibalise them here.
- **Voice:** editorial, calm, confident, precise. Short paragraphs (2–4 lines). No hype, no "revolutionary", no "say goodbye to", no exclamation marks.
- **Every claim must be medically defensible.** Realistic result ranges, honest downtime, stated contraindications. Dr. Aarushi's credibility is the asset — protect it.
- **YMYL compliance (India medical advertising):** no guaranteed outcomes, no "permanent" claims unless true, no before/after promises in copy, no price guarantees, no cure language. Include a medical disclaimer partial on every treatment/concern/FM page.
- **Zero duplicate content.** 54 treatment pages must not be a find-and-replace of each other. Each page needs its own genuine mechanism explanation, its own FAQs, its own protocol angle. If two pages could swap intros without anyone noticing, rewrite both.
- **Internal linking:** minimum 5 contextual in-body links per page. Treatment ↔ Concern ↔ Functional Medicine must interlink in a genuine mesh — this is the topical authority engine.

**Meta per page:** title (≤60 chars, keyword-front-loaded), meta description (≤155 chars, benefit + CTA), OG title/description/image, canonical.

**Schema (JSON-LD) per page type:**

- Treatment → `MedicalProcedure` + `FAQPage` + `BreadcrumbList`
- Concern → `MedicalCondition` + `FAQPage` + `BreadcrumbList`
- FM/Wellness → `MedicalTherapy` + `FAQPage` + `BreadcrumbList`
- Site-wide → `MedicalClinic` + `LocalBusiness` ×2 (Delhi, Gurgaon) + `Physician` (Dr. Aarushi Passi Bhandari) + `Organization`

---

## STEP 5 — DESIGN RULES

- Every value from `tokens.css`. No hardcoded hex, px font-sizes, or magic numbers.
- Mobile-first. Test at 375 / 768 / 1024 / 1440 / 1920.
- Editorial rhythm: generous whitespace, asymmetric layouts where earned, wide-tracked uppercase eyebrow labels above each section, serif display headings, thin gold rules as dividers.
- Sections must **alternate surface tones** (light bg → deep bg → light) to create rhythm. Never 12 identical white blocks.
- Interaction: subtle only. Slow ease, small translate, opacity fades. Respect `prefers-reduced-motion`.
- Imagery: `<figure>` slots with 4:5 / 16:9 / 3:2 ratios, lazy loading, explicit width/height, meaningful alt text (alt is SEO + a11y, not decoration).
- Accessibility: semantic landmarks, single H1, logical heading order, AA contrast, visible focus rings, keyboard-navigable secondary bar and gallery.
- Performance budget: **Lighthouse 100 / 100 / 100 / 100** on every page. LCP < 1.5s. Zero CLS. If a component threatens this, redesign it.

---

## STEP 6 — EXECUTION ORDER

Work in batches. Show me output and wait for approval at each checkpoint.

1. `tokens.css` + `BaseLayout` + header + secondary bar + footer → **checkpoint**
2. All section components, built once, token-driven, reusable → **checkpoint**
3. `TreatmentLayout` + **2 full sample pages**: `/treatments/face/hydrafacial` and `/treatments/hair/hair-prp-gfc` → **checkpoint. I approve the pattern before you scale.**
4. Remaining 52 treatment pages, in batches of 10
5. `ConcernLayout` + 2 samples (`/concerns/face/acne-scars`, `/concerns/hair/hair-fall`) → **checkpoint** → then remaining 50 in batches of 10
6. Functional Medicine (10) → Wellness (6) → Regenerative (3)
7. 13 core brand pages
8. Journal + utility (`/privacy-policy`, `/terms`, `/disclaimer`, `/sitemap`, `/404`)
9. Sanity schemas mirroring every collection
10. Technical SEO: `sitemap.xml`, `robots.txt`, canonicals, GA4 + Search Console hooks

---

## PAGE MANIFEST

### Core Brand — 13

`/` · `/our-philosophy` · `/about-clinic` · `/dr-aarushi-passi-bhandari` · `/rahul-bhandari` · `/dzen-signatures` · `/pre-bridal` · `/results` · `/workshops-training` · `/men` · `/media` · `/journal` · `/contact`

### Treatments — 54

Hubs: `/treatments` · `/treatments/face` · `/treatments/body` · `/treatments/anti-ageing` · `/treatments/hair`

**Face (23)** `/treatments/face/` → hydrafacial · oxy-facial · medipeels · laser-hair-reduction-face · mesotherapy · microneedling · dermablading · mesolipolysis-face · hifu-rf · mnrf · jawline-enhancement · non-invasive-face-lift · laser-resurfacing · laser-toning · photofacial · carbon-laser · derma-pen · endo-laser-face · radiocautery-face · hyperhidrosis-face · aquagold · double-chin-reduction · cheek-buckle-fat-removal

**Body (14)** `/treatments/body/` → medipeels-body · miradry · laser-hair-reduction · non-invasive-body-lifting · mesolipolysis · botox-under-arms · laser-tattoo-removal · nail-fungus-laser · endo-laser-body · radiocautery · hyperhidrosis · bra-bulge-treatment · earlobe-repair · stubborn-fat-reduction

**Anti-Ageing (8)** `/treatments/anti-ageing/` → dermal-fillers · botox · thread-lift · collagen-boosters · hand-rejuvenation · pico-toning · skin-boosters · aquagold-ageing

**Hair (4)** `/treatments/hair/` → hair-prp-gfc · exosome-therapy · follicle-renewal · hair-microneedling

### Concerns — 52

Hubs: `/concerns` · `/concerns/face` · `/concerns/body` · `/concerns/ageing` · `/concerns/hair` · `/concerns/wellness`

**Face (20)** `/concerns/face/` → acne · acne-scars · pigmentation · melasma · open-pores · dull-skin · dark-circles · under-eye-hollows · double-chin · undefined-jawline · fine-lines · sagging-skin · rosacea · uneven-skin-tone · blackheads · oily-skin · dry-skin · unwanted-facial-hair · sun-damage · moles-warts-skin-tags

**Body (12)** `/concerns/body/` → unwanted-body-hair · unwanted-tattoo · excessive-sweating · stubborn-fat · cellulite · stretch-marks · body-pigmentation · back-acne · nail-fungus · bra-bulge · torn-earlobes · loose-skin

**Ageing (8)** `/concerns/ageing/` → wrinkles · volume-loss · skin-laxity · ageing-hands · neck-ageing · thin-lips · tear-trough-hollows · collagen-loss

**Hair (6)** `/concerns/hair/` → hair-fall · hair-thinning · male-pattern-baldness · female-pattern-hair-loss · dandruff-scalp-health · postpartum-hair-loss

**Wellness (6)** `/concerns/wellness/` → hormonal-imbalance · gut-health · chronic-fatigue · weight-gain · menopause · low-immunity

### Functional Medicine — 10

`/functional-medicine/` → bhrt · iv-nutrition · ozone-therapy · fir-sauna · coffee-enema · gut-healing · kansa-therapy · diagnostics · lymphatic-detox · pemf

### Wellness Programmes — 6

`/wellness-programmes/` → full-body-detox · gut-restoration · longevity · intimate-wellness · fat-loss · beauty-inside-out

### Regenerative Aesthetics — 3

`/regenerative-aesthetics/` → skin · hair · ageing

### Journal & Utility — 6+

`/journal/skin-aesthetics` · `/journal/functional-wellness` · `/journal/longevity-beauty-inside-out` · `/journal/dzen-conversations` · `/journal/[slug]` (5 seed articles) · `/privacy-policy` · `/terms` · `/disclaimer` · `/sitemap` · `/404`

**Total: 145+**

---

## DO NOT

- Do not invent design tokens. `/v2/index.html` is law.
- Do not put treatment names in the primary nav.
- Do not use React, Tailwind, WordPress, or any UI framework.
- Do not use lorem ipsum or `TODO` placeholders. Real content or ask me.
- Do not ship a page under 900 words.
- Do not spin the same content across pages with words swapped.
- Do not make medical claims that can't be defended.
- Do not deviate from a template once I've approved it.
- Do not build Phase 2 location pages yet.

---

## QA GATE — every batch must pass before you move on

- [ ] All tokens from `tokens.css`, zero hardcoded values
- [ ] Section order matches the approved template exactly
- [ ] Word count in range; content genuinely unique vs sibling pages
- [ ] Title ≤60, meta ≤155, canonical set
- [ ] JSON-LD present and valid
- [ ] ≥5 contextual internal links
- [ ] Single H1, logical heading order, AA contrast
- [ ] Responsive at all 5 breakpoints
- [ ] Lighthouse 100 across the board
- [ ] Medical disclaimer present where required

**Start with STEP 0. Report the tokens. Do not Wait for my approval.**

1. CORE BRAND — 13
   #PageSlug1Home/2Our Philosophy/our-philosophy3About The Clinic/about-clinic4Dr. Aarushi Passi Bhandari/dr-aarushi-passi-bhandari5Rahul Bhandari/rahul-bhandari6D'Zen Signatures/dzen-signatures7Pre-Bridal Programme/pre-bridal8Results Gallery/results9Workshops & Training/workshops-training10Men's Aesthetics/men11Media Coverage/media12The Journal/journal13Contact / Locations/contact

2. TREATMENTS — 54
   Hubs (5)

/treatments
/treatments/face
/treatments/body
/treatments/anti-ageing
/treatments/hair

Face — 23 (/treatments/face/…)
hydrafacial · oxy-facial · medipeels · laser-hair-reduction-face · mesotherapy · microneedling · dermablading · mesolipolysis-face · hifu-rf · mnrf · jawline-enhancement · non-invasive-face-lift · laser-resurfacing · laser-toning · photofacial · carbon-laser · derma-pen · endo-laser-face · radiocautery-face · hyperhidrosis-face · aquagold · double-chin-reduction · cheek-buckle-fat-removal
Body — 14 (/treatments/body/…)
medipeels-body · miradry · laser-hair-reduction · non-invasive-body-lifting · mesolipolysis · botox-under-arms · laser-tattoo-removal · nail-fungus-laser · endo-laser-body · radiocautery · hyperhidrosis · bra-bulge-treatment · earlobe-repair · stubborn-fat-reduction
Anti-Ageing — 8 (/treatments/anti-ageing/…)
dermal-fillers · botox · thread-lift · collagen-boosters · hand-rejuvenation · pico-toning · skin-boosters · aquagold-ageing
Hair — 4 (/treatments/hair/…)
hair-prp-gfc · exosome-therapy · follicle-renewal · hair-microneedling

3. CONCERNS — 52
   (PDF gives no slugs → proposed)
   Hub + area hubs
   /concerns · /concerns/face · /concerns/body · /concerns/ageing · /concerns/hair · /concerns/wellness
   Face — 20 (/concerns/face/…)
   acne · acne-scars · pigmentation · melasma · open-pores · dull-skin · dark-circles · under-eye-hollows · double-chin · undefined-jawline · fine-lines · sagging-skin · rosacea · uneven-skin-tone · blackheads · oily-skin · dry-skin · unwanted-facial-hair · sun-damage · moles-warts-skin-tags
   Body — 12 (/concerns/body/…)
   unwanted-body-hair · unwanted-tattoo · excessive-sweating · stubborn-fat · cellulite · stretch-marks · body-pigmentation · back-acne · nail-fungus · bra-bulge · torn-earlobes · loose-skin
   Ageing — 8 (/concerns/ageing/…)
   wrinkles · volume-loss · skin-laxity · ageing-hands · neck-ageing · thin-lips · tear-trough-hollows · collagen-loss
   Hair — 6 (/concerns/hair/…)
   hair-fall · hair-thinning · male-pattern-baldness · female-pattern-hair-loss · dandruff-scalp-health · postpartum-hair-loss
   Wellness — 6 (/concerns/wellness/…)
   hormonal-imbalance · gut-health · chronic-fatigue · weight-gain · menopause · low-immunity

4. FUNCTIONAL MEDICINE — 10
   /functional-medicine/ + bhrt · iv-nutrition · ozone-therapy · fir-sauna · coffee-enema · gut-healing · kansa-therapy · diagnostics · lymphatic-detox · pemf
   Hub: /functional-medicine
5. WELLNESS PROGRAMMES — 6
   /wellness-programmes/ + full-body-detox · gut-restoration · longevity · intimate-wellness · fat-loss · beauty-inside-out
   Hub: /wellness-programmes
6. REGENERATIVE AESTHETICS — 3
   /regenerative-aesthetics/ + skin · hair · ageing
   Hub: /regenerative-aesthetics
