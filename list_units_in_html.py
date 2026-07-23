import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

units = re.findall(r'id="unit-(\d+)"', html)
print("Units in index.html:", units)
