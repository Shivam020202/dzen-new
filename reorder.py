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

sig_start, sig_end = get_section(html, '<section class="sig-services-zone"')
test_start, test_end = get_section(html, '<section class="testimonials-modern-section"')

sig_block = html[sig_start:sig_end]
test_block = html[test_start:test_end]

# Remove both from html
html_no_blocks = html.replace(sig_block, '').replace(test_block, '')

# Find insertion points
srv_start, srv_end = get_section(html_no_blocks, '<section class="service-arch-section"')
main_end_idx = html_no_blocks.find('</main>')

# Insert sig_block
html_inserted = html_no_blocks[:srv_end] + '\n\n' + sig_block + '\n\n' + html_no_blocks[srv_end:]

# Insert test_block
main_end_idx = html_inserted.find('</main>')
html_final = html_inserted[:main_end_idx] + test_block + '\n\n' + html_inserted[main_end_idx:]

with open('v2/index.html', 'w', encoding='utf-8') as f:
    f.write(html_final)
print("Done!")
