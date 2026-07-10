import re

html_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Complete A1 English Course</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header class="header">
        <div class="container">
            <a href="index.html" class="logo">🌍 A1 <span>English Course</span></a>
            <nav class="navigation">
                <a href="index.html" class="nav-link">Home</a>
                <div class="dropdown">
                    <button class="dropdown-btn" style="font-size:0.85rem">📄 Export <span class="arrow">▼</span></button>
                    <div class="dropdown-content">
                        <a href="#" onclick="copyClassContent()" class="dropdown-item">📋 Copy All</a>
                        <a href="#" onclick="exportCompleteClass()" class="dropdown-item">📄 Export to Word</a>
                        <a href="#" onclick="printSection('main')" class="dropdown-item">🖨️ Print</a>
                    </div>
                </div>
            </nav>
        </div>
    </header>
    <main id="main">
"""

footer = """
    </main>
    <script src="script.js"></script>
</body>
</html>
"""

units = [f"unit{i}.html" for i in range(1, 9)]
letters = "ABCDEFGHIJ"

combined_html = html_template

for i, unit_file in enumerate(units):
    unit_num = i + 1
    try:
        with open(unit_file, "r", encoding="utf-8") as f:
            content = f.read()
            
            hero_match = re.search(r'<section class="hero">.*?</section>', content, re.DOTALL)
            main_match = re.search(r'<main id="main">(.*?)</main>', content, re.DOTALL)
            
            if hero_match and main_match:
                combined_html += hero_match.group(0) + "\n"
                
                main_content = main_match.group(1)
                
                # Enumerate sections A1, B1, C1 etc.
                section_labels = re.finditer(r'<span class="section-label[^>]*">(.*?)</span>', main_content)
                
                new_main = main_content
                offset = 0
                for idx, match in enumerate(section_labels):
                    original_text = match.group(1)
                    clean_text = re.sub(r'^[^\w\s]+', '', original_text).strip()
                    if not clean_text: clean_text = original_text
                    
                    letter = letters[idx] if idx < len(letters) else "X"
                    numbering = f"{letter}{unit_num}. {clean_text}"
                    
                    full_match_text = match.group(0)
                    replacement = full_match_text.replace(original_text, numbering)
                    
                    start = match.start() + offset
                    end = match.end() + offset
                    
                    new_main = new_main[:start] + replacement + new_main[end:]
                    offset += len(replacement) - (end - start)
                
                combined_html += f'<div class="container unit-container" id="unit-{unit_num}">\n'
                combined_html += new_main
                combined_html += '</div>\n<hr style="margin: 4rem 0; border: none; border-top: 2px dashed #ddd;">\n'
    except Exception as e:
        print(f"Error processing {unit_file}: {e}")

combined_html += footer

with open("course.html", "w", encoding="utf-8") as f:
    f.write(combined_html)

print("course.html generated successfully.")
