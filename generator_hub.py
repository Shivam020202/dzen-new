import shutil

shutil.copy('treatments/face/index.html', 'treatments/index.html')

with open('treatments/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('Face Aesthetics & Treatments', 'All Clinical Treatments')
html = html.replace('<span style="display:inline-block; font-size:11px; font-weight:600; letter-spacing:0.3em; text-transform:uppercase; color:#e0a65a; margin-bottom:16px;">The Portfolio</span>', '<span style="display:inline-block; font-size:11px; font-weight:600; letter-spacing:0.3em; text-transform:uppercase; color:#e0a65a; margin-bottom:16px;">The Directory</span>')
html = html.replace('<h1 style="font-family:\'Belgiano Serif 2\', serif; font-size:clamp(40px, 4.5vw, 60px); color:#2B1A12; margin-bottom:24px;">Face Aesthetics</h1>', '<h1 style="font-family:\'Belgiano Serif 2\', serif; font-size:clamp(40px, 4.5vw, 60px); color:#2B1A12; margin-bottom:24px;">Clinical Treatments</h1>')
html = html.replace('Discover our curated collection of clinical facial treatments designed to restore, refine, and rejuvenate your skin from the cellular level upwards.', 'Explore our complete directory of medical-grade treatments for Face, Body, Hair, and Anti-Ageing, guided by our signature inside-out regenerative philosophy.')

# Change links to point to the face hub
html = html.replace('hydrafacial.html', 'face/hydrafacial.html')
html = html.replace('oxy-facial.html', 'face/oxy-facial.html')

with open('treatments/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Main treatments hub generated.")
