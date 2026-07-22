import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Clean up white inline text just to be safe
html = re.sub(r'color:\s*white;?', '', html, flags=re.IGNORECASE)
html = re.sub(r'color:\s*#ffffff;?', '', html, flags=re.IGNORECASE)
html = re.sub(r'color:\s*#fff;?', '', html, flags=re.IGNORECASE)
html = html.replace('style=""', '')

# 2. Extract <section class="culture-section">...</section> and move it to the top of <div class="container">
def move_culture_to_top(match):
    # match.group(1) is the <div class="container">...</div> part excluding the culture section
    # match.group(2) is the culture section
    unit_content = match.group(1)
    culture_sec = match.group(2)
    
    # We want to insert culture_sec right after <div class="container">
    # We find the first <div class="container"> inside unit_content
    container_idx = unit_content.find('<div class="container">')
    if container_idx != -1:
        insert_pos = container_idx + len('<div class="container">')
        new_content = unit_content[:insert_pos] + "\n\n" + culture_sec + "\n\n" + unit_content[insert_pos:]
        return new_content
    return match.group(0) # fallback

# Find the full course unit block, which ends with the culture section in our current html
# Our inject_content.py added it right before the last </div></div> of the unit.
# Wait, actually inject_content.py added it right before `    </div>\n</div>` which closes the container and the unit!
# Let's write a regex that finds the culture section and removes it, then inserts it at the top of the container.

# We will process unit by unit.
units = re.split(r'(<div id="unit-\d+" class="course-unit".*?>)', html)
new_html = units[0]

for i in range(1, len(units), 2):
    unit_header = units[i]
    unit_body = units[i+1]
    
    # Extract culture section
    culture_match = re.search(r'(<section class="culture-section".*?</section>)', unit_body, re.DOTALL)
    if culture_match:
        culture_sec = culture_match.group(1)
        # Remove from body
        unit_body = unit_body.replace(culture_sec, '')
        
        # Insert right after <div class="container">
        container_idx = unit_body.find('<div class="container">')
        if container_idx != -1:
            insert_pos = container_idx + len('<div class="container">')
            unit_body = unit_body[:insert_pos] + "\n" + culture_sec + "\n" + unit_body[insert_pos:]
            
    new_html += unit_header + unit_body

with open("index.html", "w", encoding="utf-8") as f:
    f.write(new_html)

print("Moved culture section to top of container and cleaned white text!")
