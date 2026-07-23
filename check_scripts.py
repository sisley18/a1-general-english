import re, sys
sys.stdout.reconfigure(encoding='utf-8')

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

for u in range(5, 11):
    pattern = r'<div id="unit-' + str(u) + r'"[\s\S]*?(?=<div id="unit-' + str(u+1) + r'"|<!-- PROGRESS TEST|<footer|$)'
    m = re.search(pattern, html)
    if m:
        content = m.group(0)
        headings = re.findall(r'<h[23][^>]*>(.*?)</h[23]>', content)
        buttons = len(re.findall(r'onclick="speakText', content))
        exercises = len(re.findall(r'class="[^\"]*vocab-card[^\"]*"|class="[^\"]*exercise-[^\"]*"', content))
        print(f"=== UNIT {u} ===")
        print(f"Length: {len(content)} chars | Audio Buttons: {buttons}")
        print("Headings:", headings[:10])
        print("-" * 50)
    else:
        print(f"=== UNIT {u} NOT FOUND ===")
