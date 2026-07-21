import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Change header to sidebar
html = html.replace('<header class="header">', '<aside class="sidebar">')
html = html.replace('</header>', '</aside>')

# 2. Wrap main content and sidebar in app-container if not already wrapped
if '<div class="app-container">' not in html:
    html = html.replace('<aside class="sidebar">', '<div class="app-container">\n    <aside class="sidebar">')
    # find the closing tag of main to close app-container
    html = html.replace('</main>', '</main>\n</div>')
    
    # Change main class
    html = html.replace('<main id="main">', '<main id="main" class="dashboard-content">')

# 3. Move culture-section to the top of each unit's container
# The structure is: <div id="unit-X"...> <div class="container"> ... <section class="culture-section">...</section> </div> </div>
# We need to extract the culture-section and insert it right after <div class="container">

def move_culture_section_to_top():
    global html
    # Find all units
    unit_pattern = re.compile(r'(<div id="unit-\d+" class="course-unit".*?>\s*<div class="container">)(.*?)(    </div>\n</div>)', re.DOTALL)
    
    # Find culture section within a unit
    culture_pattern = re.compile(r'(\s*<!-- 🇺🇸 AMERICAN ENGLISH IN USE.*?</section>\n)', re.DOTALL)
    
    def replacer(match):
        unit_start = match.group(1)
        unit_content = match.group(2)
        unit_end = match.group(3)
        
        culture_match = culture_pattern.search(unit_content)
        if culture_match:
            culture_html = culture_match.group(1)
            # Remove culture_html from unit_content
            new_content = unit_content.replace(culture_html, "")
            # Prepend culture_html
            return unit_start + culture_html + new_content + unit_end
        else:
            return match.group(0)

    html = unit_pattern.sub(replacer, html)

move_culture_section_to_top()

# 4. Remove the dropdown-btn which is no longer needed
html = html.replace('<button class="dropdown-btn">', '<!-- <button class="dropdown-btn"> -->')
html = html.replace('📚 Units <span class="arrow">▼</span>', '<!-- 📚 Units <span class="arrow">▼</span> -->')
html = html.replace('</button>\n                    <div class="dropdown-content"', '<!-- </button> -->\n                    <div class="dropdown-content"')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Dashboard layout applied!")
