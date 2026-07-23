import sys
sys.stdout.reconfigure(encoding='utf-8')

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Check if script.js tag is present
if '<script src="script.js"></script>' not in html:
    print("Adding missing script.js tag and closing HTML tags...")
    
    # Strip any trailing whitespace
    html = html.rstrip()
    
    closing_block = """

    </main>

    <footer style="text-align: center; padding: 2rem; color: #64748b; margin-top: 3rem; border-top: 1px solid #e2e8f0;">
        <p>&copy; A1 General English Coursebook — CEFR Level A1</p>
    </footer>

    <script src="script.js"></script>
</body>
</html>
"""
    html += closing_block
    
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("SUCCESS: script.js tag and closing tags added to index.html!")
else:
    print("script.js tag is already present in index.html.")
