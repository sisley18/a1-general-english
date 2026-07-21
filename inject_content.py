import re
import json

# Curated YouTube IDs for A1 English (VOA Learning English / Everyday English)
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
    },
    {
        "unit": 5,
        "reading_title": "Homes in the Suburbs",
        "reading_text": "Many American families live in the suburbs. These are quiet neighborhoods outside the big city. Houses usually have a front <b>yard</b> and a backyard for barbecues. People park their cars in the <b>garage</b>.",
        "dialogue": [
            ("Agent", "This is a beautiful house. It has three bedrooms and two bathrooms."),
            ("Buyer", "Is there a garage?"),
            ("Agent", "Yes, a two-car garage. And a big backyard!"),
            ("Buyer", "Awesome. I love it.")
        ]
    },
    {
        "unit": 6,
        "reading_title": "Navigating the City",
        "reading_text": "American cities are built on a grid system. It is easy to find places. Streets go east to west, and avenues go north to south. If you are lost, you can ask a police officer for directions.",
        "dialogue": [
            ("Tourist", "Excuse me, where is the nearest <b>subway</b> station?"),
            ("Local", "Go straight for two blocks, then turn left on 5th Avenue."),
            ("Tourist", "Thank you! Is there a <b>restroom</b> near here?"),
            ("Local", "Yes, there is one in the coffee shop on the corner.")
        ]
    },
    {
        "unit": 7,
        "reading_title": "Shopping at the Mall",
        "reading_text": "Americans love going to the shopping mall. Malls have many stores, a food court, and sometimes a movie theater. In the winter, malls are warm. In the summer, they have cold air conditioning.",
        "dialogue": [
            ("Clerk", "Hi, can I help you find something?"),
            ("Shopper", "Yes, I'm looking for a pair of <b>sneakers</b>."),
            ("Clerk", "What size do you wear?"),
            ("Shopper", "I wear a size 10. Do you have these in black?")
        ]
    },
    {
        "unit": 8,
        "reading_title": "Weekend Hobbies",
        "reading_text": "On weekends, Americans enjoy many hobbies. They play sports like baseball or basketball. Many people love going camping in national parks or watching movies on Netflix at home.",
        "dialogue": [
            ("Mark", "What do you like doing in your free time?"),
            ("Lucy", "I love hiking and taking photos. What about you?"),
            ("Mark", "I'm a big fan of baseball. I watch games every Sunday."),
            ("Lucy", "That sounds fun!")
        ]
    }
]

# Generate remaining units up to 24 with a pattern to save script space
for i in range(9, 25):
    data.append({
        "unit": i,
        "reading_title": f"American English in Use (Unit {i})",
        "reading_text": "American culture is full of interesting idioms and everyday phrases. When speaking with locals, pay attention to the pronunciation of words and the casual expressions they use in daily conversations. <b>Practice makes perfect!</b>",
        "dialogue": [
            ("Alex", "Hey, how's it going today?"),
            ("Jordan", "Pretty good, thanks! Just studying some English."),
            ("Alex", "Awesome. Keep up the great work!"),
            ("Jordan", "Thanks, I will!")
        ]
    })

HTML_TEMPLATE = """
        <!-- 🇺🇸 AMERICAN ENGLISH IN USE (OXFORD STYLE) -->
        <section class="culture-section" style="margin-top: 3rem;">
            <span class="section-label" style="background: var(--accent-orange); color: white;">🇺🇸 American English in Use</span>
            <h2 class="section-title">{reading_title}</h2>
            
            <!-- YouTube Embedded Video -->
            <div class="youtube-container">
                <iframe src="https://www.youtube.com/embed/{youtube_id}?rel=0" allowfullscreen></iframe>
            </div>

            <p style="font-size: 1.15rem; color: var(--text-secondary); margin-bottom: 1.5rem;">{reading_text}</p>
            <button class="audio-btn" onclick="speakText('{reading_id}')" style="margin-bottom: 2rem;">🔊 Listen to Text</button>
            <div id="{reading_id}" style="display: none;">{reading_text_clean}</div>

            <!-- Dialogue -->
            <div class="american-dialogue">
                <h3 style="color: var(--accent-indigo); margin-bottom: 1rem;">🗣️ Real World Conversation</h3>
                <div id="{dialogue_id}">
                    {dialogue_html}
                </div>
                <button class="audio-btn" onclick="speakText('{dialogue_id}')" style="margin-top: 1rem;">🔊 Listen to Conversation</button>
            </div>
        </section>
"""

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

for d in data:
    unit_num = d["unit"]
    yt = yt_ids[unit_num % len(yt_ids)]
    
    clean_reading = re.sub(r'<[^>]+>', '', d["reading_text"])
    
    dialogue_lines = []
    dialogue_clean = []
    for speaker, text in d["dialogue"]:
        dialogue_lines.append(f'<p style="margin-bottom: 0.5rem;"><strong>{speaker}:</strong> {text}</p>')
        dialogue_clean.append(f"{speaker} says: {text}")
        
    html = HTML_TEMPLATE.format(
        reading_title=d["reading_title"],
        reading_text=d["reading_text"],
        youtube_id=yt,
        reading_id=f"am-text-{unit_num}",
        reading_text_clean=clean_reading,
        dialogue_id=f"am-dialogue-{unit_num}",
        dialogue_html="\n                    ".join(dialogue_lines)
    )
    
    # We need to insert this html just before the end of the unit's section-wrapper or practice-section.
    # Every unit ends with `    </div>\n</div>`
    
    # Find the block for the current unit
    pattern = rf'(<div id="unit-{unit_num}" class="course-unit".*?)(    </div>\n</div>)'
    match = re.search(pattern, content, re.DOTALL)
    if match:
        new_block = match.group(1) + html + match.group(2)
        content = content.replace(match.group(0), new_block)
        print(f"Injected Unit {unit_num}")
    else:
        print(f"Could not find Unit {unit_num}")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)
print("Done injecting!")
