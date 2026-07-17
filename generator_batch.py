import json

def generate(pages):
    with open('treatments/face/hydrafacial.html', 'r', encoding='utf-8') as f:
        base = f.read()

    for p in pages:
        html = base
        
        # Meta and hero
        html = html.replace('<title>HydraFacial Treatment Delhi & Gurgaon | D\'Zen Derma</title>', f'<title>{p["title"]} Delhi & Gurgaon | D\'Zen Derma</title>')
        html = html.replace('"name": "Medical HydraFacial"', f'"name": "{p["name"]}"')
        html = html.replace('<h1 class="hero-title">Medical HydraFacial</h1>', f'<h1 class="hero-title">{p["name"]}</h1>')
        
        html = html.replace('Beyond surface glow: a deeply purifying, nutrient-rich resurfacing protocol that restores cellular vitality without downtime.', p['hero_desc'])
        
        # What is it
        html = html.replace('What is a <em>Medical HydraFacial</em>?', f'What is <em>{p["name"]}</em>?')
        
        p1 = 'The HydraFacial is a non-invasive, multi-step dermatological treatment that combines hydradermabrasion, chemical peels, and painless extractions with a specialized delivery of antioxidants, hyaluronic acid, and peptides.'
        html = html.replace(p1, p['p1'])
        
        p2 = "Unlike traditional salon facials that sit on the skin's surface, our medical-grade HydraFacial utilizes patented vortex technology to physically extract deeply embedded sebum and debris while simultaneously infusing the dermis with clinical-strength serums tailored to your specific skin biome. It bridges the gap between relaxation and measurable dermatological results."
        html = html.replace(p2, p['p2'])
        
        html = html.replace('HydraFacial is universally beneficial and structurally safe for all skin types.', p['suitability'])
        
        dzen_diff = "At D'Zen Derma, we do not believe in one-size-fits-all aesthetics. A HydraFacial in our clinic is a medically supervised protocol."
        html = html.replace(dzen_diff, p['dzen1'])
        
        dzen_diff_p2 = "We augment the standard 3-step process with customized clinical boosters (such as Britenol or Dermabuilder), targeted LED light therapy, and lymphatic drainage to reduce systemic inflammation. Furthermore, our dermatologists may pair this treatment with targeted IV nutritional therapy, ensuring your skin receives vital hydration and vitamins from the inside out simultaneously."
        html = html.replace(dzen_diff_p2, p['dzen2'])
        
        with open(f'treatments/face/{p["slug"]}.html', 'w', encoding='utf-8') as f:
            f.write(html)
        print(f'{p["slug"]}.html generated successfully.')

