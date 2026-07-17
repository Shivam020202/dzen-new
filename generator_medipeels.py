import os

with open('treatments/face/hydrafacial.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace basic strings
html = html.replace('<title>HydraFacial Treatment Delhi & Gurgaon | D\'Zen Derma</title>', '<title>Medical Grade Peels Delhi & Gurgaon | D\'Zen Derma</title>')
html = html.replace('"name": "Medical HydraFacial"', '"name": "Clinical Medipeels"')
html = html.replace('<h1 class="hero-title">Medical HydraFacial</h1>', '<h1 class="hero-title">Clinical Medipeels</h1>')
html = html.replace('Beyond surface glow: a deeply purifying, nutrient-rich resurfacing protocol that restores cellular vitality without downtime.', 'Advanced chemical exfoliation tailored to your unique skin concerns, accelerating cellular turnover to reveal a brighter, smoother, and more even complexion.')
html = html.replace('What is a <em>Medical HydraFacial</em>?', 'What are <em>Clinical Medipeels</em>?')

p1 = 'The HydraFacial is a non-invasive, multi-step dermatological treatment that combines hydradermabrasion, chemical peels, and painless extractions with a specialized delivery of antioxidants, hyaluronic acid, and peptides.'
p1_new = 'Clinical Medipeels (chemical peels) are dermatological treatments that utilize carefully formulated acidic solutions to safely and predictably exfoliate the uppermost layers of the skin. By removing damaged epidermal cells, they stimulate the dermis to produce fresh collagen and elastin.'
html = html.replace(p1, p1_new)

p2 = "Unlike traditional salon facials that sit on the skin's surface, our medical-grade HydraFacial utilizes patented vortex technology to physically extract deeply embedded sebum and debris while simultaneously infusing the dermis with clinical-strength serums tailored to your specific skin biome. It bridges the gap between relaxation and measurable dermatological results."
p2_new = "Unlike superficial over-the-counter exfoliants, our medical-grade peels penetrate deeply to target the root causes of hyperpigmentation, active acne, and photoaging. Ranging from mild AHA/BHA blends (like Mandelic or Salicylic acid) to deeper TCA (Trichloroacetic acid) peels, the strength and depth are entirely customized to your skin's clinical requirements, bridging the gap between cosmetic glow and profound structural repair."
html = html.replace(p2, p2_new)

html = html.replace('HydraFacial is universally beneficial and structurally safe for all skin types.', 'Medipeels are highly versatile and can be formulated for all skin types, including sensitive and acne-prone skin, when supervised by a dermatologist.')

dzen_diff = "At D'Zen Derma, we do not believe in one-size-fits-all aesthetics. A HydraFacial in our clinic is a medically supervised protocol."
dzen_diff_new = "At D'Zen Derma, our peeling protocols are strictly supervised by our dermatologists. We do not use generic, pre-mixed solutions; every peel is compounded and timed precisely for your skin's unique tolerance and specific concerns."
html = html.replace(dzen_diff, dzen_diff_new)

dzen_diff_p2 = "We augment the standard 3-step process with customized clinical boosters (such as Britenol or Dermabuilder), targeted LED light therapy, and lymphatic drainage to reduce systemic inflammation. Furthermore, our dermatologists may pair this treatment with targeted IV nutritional therapy, ensuring your skin receives vital hydration and vitamins from the inside out simultaneously."
dzen_diff_p2_new = "We often combine our Medipeels with dermaplaning for deeper penetration, and follow up with restorative ceramide masks and cooling LED therapy to minimize erythema and accelerate healing. For patients dealing with severe pigmentation, we may integrate this with targeted internal supplements or IV Glutathione to address melanin production from the inside out."
html = html.replace(dzen_diff_p2, dzen_diff_p2_new)

with open('treatments/face/medipeels.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('medipeels.html generated successfully.')
