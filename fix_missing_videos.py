import re
import json

yt_ids = [
    "51kO3-Jm5-s", "V_N7wWvN5z4", "aPzY5_9zO2A", "_F2PZcslXlA", "H2aHn0o_2s8", 
    "6uU5oB0w9aQ", "4qD7oA9q8wM", "2pY2a2h8x3M", "8y12Q9b9c9Q", "s63XgM-a4Uo"
]

data = [
    {
        "unit": 1,
        "reading_title": "Meeting People in New York",
        "reading_text": "New York is a big city. People are always busy. When Americans meet for the first time, they shake hands and say, 'Nice to meet you!' or 'How are you doing?' They use first names quickly.",
        "dialogue": [
            ("Sarah", "Hi, I'm Sarah. Nice to meet you!"),
            ("Mike", "Nice to meet you too, Sarah. I'm Mike. Where are you from?"),
            ("Sarah", "I'm from Boston. How about you?"),
            ("Mike", "I'm from Los Angeles. Welcome to New York!")
        ]
    },
    {
        "unit": 2,
        "reading_title": "American Families",
        "reading_text": "In the United States, families are diverse. Many people live with their parents and siblings in a house or an <b>apartment</b>. Extended families (grandparents, aunts, uncles) often get together for Thanksgiving in November.",
        "dialogue": [
            ("Lisa", "Do you have a big family?"),
            ("Tom", "No, I have a small family. Just my mom, dad, and my younger sister."),
            ("Lisa", "Do your grandparents live with you?"),
            ("Tom", "No, they live in Florida. We visit them every summer.")
        ]
    },
    {
        "unit": 3,
        "reading_title": "A Typical American Morning",
        "reading_text": "Many Americans wake up early, around 6:30 AM. They take a quick shower, drink a cup of coffee, and eat cereal or toast. Then, they take the bus or drive their car to work or school.",
        "dialogue": [
            ("Emma", "What time do you usually get up?"),
            ("Jake", "I get up at 7:00 AM. I grab a coffee and go to work."),
            ("Emma", "Do you eat breakfast?"),
            ("Jake", "Sometimes. Usually just a donut or a bagel.")
        ]
    },
    {
        "unit": 4,
        "reading_title": "Eating Out at a Diner",
        "reading_text": "An American diner is a casual restaurant. You can eat breakfast there all day! People love pancakes, bacon, and eggs. The waitress usually brings you a glass of ice water for free.",
        "dialogue": [
            ("Waiter", "Hi guys, are you ready to order?"),
            ("Customer", "Yes, I'll have the cheeseburger and <b>french fries</b>, please."),
            ("Waiter", "Would you like something to drink?"),
            ("Customer", "Just a glass of water with ice. Thank you!")
        ]
    }
]

HTML_TEMPLATE = """
        <!-- 🇺🇸 AMERICAN ENGLISH IN USE (OXFORD STYLE) -->
        <section class="culture-section" style="margin-top: 0 !important;">
            <h2 class="section-title">{reading_title}</h2>
            
            <!-- YouTube Embedded Video -->
            <div class="youtube-container">
                <iframe src="https://www.youtube.com/embed/{youtube_id}?rel=0" allowfullscreen></iframe>
            </div>
            
            <div class="reading-passage" id="{reading_id}">
                <h3>📖 American Culture Notes</h3>
                <p>{reading_text}</p>
                <div style="margin-top:1rem;">
                    <button class="audio-btn" onclick="speakText('{reading_text_clean}')">🔊 Listen to Notes</button>
                    <button class="audio-btn stop" onclick="stopAudio()">⏹️ Stop</button>
                </div>
            </div>

            <div class="american-dialogue" id="{dialogue_id}">
                <h3>🗣️ Everyday Dialogue</h3>
                <div class="dialogue-box">
                    {dialogue_html}
                </div>
                <div style="margin-top:1rem;">
                    <button class="audio-btn" onclick="speakText('Dialogue. {dialogue_text_clean}')">🔊 Listen to Dialogue</button>
                    <button class="audio-btn stop" onclick="stopAudio()">⏹️ Stop</button>
                </div>
            </div>
        </section>
"""

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

for d in data:
    unit_num = d["unit"]
    yt = yt_ids[(unit_num - 1) % len(yt_ids)]
    
    clean_reading = re.sub(r'<[^>]+>', '', d["reading_text"]).replace("'", "\\'")
    
    dialogue_lines = []
    dialogue_clean = []
    for speaker, text in d["dialogue"]:
        dialogue_lines.append(f'<p style="margin-bottom: 0.5rem;"><strong>{speaker}:</strong> {text}</p>')
        dialogue_clean.append(f"{speaker} says: {text}")
        
    dialogue_text_clean = " ".join(dialogue_clean).replace("'", "\\'")
    
    html = HTML_TEMPLATE.format(
        reading_title=d["reading_title"],
        reading_text=d["reading_text"],
        youtube_id=yt,
        reading_id=f"am-text-{unit_num}",
        reading_text_clean=clean_reading,
        dialogue_id=f"am-dialogue-{unit_num}",
        dialogue_html="\n                    ".join(dialogue_lines),
        dialogue_text_clean=dialogue_text_clean
    )
    
    # We need to insert this html right after <div class="container"> inside the specific unit block
    pattern = rf'(<div id="unit-{unit_num}" class="course-unit".*?<div class="container">)'
    match = re.search(pattern, content, re.DOTALL)
    if match:
        new_block = match.group(1) + html
        content = content.replace(match.group(1), new_block)
        print(f"Injected Video into Unit {unit_num}")
    else:
        print(f"Failed to find Unit {unit_num}")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)
print("Done fixing missing videos!")
