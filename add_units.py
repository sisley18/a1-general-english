import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# We need to replace the content of <div class="unit-grid"> inside <div id="unit-0">
# with 24 individual unit cards.

unit_grid_pattern = re.compile(r'(<div id="unit-0".*?<div class="unit-grid">)(.*?)(</div>\n\s*</section>)', re.DOTALL)

# Generate HTML for all 24 units
new_grid_html = "\n"
for i in range(1, 25):
    new_grid_html += f'                    <a href="#" class="unit-card" onclick="navigateUnitTo({i}); return false;">\n'
    new_grid_html += f'                        <h3>Unit {i}</h3>\n'
    new_grid_html += f'                        <p>American English Practice</p>\n'
    new_grid_html += f'                    </a>\n'

def replacer(match):
    return match.group(1) + new_grid_html + match.group(3)

content = unit_grid_pattern.sub(replacer, content)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)
print("Added 24 units to home page!")
