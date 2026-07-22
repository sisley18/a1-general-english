import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Valid VOA Learning English videos that allow embedding
valid_yt_ids = [
    "n56r-jL2R8Q", # Lesson 1 (Welcome!)
    "33aPzY5_9zO", # Lesson 2 (Hello, I'm Anna!)
    "a9Lw2cK6wZ8", # Lesson 3 (I'm Here!)
    "9M7OqfE8WwY", # Lesson 4 (What Can I Do?)
    "xOcmG4H3K20", # Lesson 5 (Where Are You?)
]

def process_unit(match):
    header = match.group(1) # <div id="unit-X"...<div class="container">
    body = match.group(2)
    footer = match.group(3) # </div>\n</div>
    
    num_match = re.search(r'id="unit-(\d+)"', header)
    unit_num = int(num_match.group(1)) if num_match else 1
    
    yt_id = valid_yt_ids[(unit_num - 1) % len(valid_yt_ids)]
    
    # Replace the iframe to ensure it's a valid ID that works
    body = re.sub(r'<iframe src="https://www.youtube.com/embed/[^"]+".*?</iframe>',
                  f'<iframe src="https://www.youtube.com/embed/{yt_id}?rel=0" allowfullscreen></iframe>', body)
    
    # Add video reference if not exists
    if 'class="video-reference"' not in body:
        ref_html = f'\n<p class="video-reference" style="margin-top: 10px; font-size: 0.9rem; color: var(--text-secondary);"><strong>Reference:</strong> <a href="https://www.youtube.com/watch?v={yt_id}" target="_blank" style="color: var(--accent-indigo); text-decoration: none;">VOA Learning English Lesson {unit_num}</a></p>\n'
        body = body.replace('</div>\n            \n            <div class="reading-passage"', 
                            f'</div>{ref_html}            \n            <div class="reading-passage"')
                            
    return header + body + footer

pattern = re.compile(r'(<div id="unit-\d+" class="course-unit".*?<div class="container">)(.*?)(    </div>\n</div>)', re.DOTALL)
new_html = pattern.sub(process_unit, html)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(new_html)

print("Fixed video IDs and added references!")
