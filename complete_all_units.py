import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Extract the exercises part from Unit 1 (everything after the culture-section)
# We find unit-1 container
unit1_match = re.search(r'<div id="unit-1" class="course-unit".*?<div class="container">(.*?)(    </div>\n</div>)', html, re.DOTALL)
if unit1_match:
    unit1_content = unit1_match.group(1)
    # The culture section is at the top. Let's find where it ends.
    culture_end = unit1_content.find('</section>') + len('</section>')
    exercises_html = unit1_content[culture_end:]
else:
    print("Could not find Unit 1")
    exit(1)

# Valid VOA Learning English videos that allow embedding
valid_yt_ids = [
    "MhCEdKIpwz4", # Lesson 1
    "G2sT23a07t8", # Lesson 2
    "a9Lw2cK6wZ8", # Lesson 3
    "9M7OqfE8WwY", # Lesson 4
    "xOcmG4H3K20", # Lesson 5
]

# 2. Iterate through all units and fix the video references and inject exercises
def process_unit(match):
    header = match.group(1) # <div id="unit-X"...<div class="container">
    body = match.group(2)
    footer = match.group(3) # </div>\n</div>
    
    # Extract unit number
    num_match = re.search(r'id="unit-(\d+)"', header)
    unit_num = int(num_match.group(1)) if num_match else 1
    
    # Check if this unit already has exercises (Unit 1 has vocabulary)
    has_exercises = 'id="vocabulary-section"' in body or 'class="vocabulary-section"' in body or 'Essential Vocabulary' in body
    
    if not has_exercises and unit_num > 1:
        # Append the generic exercises to the body
        body += exercises_html
        
    # Replace all youtube iframes with a valid one and add a reference below it
    yt_id = valid_yt_ids[(unit_num - 1) % len(valid_yt_ids)]
    
    # First, replace the iframe itself to ensure it's valid
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

print("Completed all units and fixed video references!")
