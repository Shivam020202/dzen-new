import os
import json
import re

def create_treatment_page(data):
    with open('treatments/face/hydrafacial.html', 'r', encoding='utf-8') as f:
        template = f.read()

    # Replacements
    template = re.sub(r'<title>.*?</title>', f'<title>{data["title_tag"]}</title>', template)
    template = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{data["meta_desc"]}">', template)
    template = re.sub(r'"name": ".*?"', f'"name": "{data["schema_name"]}"', template, count=1)
    
    # Hero
    template = re.sub(r'<img src="https://images.unsplash.com[^"]+" alt="Medical HydraFacial">', f'<img src="{data["hero_img"]}" alt="{data["h1"]}">', template)
    template = re.sub(r'<span style="display:inline-block; font-size:11px.*?</span>', f'<span style="display:inline-block; font-size:11px; font-weight:600; letter-spacing:0.3em; text-transform:uppercase; color:#e0a65a; margin-bottom:16px;">{data["category_eyebrow"]}</span>', template)
    template = re.sub(r'<h1 class="hero-title">.*?</h1>', f'<h1 class="hero-title">{data["h1"]}</h1>', template)
    template = re.sub(r'<p style="font-size:1.25rem; font-weight:300.*?</p>', f'<p style="font-size:1.25rem; font-weight:300; line-height:1.6; margin-bottom:32px; color:#fff;">{data["hero_sub"]}</p>', template)
    
    # Section 1: What is it
    # We will just replace everything between <div class="about-v2__intro-block text-center" style="max-width: 900px; margin: 0 auto;"> and the next </div></div></section>
    
    start_what = template.find('<div class="about-v2__intro-block text-center"')
    end_what = template.find('</section>', start_what)
    
    what_html = f'''<div class="about-v2__intro-block text-center" style="max-width: 900px; margin: 0 auto;">
                    <span class="about-v2__eyebrow">The Fundamentals</span>
                    <h2 class="about-v2__title">What is <em>{data["h1"]}</em>?</h2>
                    <p class="about-v2__lead" style="margin-top:24px;">
                        {data["what_is_p1"]}
                    </p>
                    <p class="about-v2__lead about-v2__lead--light">
                        {data["what_is_p2"]}
                    </p>
                    <p class="about-v2__lead about-v2__lead--light">
                        {data["what_is_p3"]}
                    </p>
                </div>
            </div>'''
            
    template = template[:start_what] + what_html + template[end_what:]
    
    out_path = f'treatments/{data["folder"]}/{data["slug"]}.html'
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(template)
    print(f"Created {out_path}")

