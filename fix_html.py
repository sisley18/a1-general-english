import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Remove the white label that user complained about
content = content.replace('<span class="section-label" style="background: var(--accent-orange); color: white;">🇺🇸 American English in Use</span>', '')

# Ensure we remove any other explicit white text styles that might be invisible
content = content.replace('color: white;', '')
content = content.replace('color:white;', '')
content = content.replace('color: #fff;', '')
content = content.replace('color:#fff;', '')

# Also, the user might be referring to the button text being white against a white background? 
# No, audio buttons have gradients. 
# But just to be safe, let's make sure the inline styles in index.html don't force white text where it shouldn't.

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)
print("Removed white text inline styles.")
