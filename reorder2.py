import sys

def get_section(content, start_tag):
    start_idx = content.find(start_tag)
    if start_idx == -1: return None, None
    
    end_idx = start_idx
    depth = 0
    while end_idx < len(content):
        next_open = content.find('<section', end_idx)
        next_close = content.find('</section>', end_idx)
        
        if next_close == -1: break
        
        if next_open != -1 and next_open < next_close:
            depth += 1
            end_idx = next_open + 8
        else:
            depth -= 1
            end_idx = next_close + 10
            if depth == 0:
                break
    
    return start_idx, end_idx

with open('v2/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

with open('footer.html', 'r', encoding='utf-8') as f:
    footer = f.read()

sections = [
    ('hero', '<div class="hero-wrapper"'),
    ('welcome', '<section class="about-v2"'),
    ('philosophy', '<section class="brand-philosophy-strip-section"'),
    ('team', '<section class="doctors-v2"'),
    ('expertise', '<section class="service-arch-section"'),
    ('signature', '<section class="sig-services-zone"'),
    ('training', '<section class="trainer-section"'),
    ('featured', '<section class="media-coverage"'),
    ('news', '<section class="headlines-section"'),
    ('testimonials', '<section class="testimonials-modern-section"')
]

blocks = {}
for name, tag in sections:
    if name == 'hero':
        start = html.find(tag)
        end = html.find('</div>', html.find('</section>', start)) + 6
    else:
        start, end = get_section(html, tag)
    
    if start is not None and end is not None:
        blocks[name] = html[start:end]
    else:
        print(f"Failed to find {name}")

# Now find the <main> block
main_start = html.find('<main>')
main_end_tag = html.find('</main>')

if main_start != -1 and main_end_tag != -1:
    main_start = main_start + 6
    
    # Expected order
    order = [
        'hero',
        'welcome',
        'philosophy',
        'team',
        'expertise',
        'signature',
        'training',
        'featured',
        'news',
        'testimonials'
    ]
    
    new_main_content = "\n\n        ".join(blocks[n] for n in order if n in blocks)
    new_html = html[:main_start] + "\n        " + new_main_content + "\n\n" + footer + "\n    " + html[main_end_tag:]
    
    with open('v2/index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Done reordering!")
else:
    print("Failed to find main tags")
