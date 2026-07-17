import os

with open('treatments/face/hydrafacial.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace basic strings
html = html.replace('<title>HydraFacial Treatment Delhi & Gurgaon | D\'Zen Derma</title>', '<title>Medical Oxy-Facial Treatment Delhi & Gurgaon | D\'Zen Derma</title>')
html = html.replace('"name": "Medical HydraFacial"', '"name": "Medical Oxy-Facial"')
html = html.replace('<h1 class="hero-title">Medical HydraFacial</h1>', '<h1 class="hero-title">Medical Oxy-Facial</h1>')
html = html.replace('Beyond surface glow: a deeply purifying, nutrient-rich resurfacing protocol that restores cellular vitality without downtime.', 'A highly pressurized stream of medical-grade oxygen combined with customized serums to instantly plump, hydrate, and revive fatigued skin.')
html = html.replace('What is a <em>Medical HydraFacial</em>?', 'What is a <em>Medical Oxy-Facial</em>?')

p1 = 'The HydraFacial is a non-invasive, multi-step dermatological treatment that combines hydradermabrasion, chemical peels, and painless extractions with a specialized delivery of antioxidants, hyaluronic acid, and peptides.'
p1_new = 'The Medical Oxy-Facial is an advanced transdermal infusion system. It utilizes continuous, hyperbaric oxygen pressure to deliver a potent cocktail of low-molecular-weight hyaluronic acid, essential vitamins, and targeted antioxidants directly into the dermis without any needles or trauma.'
html = html.replace(p1, p1_new)

p2 = "Unlike traditional salon facials that sit on the skin's surface, our medical-grade HydraFacial utilizes patented vortex technology to physically extract deeply embedded sebum and debris while simultaneously infusing the dermis with clinical-strength serums tailored to your specific skin biome. It bridges the gap between relaxation and measurable dermatological results."
p2_new = "Where topical serums fail to penetrate the skin barrier, the pressurized oxygen acts as a sophisticated delivery mechanism, forcing active ingredients past the stratum corneum. The oxygen itself has a profound antibacterial and cooling effect, instantly reducing erythema (redness) and stimulating cellular respiration. The result is a deeply quenched, volumized, and visibly lifted complexion—the ultimate red-carpet preparation."
html = html.replace(p2, p2_new)

html = html.replace('HydraFacial is universally beneficial and structurally safe for all skin types.', 'The Oxy-Facial is extremely gentle and highly recommended for almost all skin types, especially sensitive or reactive skin.')

dzen_diff = "At D'Zen Derma, we do not believe in one-size-fits-all aesthetics. A HydraFacial in our clinic is a medically supervised protocol."
dzen_diff_new = "At D'Zen Derma, our Medical Oxy-Facial is rigorously customized. We do not use generic ampoules; our dermatologists select specific serums (such as Vitamin C, Peptides, or Retinol) based on your immediate skin assessment."
html = html.replace(dzen_diff, dzen_diff_new)

dzen_diff_p2 = "We augment the standard 3-step process with customized clinical boosters (such as Britenol or Dermabuilder), targeted LED light therapy, and lymphatic drainage to reduce systemic inflammation. Furthermore, our dermatologists may pair this treatment with targeted IV nutritional therapy, ensuring your skin receives vital hydration and vitamins from the inside out simultaneously."
dzen_diff_p2_new = "We augment the infusion process with gentle enzymatic exfoliation beforehand to clear the canvas, and finish with specialized LED light therapy to seal the active ingredients and promote deep tissue healing. When paired with our signature IV Nutrition drips, this protocol becomes a powerful inside-out cellular regeneration treatment."
html = html.replace(dzen_diff_p2, dzen_diff_p2_new)

with open('treatments/face/oxy-facial.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('oxy-facial.html generated successfully.')
