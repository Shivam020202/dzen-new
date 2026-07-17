import os

with open('treatments/face/hydrafacial.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace basic strings
html = html.replace('<title>HydraFacial Treatment Delhi & Gurgaon | D\'Zen Derma</title>', '<title>Laser Hair Reduction Face Delhi & Gurgaon | D\'Zen Derma</title>')
html = html.replace('"name": "Medical HydraFacial"', '"name": "Laser Hair Reduction (Face)"')
html = html.replace('<h1 class="hero-title">Medical HydraFacial</h1>', '<h1 class="hero-title">Laser Hair Reduction (Face)</h1>')
html = html.replace('Beyond surface glow: a deeply purifying, nutrient-rich resurfacing protocol that restores cellular vitality without downtime.', 'Precision laser technology for safe, permanent reduction of unwanted facial hair, ensuring smooth skin without the irritation of threading or waxing.')
html = html.replace('What is a <em>Medical HydraFacial</em>?', 'What is <em>Facial Laser Hair Reduction</em>?')

p1 = 'The HydraFacial is a non-invasive, multi-step dermatological treatment that combines hydradermabrasion, chemical peels, and painless extractions with a specialized delivery of antioxidants, hyaluronic acid, and peptides.'
p1_new = 'Facial Laser Hair Reduction (LHR) uses concentrated beams of light to target the melanin (pigment) within hair follicles. This light energy converts to heat, safely destroying the follicle to inhibit future hair growth without damaging the surrounding delicate facial skin.'
html = html.replace(p1, p1_new)

p2 = "Unlike traditional salon facials that sit on the skin's surface, our medical-grade HydraFacial utilizes patented vortex technology to physically extract deeply embedded sebum and debris while simultaneously infusing the dermis with clinical-strength serums tailored to your specific skin biome. It bridges the gap between relaxation and measurable dermatological results."
p2_new = "Unlike traditional hair removal methods like threading, plucking, or waxing, which cause micro-trauma, ingrown hairs, and hyperpigmentation, our medical-grade LHR offers a permanent, skin-safe solution. We utilize advanced multi-wavelength diode lasers (like Soprano Titanium) that are highly effective for Indian skin tones, providing a nearly painless experience through advanced contact cooling."
html = html.replace(p2, p2_new)

html = html.replace('HydraFacial is universally beneficial and structurally safe for all skin types.', 'Laser Hair Reduction is safe for all skin types, but requires a clinical assessment to ensure hormonal imbalances (like PCOS) are addressed for optimal long-term results.')

dzen_diff = "At D'Zen Derma, we do not believe in one-size-fits-all aesthetics. A HydraFacial in our clinic is a medically supervised protocol."
dzen_diff_new = "At D'Zen Derma, facial hair removal is never treated as a purely cosmetic procedure. Because facial hair is highly hormonally driven, our dermatologists conduct a thorough endocrinological assessment before beginning your laser sessions."
html = html.replace(dzen_diff, dzen_diff_new)

dzen_diff_p2 = "We augment the standard 3-step process with customized clinical boosters (such as Britenol or Dermabuilder), targeted LED light therapy, and lymphatic drainage to reduce systemic inflammation. Furthermore, our dermatologists may pair this treatment with targeted IV nutritional therapy, ensuring your skin receives vital hydration and vitamins from the inside out simultaneously."
dzen_diff_p2_new = "If underlying conditions like PCOS or insulin resistance are identified, we integrate your laser treatments with our Functional Medicine protocols. By addressing the root cause hormonally while treating the symptom physically with our advanced diode lasers, we ensure that your results are genuinely permanent and your skin remains flawless."
html = html.replace(dzen_diff_p2, dzen_diff_p2_new)

with open('treatments/face/laser-hair-reduction-face.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('laser-hair-reduction-face.html generated successfully.')