pages = [
    {
        "slug": "mesotherapy",
        "title": "Facial Mesotherapy",
        "name": "Facial Mesotherapy",
        "hero_desc": "Micro-injections of potent vitamins, enzymes, and plant extracts to rejuvenate, tighten, and profoundly hydrate the skin from within.",
        "p1": "Mesotherapy is a minimally invasive dermatological procedure that involves delivering a customized cocktail of highly active ingredients directly into the mesoderm (middle layer of the skin).",
        "p2": "Unlike topical creams that struggle to penetrate the epidermis, these micro-injections bypass the skin barrier to deliver hyaluronic acid, amino acids, and antioxidants exactly where cellular repair occurs, stimulating intense collagen synthesis and cellular turnover.",
        "suitability": "Mesotherapy is ideal for patients seeking deep hydration, reduction in fine lines, and an overall luminous complexion.",
        "dzen1": "At D'Zen Derma, we take a highly analytical approach to Mesotherapy. We do not use standard ampoules; we compound the infusions based on your specific nutritional skin deficiencies.",
        "dzen2": "We combine our targeted micro-injections with a holistic assessment of your internal health, often recommending oral supplements or dietary shifts to support the newly stimulated cellular matrix from the inside out."
    },
    {
        "slug": "microneedling",
        "title": "Medical Microneedling",
        "name": "Medical Microneedling",
        "hero_desc": "Advanced collagen induction therapy that utilizes the body's natural healing cascade to repair acne scars, smooth texture, and restore firmness.",
        "p1": "Medical Microneedling (Collagen Induction Therapy) uses automated, sterile micro-needles to create thousands of controlled micro-injuries in the dermal layer of the skin.",
        "p2": "This clinically proven process triggers an immediate immune response, signaling the body to produce high quantities of new collagen and elastin as it heals the micro-channels. It is the gold standard for remodeling textural irregularities, atrophic acne scars, and enlarged pores.",
        "suitability": "Microneedling is highly effective for patients with acne scarring, textural issues, and mild to moderate skin laxity.",
        "dzen1": "At D'Zen Derma, we utilize the highest-grade FDA-approved devices to ensure perfectly vertical, tear-free channels.",
        "dzen2": "To maximize your regenerative potential, we infuse these micro-channels with advanced growth factors, exosomes, or platelet-rich plasma (PRP) drawn in-clinic, turning a simple physical treatment into a profound biological cellular regeneration protocol."
    },
    {
        "slug": "dermablading",
        "title": "Clinical Dermablading",
        "name": "Clinical Dermablading",
        "hero_desc": "A precise, surgical exfoliation technique that removes vellus hair and the outermost layer of dead skin cells for an instantly flawless, glass-like finish.",
        "p1": "Clinical Dermablading (or Dermaplaning) utilizes a sterile surgical scalpel held at a precise 45-degree angle to manually abrade the stratum corneum.",
        "p2": "This physical exfoliation not only removes weeks of accumulated dead skin cells but also eliminates vellus hair (peach fuzz) that traps dirt and oils. The immediate result is an ultra-smooth surface that allows for up to 80% deeper penetration of skincare products and flawless makeup application.",
        "suitability": "Dermablading is an excellent choice for almost all skin types, especially those with dry skin, superficial hyperpigmentation, or mild acne scarring.",
        "dzen1": "At D'Zen Derma, Dermablading is performed strictly by trained clinical professionals in a medically sterile environment to ensure zero risk of micro-tears.",
        "dzen2": "We never perform Dermablading in isolation. We always follow the physical exfoliation with a customized infusion of soothing ceramides and intensely hydrating hyaluronic acid masks, sealed in with cooling LED therapy to ensure an absolutely radiant, irritation-free result."
    },
    {
        "slug": "mesolipolysis-face",
        "title": "Facial Mesolipolysis",
        "name": "Facial Mesolipolysis",
        "hero_desc": "Targeted, non-surgical fat dissolving injections designed to contour the jawline and eliminate submental fat (double chin).",
        "p1": "Facial Mesolipolysis involves the precise injection of fat-dissolving compounds, such as deoxycholic acid or phosphatidylcholine, directly into localized subcutaneous fat deposits.",
        "p2": "These active enzymes work by safely breaking down the membrane of adipocytes (fat cells). Once the cell is destroyed, it releases its lipid contents, which are then naturally metabolized and permanently eliminated by the body's lymphatic system over the course of several weeks.",
        "suitability": "Mesolipolysis is the ideal clinical solution for patients with stubborn localized fat pockets, particularly around the jawline, jowls, or submental region, who wish to avoid surgical liposuction.",
        "dzen1": "At D'Zen Derma, contouring the face requires an architectural understanding of facial anatomy. We map the exact fat compartments before injection.",
        "dzen2": "Because fat elimination is heavily reliant on the lymphatic system, we incorporate lymphatic drainage techniques post-treatment and advise on internal anti-inflammatory practices to speed up the metabolic clearance of the dissolved fat cells for faster, smoother contouring."
    },
    {
        "slug": "hifu-rf",
        "title": "HIFU & RF Skin Tightening",
        "name": "HIFU & RF Contouring",
        "hero_desc": "Non-surgical, ultrasound-driven lifting and radiofrequency tightening to restore structural firmness and redefine facial contours.",
        "p1": "High-Intensity Focused Ultrasound (HIFU) and Radiofrequency (RF) are the premier non-invasive technologies for deep tissue lifting and dermal tightening.",
        "p2": "HIFU delivers concentrated ultrasound energy deep into the SMAS layer (the fibrous tissue targeted during a surgical facelift) to induce precise thermal coagulation points, while RF uniformly heats the dermal matrix to instantly contract existing collagen fibers and stimulate neocollagenesis. Together, they provide both deep lifting and surface firming.",
        "suitability": "This dual-modality treatment is perfect for patients experiencing mild to moderate skin laxity, jowling, and loss of jawline definition.",
        "dzen1": "At D'Zen Derma, we do not believe in isolated energy delivery. We customize the exact depths and energy protocols of HIFU and RF based on ultrasound mapping of your skin's thickness.",
        "dzen2": "We support this powerful structural remodeling with our Regenerative pillars, often recommending specific amino acid supplements and collagen-boosting IV therapies to give your body the exact biological building blocks it needs to construct the new collagen triggered by the devices."
    },
    {
        "slug": "mnrf",
        "title": "MNRF (Microneedling Radiofrequency)",
        "name": "MNRF Therapy",
        "hero_desc": "The ultimate synergy of physical micro-trauma and deep thermal energy for unparalleled skin remodeling, scar revision, and pore refinement.",
        "p1": "Microneedling Radiofrequency (MNRF) combines the mechanical stimulation of traditional microneedling with the deep thermal tissue heating of radiofrequency energy.",
        "p2": "Sterile, gold-plated needles penetrate the skin to a precisely controlled depth before releasing a burst of RF energy directly into the dermis. This bypasses the epidermis (protecting the surface from heat damage) and forces the deeper layers to aggressively produce new, highly structured collagen and elastin bundles.",
        "suitability": "MNRF is the gold standard for patients with severe atrophic acne scars, deeply enlarged pores, stretch marks, and stubborn skin laxity.",
        "dzen1": "At D'Zen Derma, our MNRF protocols are intensely customized. We adjust the needle depth and RF pulse duration dynamically across different zones of your face in a single session.",
        "dzen2": "Because MNRF demands significant cellular energy to heal and remodel, we heavily incorporate our Integrative Wellness philosophy, pairing the treatment with post-procedure exosome infusions and systemic antioxidant therapy to ensure the healing response is fast, robust, and highly effective."
    },
    {
        "slug": "jawline-enhancement",
        "title": "Jawline Enhancement",
        "name": "Jawline Enhancement",
        "hero_desc": "Architectural facial sculpting using high-density dermal fillers to create a sharp, defined, and harmoniously balanced lower face.",
        "p1": "Jawline Enhancement is an advanced aesthetic procedure that involves the strategic placement of structural hyaluronic acid fillers along the mandible and chin.",
        "p2": "By adding volume and structural support precisely where bone resorption or natural anatomy is lacking, the fillers act as biological scaffolding. This creates a sharp demarcation between the jaw and the neck, restores facial proportions, and visually tightens the lower facial skin.",
        "suitability": "Ideal for patients seeking to correct a weak chin, reduce the appearance of jowls, or achieve a more chiseled, editorial jawline profile.",
        "dzen1": "At D'Zen Derma, we view the face as an interconnected structure. We never fill a jawline in isolation without first analyzing the chin projection, the mid-face support, and your unique anatomical profile.",
        "dzen2": "Our enhancement protocol goes beyond just volume. We often combine structural fillers with targeted botulinum toxin in the masseters or platysmal bands to relax downward-pulling muscles, creating an elegantly lifted and balanced lower face that honors your natural proportions."
    }
]

generate(pages)
