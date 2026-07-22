import os
import shutil

# 1. Create directory structure
os.makedirs("a2b/images", exist_ok=True)
print("Created directory structure 'a2b/images'")

# 2. Copy illustration assets
src_files = {
    r"C:\Users\curso\.gemini\antigravity-ide\brain\805ee8e1-df77-4ddb-8ef2-7d6dc731fdbc\english_learning_illustration_st_john_1784724237464.png": "a2b/images/unit5_home.png",
    r"C:\Users\curso\.gemini\antigravity-ide\brain\805ee8e1-df77-4ddb-8ef2-7d6dc731fdbc\around_town_illustration_1784724281932.png": "a2b/images/unit6_town.png",
    r"C:\Users\curso\.gemini\antigravity-ide\brain\805ee8e1-df77-4ddb-8ef2-7d6dc731fdbc\clothes_shopping_illustration_1784724298086.png": "a2b/images/unit7_clothes.png"
}

for src, dst in src_files.items():
    if os.path.exists(src):
        shutil.copy(src, dst)
        print(f"Copied {src} to {dst}")
    else:
        print(f"Source file not found: {src}")

# 3. Create a2b/styles.css
css_content = """/* Global Reset & Typography */
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap');

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Outfit', sans-serif;
    background: linear-gradient(135deg, #faf8f5, #fcece7);
    color: #1e293b;
    min-height: 100vh;
    line-height: 1.6;
}

/* Portal Container Layout */
.portal-container {
    display: flex;
    min-height: 100vh;
}

/* Sidebar Navigation */
.sidebar {
    width: 320px;
    background: rgba(255, 255, 255, 0.9);
    backdrop-filter: blur(10px);
    border-right: 1px solid rgba(226, 232, 240, 0.8);
    display: flex;
    flex-direction: column;
    padding: 2rem 1.5rem;
    flex-shrink: 0;
}

.portal-title {
    font-size: 1.5rem;
    font-weight: 700;
    color: #1e293b;
    margin-bottom: 0.5rem;
    display: flex;
    align-items: center;
    gap: 10px;
}

.portal-subtitle {
    font-size: 0.85rem;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: #64748b;
    font-weight: 600;
}

/* Progress Section */
.progress-section {
    margin: 1.5rem 0 2rem;
    background: #f8fafc;
    padding: 1rem;
    border-radius: 12px;
    border: 1px solid #e2e8f0;
}

.progress-header {
    display: flex;
    justify-content: space-between;
    font-size: 0.85rem;
    font-weight: bold;
    color: #475569;
}

.progress-bar-container {
    background: #cbd5e1;
    height: 10px;
    border-radius: 5px;
    overflow: hidden;
    margin-top: 0.5rem;
}

.progress-bar {
    background: linear-gradient(90deg, #d97706, #f59e0b);
    height: 100%;
    width: 0%;
    transition: width 0.4s ease;
}

/* Unit Selector List */
.unit-list {
    list-style: none;
    overflow-y: auto;
    flex-grow: 1;
}

.unit-item {
    padding: 1rem;
    border-radius: 10px;
    margin-bottom: 0.75rem;
    cursor: pointer;
    transition: all 0.2s ease;
    border: 1px solid transparent;
    background: #ffffff;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.unit-item:hover {
    background: #f8fafc;
    border-color: #cbd5e1;
}

.unit-item.active {
    background: #fef3c7;
    border-color: #f59e0b;
    font-weight: 600;
}

.unit-info {
    display: flex;
    flex-direction: column;
    gap: 0.25rem;
}

.unit-num {
    font-size: 0.75rem;
    color: #d97706;
    text-transform: uppercase;
    font-weight: bold;
}

.unit-name {
    font-size: 0.95rem;
    color: #1e293b;
}

.unit-status {
    width: 18px;
    height: 18px;
    border-radius: 50%;
    border: 2px solid #94a3b8;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 0.7rem;
    color: transparent;
    transition: all 0.2s ease;
}

.unit-item.completed .unit-status {
    border-color: #10b981;
    background: #10b981;
    color: white;
}

/* Main Workspace */
.workspace {
    flex-grow: 1;
    padding: 3rem;
    max-width: 1200px;
    margin: 0 auto;
    width: 100%;
}

.workspace-header {
    margin-bottom: 2rem;
}

.active-unit-num {
    font-size: 0.9rem;
    text-transform: uppercase;
    color: #d97706;
    font-weight: 700;
    letter-spacing: 0.05em;
}

.active-unit-title {
    font-size: 2.25rem;
    font-weight: 700;
    color: #1e293b;
    margin-top: 0.25rem;
}

/* Tabs System */
.tabs-container {
    display: flex;
    gap: 0.75rem;
    margin-bottom: 2rem;
    border-bottom: 2px solid #e2e8f0;
    padding-bottom: 0.75rem;
}

.tab-button {
    background: none;
    border: none;
    padding: 0.75rem 1.5rem;
    border-radius: 20px;
    font-weight: 600;
    font-size: 0.95rem;
    cursor: pointer;
    color: #64748b;
    transition: all 0.2s ease;
    display: flex;
    align-items: center;
    gap: 8px;
}

.tab-button:hover {
    color: #1e293b;
    background: rgba(226, 232, 240, 0.5);
}

.tab-button.active {
    background: #1e293b;
    color: #ffffff;
}

/* Tab Panels */
.tab-panel {
    display: none;
    animation: fadeIn 0.3s ease-in-out;
}

.tab-panel.active {
    display: block;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(5px); }
    to { opacity: 1; transform: translateY(0); }
}

/* Content Layouts */
.glass-container {
    background: rgba(255, 255, 255, 0.75);
    backdrop-filter: blur(12px);
    border-radius: 20px;
    border: 1px solid rgba(255, 255, 255, 0.6);
    box-shadow: 0 10px 30px rgba(0,0,0,0.03);
    padding: 2.5rem;
}

/* Two Column Layout (Tab 1: Video & Reading) */
.two-column-layout {
    display: grid;
    grid-template-columns: 1.2fr 0.8fr;
    gap: 2.5rem;
}

.video-container {
    width: 100%;
    aspect-ratio: 16/9;
    background: #000;
    border-radius: 16px;
    overflow: hidden;
    box-shadow: 0 8px 24px rgba(0,0,0,0.15);
    border: 4px solid #fff;
}

.video-container iframe {
    width: 100%;
    height: 100%;
    border: none;
}

.reading-passage-box {
    background: #fff;
    padding: 2rem;
    border-radius: 16px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.02);
}

.reading-text {
    font-size: 1.1rem;
    color: #334155;
    line-height: 1.7;
    margin: 1.5rem 0;
}

.tiktok-btn {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: #000;
    color: #fff;
    padding: 8px 16px;
    border-radius: 24px;
    font-weight: bold;
    font-size: 0.9rem;
    text-decoration: none;
    transition: transform 0.2s ease;
}

.tiktok-btn:hover {
    transform: scale(1.05);
}

/* Vocabulary Grid */
.vocab-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 1.5rem;
}

.vocab-card {
    background: #fff;
    border-radius: 14px;
    padding: 1.5rem;
    box-shadow: 0 4px 12px rgba(0,0,0,0.03);
    border: 1px solid #f1f5f9;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    transition: all 0.2s ease;
}

.vocab-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 20px rgba(0,0,0,0.06);
}

.vocab-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    margin-bottom: 0.5rem;
}

.vocab-word {
    font-size: 1.25rem;
    font-weight: 700;
    color: #1e293b;
}

.vocab-def {
    font-size: 0.9rem;
    color: #64748b;
    margin-bottom: 0.75rem;
}

.vocab-ex {
    font-size: 0.95rem;
    color: #334155;
    font-style: italic;
    border-left: 3px solid #f59e0b;
    padding-left: 0.5rem;
    margin-bottom: 1rem;
}

/* Buttons */
.audio-btn {
    background: linear-gradient(135deg, #f59e0b, #d97706);
    border: none;
    color: white;
    cursor: pointer;
    width: 36px;
    height: 36px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1rem;
    transition: all 0.2s ease;
}

.audio-btn:hover {
    transform: scale(1.1);
}

.audio-btn.primary {
    width: auto;
    height: auto;
    border-radius: 20px;
    padding: 0.6rem 1.2rem;
    font-weight: bold;
    display: inline-flex;
    gap: 8px;
}

/* Grammar Section Styles */
.grammar-box {
    background: #fff;
    padding: 2rem;
    border-radius: 16px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.02);
}

.grammar-rule {
    background: #f8fafc;
    border-left: 4px solid #1e293b;
    padding: 1.25rem;
    border-radius: 8px;
    margin-bottom: 1.5rem;
}

/* Practice & Quiz Styles */
.quiz-section {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
}

.question-card {
    background: #fff;
    padding: 1.5rem;
    border-radius: 12px;
    border: 1px solid #e2e8f0;
}

.question-text {
    font-weight: 600;
    margin-bottom: 1rem;
}

.options-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 0.75rem;
}

.option-btn {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    padding: 0.75rem 1rem;
    border-radius: 8px;
    cursor: pointer;
    font-weight: 500;
    transition: all 0.2s ease;
    text-align: left;
}

.option-btn:hover {
    background: #f1f5f9;
    border-color: #cbd5e1;
}

.option-btn.selected {
    background: #1e293b;
    color: white;
    border-color: #1e293b;
}

.option-btn.correct {
    background: #d1fae5;
    color: #065f46;
    border-color: #34d399;
}

.option-btn.incorrect {
    background: #fee2e2;
    color: #991b1b;
    border-color: #f87171;
}

.submit-quiz-btn {
    background: linear-gradient(135deg, #10b981, #059669);
    border: none;
    color: white;
    padding: 0.8rem 1.8rem;
    border-radius: 20px;
    font-weight: bold;
    cursor: pointer;
    font-size: 1rem;
    align-self: center;
    transition: transform 0.2s ease;
}

.submit-quiz-btn:hover {
    transform: scale(1.05);
}

.feedback-msg {
    margin-top: 1rem;
    font-weight: bold;
}

/* Dialogue Box styling */
.dialogue-box {
    background: #f8fafc;
    padding: 1.5rem;
    border-radius: 12px;
    margin-bottom: 1.5rem;
    border: 1px solid #e2e8f0;
}

.speaker-line {
    margin-bottom: 0.75rem;
}

.speaker-name {
    font-weight: bold;
    color: #d97706;
}

/* Device Responsiveness */
@media (max-width: 768px) {
    .portal-container {
        flex-direction: column;
    }
    .sidebar {
        width: 100%;
        min-height: auto;
        border-right: none;
        border-bottom: 1px solid rgba(226, 232, 240, 0.8);
        padding: 1.5rem;
    }
    .workspace {
        padding: 1.5rem 1rem;
    }
    .two-column-layout {
        grid-template-columns: 1fr;
        gap: 1.5rem;
    }
    .active-unit-title {
        font-size: 1.75rem;
    }
}
"""

with open("a2b/styles.css", "w", encoding="utf-8") as f:
    f.write(css_content.strip())
print("Created 'a2b/styles.css'")

# 4. Create a2b/script.js
js_content = """// Course Data Source
const courseData = {
    1: {
        num: "Unit 1",
        title: "People and Lifestyles",
        video_id: "r6pQ5W01-8k",
        tiktok_url: "https://www.tiktok.com/@speakenglishwithvanessa",
        reading_title: "American Lifestyles",
        reading_text: "In the United States, lifestyles vary depending on where people live. City residents often have fast-paced routines and rely on public transportation. In suburban areas, families typically enjoy spacious homes and drive cars to commute. Most Americans value their free time, spent attending barbecues, practicing sports, or visiting local community centers on weekends.",
        dialogue: [
            { name: "John", text: "How is your new routine in Seattle, Amy?" },
            { name: "Amy", text: "It is quite busy! I walk to the office every morning and usually grab coffee at a diner." },
            { name: "John", text: "Do you have a lot of free time on weekends?" },
            { name: "Amy", text: "Yes! I usually go hiking or visit nearby parks with my friends." }
        ],
        vocab: [
            { word: "Routine", def: "A sequence of actions regularly followed", ex: "My morning routine starts with a short walk." },
            { word: "Commute", def: "To travel regularly to work or school", ex: "Many people commute by subway." },
            { word: "Spacious", def: "Having ample space", ex: "They live in a spacious house in the suburbs." },
            { word: "Grab", def: "To get or buy something quickly", ex: "Let's grab a coffee before the class." },
            { word: "Diner", def: "A small, informal restaurant", ex: "We eat breakfast at the local diner." },
            { word: "Fast-paced", def: "Moving or developing very quickly", ex: "Life in New York is very fast-paced." }
        ],
        grammar_title: "Present Simple vs. Present Continuous",
        grammar_rule: "Use the **Present Simple** for habits, routines, and permanent situations. Use the **Present Continuous** for actions happening right now, at the moment of speaking.<br><br>• <strong>Present Simple:</strong> I commute by train every day.<br>• <strong>Present Continuous:</strong> I am walking to the diner right now.",
        grammar_listen: "I commute by train every day. I am walking to the diner right now. He works in Seattle. They are visiting a park at the moment.",
        quiz: [
            { q: "Choose the correct verb: 'She usually _____ breakfast at a local diner.'", options: ["eats", "is eating", "eating", "eat"], correct: 0 },
            { q: "Choose the correct verb: 'Look! They _____ a soccer game in the park.'", options: ["plays", "play", "are playing", "played"], correct: 2 },
            { q: "Fill in the blank: 'I _____ to Seattle next week for vacation.'", options: ["am traveling", "travels", "traveled", "travel"], correct: 0 }
        ]
    },
    2: {
        num: "Unit 2",
        title: "Travel Adventures",
        video_id: "B2J9T3P5a6o",
        tiktok_url: "https://www.tiktok.com/@speakenglishwithvanessa",
        reading_title: "Exploring the National Parks",
        reading_text: "National parks are incredibly popular travel destinations in America. While visitors were exploring Yosemite National Park last summer, they encountered beautiful waterfalls and giant redwood trees. Travel adventures can be unpredictable, but they offer great memories if you prepare properly, check maps, and follow safety signs.",
        dialogue: [
            { name: "Julia", text: "How was your holiday in St. John, Carlos?" },
            { name: "Carlos", text: "It was fantastic! While I was hiking in Trunk Bay, I saw amazing turtles." },
            { name: "Julia", text: "Was the weather good?" },
            { name: "Carlos", text: "Yes, it was hot and sunny every day." }
        ],
        vocab: [
            { word: "Destination", def: "The place to which someone is going", ex: "Florida is a popular travel destination." },
            { word: "Encounter", def: "To meet or run into unexpectedly", ex: "We might encounter wildlife in the park." },
            { word: "Unpredictable", def: "Not able to be foreseen or known beforehand", ex: "The island weather can be unpredictable." },
            { word: "Redwood", def: "A giant coniferous tree native to California", ex: "The redwood trees are beautiful." },
            { word: "Waterfalls", def: "Streams of water falling from a height", ex: "We walked to the waterfalls yesterday." },
            { word: "Hiking", def: "Walking in nature, mountains, or forests", ex: "I was hiking in Trunk Bay yesterday." }
        ],
        grammar_title: "Past Simple vs. Past Continuous",
        grammar_rule: "Use the **Past Continuous** (was/were + verb-ing) to describe an ongoing past action. Use the **Past Simple** to describe a completed action that interrupted it.<br><br>• <strong>Example:</strong> While I was hiking in Trunk Bay, I saw a sea turtle.",
        grammar_listen: "While I was hiking in Trunk Bay, I saw a sea turtle. They were traveling by plane when the storm started.",
        quiz: [
            { q: "Complete the sentence: 'While I _____ on the beach, it started to rain.'", options: ["was sitting", "sat", "sitting", "were sitting"], correct: 0 },
            { q: "Complete: 'They _____ beautiful birds while they were walking in the forest.'", options: ["saw", "was seeing", "were seeing", "see"], correct: 0 },
            { q: "Choose: 'When the ferry arrived, we _____ in the harbor.'", options: ["were waiting", "waited", "was waiting", "wait"], correct: 0 }
        ]
    },
    3: {
        num: "Unit 3",
        title: "Technology and Innovation",
        video_id: "c2M9K8L6x7y",
        tiktok_url: "https://www.tiktok.com/@rachels_english",
        reading_title: "Digital Life in the US",
        reading_text: "Smart technology has changed how people work and study in the US. Over the past decade, video call platforms, smart home assistant systems, and wearable health monitors have become part of daily routines. Most classrooms have integrated digital tools, allowing students to access lessons remotely.",
        dialogue: [
            { name: "Developer", text: "Have you tried the new software yet?" },
            { name: "User", text: "Yes, I have used it for two days. It is very fast!" },
            { name: "Developer", text: "Great. We have worked on this update since last January." }
        ],
        vocab: [
            { word: "Platform", def: "A digital system or software tool", ex: "We use a video call platform for classes." },
            { word: "Wearable", def: "A technological device worn on the body", ex: "My wearable watch monitors my heart rate." },
            { word: "Assistant", def: "A device or software helper", ex: "The smart assistant turned off the lights." },
            { word: "Remote", def: "Distant, from a separate location", ex: "She works from a remote office." },
            { word: "Integrate", def: "To combine or make part of a whole", ex: "They integrated technology into the classroom." },
            { word: "Software", def: "Programs used by a computer", ex: "This new software is easy to run." }
        ],
        grammar_title: "Present Perfect with For and Since",
        grammar_rule: "Use the **Present Perfect** (have/has + past participle) to talk about actions that started in the past and continue in the present. Use **for** to express duration. Use **since** to express the starting point.<br><br>• <strong>Example:</strong> I have lived in St. John for five years.<br>• <strong>Example:</strong> She has used this software since Monday.",
        grammar_listen: "I have lived in St. John for five years. She has used this software since Monday. We have studied English since 2024.",
        quiz: [
            { q: "Complete the sentence: 'She _____ this smartwatch since last year.'", options: ["has owned", "owned", "is owning", "have owned"], correct: 0 },
            { q: "Complete: 'We have worked remotely _____ three months.'", options: ["for", "since", "during", "ago"], correct: 0 },
            { q: "Choose: 'I _____ a smartphone since I was in university.'", options: ["have had", "had", "am having", "has had"], correct: 0 }
        ]
    },
    4: {
        num: "Unit 4",
        title: "Future Possibilities",
        video_id: "B2J9T3P5a6o",
        tiktok_url: "https://www.tiktok.com/@speakenglishwithvanessa",
        reading_title: "Future Careers in Tech",
        reading_text: "The job market is shifting, and new career fields are emerging. Experts predict that green energy, AI programming, and remote healthcare will create millions of jobs. Many university students are planning to start their own online businesses after graduation, expecting to work from anywhere in the world.",
        dialogue: [
            { name: "Counselor", text: "What are you going to do after graduation?" },
            { name: "Student", text: "I am going to work as a software engineer in St. Thomas." },
            { name: "Counselor", text: "Great. I think that sector will grow very quickly." }
        ],
        vocab: [
            { word: "Career", def: "An occupation undertaken for a significant period", ex: "She is pursuing a career in technology." },
            { word: "Graduate", def: "Complete a course of study at a school or college", ex: "They will graduate next summer." },
            { word: "Sector", def: "A distinct part or branch of an economy", ex: "The tech sector is expanding rapidly." },
            { word: "Predict", def: "To say or estimate what will happen in the future", ex: "Scientists predict warmer summers." },
            { word: "Emerging", def: "Becoming apparent, important, or prominent", ex: "Green energy is an emerging field." },
            { word: "Business", def: "An organization engaged in commercial activities", ex: "He wants to start a remote business." }
        ],
        grammar_title: "Future Forms: Will vs. Going to",
        grammar_rule: "Use **going to** for planned future actions and intentions. Use **will** for predictions, instant decisions, and offers.<br><br>• <strong>Intention (going to):</strong> I am going to study tonight.<br>• <strong>Prediction (will):</strong> I think it will rain tomorrow.",
        grammar_listen: "I am going to study tonight. I think it will rain tomorrow. We are going to buy a new laptop.",
        quiz: [
            { q: "Complete: 'My brother _____ study biology at university next semester.'", options: ["is going to", "will", "shall", "goes to"], correct: 0 },
            { q: "Complete: 'I think the tech sector _____ create more jobs in the future.'", options: ["will", "is going to", "going to", "shall"], correct: 0 },
            { q: "Choose: 'Oh, you need help? I _____ carry that suitcase for you.'", options: ["will", "am going to", "going to", "goes to"], correct: 0 }
        ]
    },
    5: {
        num: "Unit 5",
        title: "Health and Wellness",
        video_id: "r6pQ5W01-8k",
        tiktok_url: "https://www.tiktok.com/@speakenglishwithvanessa",
        reading_title: "Healthy Lifestyles in America",
        reading_text: "American health institutes advise that physical activity is essential. You must drink enough water, eat vegetables, and exercise three times a week. If you have a headache or a cold, you should rest. If symptoms are severe, you must visit a doctor at the local hospital.",
        dialogue: [
            { name: "Doctor", text: "You must rest for two days. You should also drink warm tea." },
            { name: "Patient", text: "Do I have to take any medicine?" },
            { name: "Doctor", text: "Yes, you must take these pills every morning." }
        ],
        vocab: [
            { word: "Symptom", def: "A physical sign of an illness", ex: "A fever is a common symptom of a cold." },
            { word: "Advise", def: "To offer suggestions about the best action", ex: "Doctors advise eating less sugar." },
            { word: "Severe", def: "Very intense, serious, or painful", ex: "He had a severe headache yesterday." },
            { word: "Pill", def: "A small round piece of medicine to swallow", ex: "You must take this pill twice a day." },
            { word: "Rest", def: "To relax, sleep, or recover strength", ex: "You should rest at home." },
            { word: "Fever", def: "An abnormally high body temperature", ex: "The child has a mild fever." }
        ],
        grammar_title: "Modals of Advice & Obligation: Should, Must, Have to",
        grammar_rule: "Use **should** for mild advice or suggestions. Use **must** and **have to** for strong obligations or rules.<br><br>• <strong>Advice:</strong> You should drink water.<br>• <strong>Obligation:</strong> You must wear a seatbelt.",
        grammar_listen: "You should drink water. You must wear a seatbelt. She has to work tomorrow.",
        quiz: [
            { q: "Complete: 'You have a high fever. You _____ see a doctor.'", options: ["must", "shouldn't", "have", "might"], correct: 0 },
            { q: "Complete: 'You _____ eat more fruit. It is good for your health.'", options: ["should", "mustn't", "have to", "has to"], correct: 0 },
            { q: "Choose: 'We _____ wear masks inside the hospital. It is a strict rule.'", options: ["have to", "should", "might", "can"], correct: 0 }
        ]
    },
    6: {
        num: "Unit 6",
        title: "Dreams and Ambitions",
        video_id: "G2sT23a07t8",
        tiktok_url: "https://www.tiktok.com/@speakenglishwithvanessa",
        reading_title: "Achieving Success",
        reading_text: "If people work hard, they will achieve their goals. Ambition is very common in American culture. Many young people dream of starting technology companies or becoming famous musicians. If they study at university and network with professionals, they will find great job opportunities.",
        dialogue: [
            { name: "Friend", text: "If you get the job in Seattle, will you move?" },
            { name: "You", text: "Yes! If I get the job, I will move next month." },
            { name: "Friend", text: "What would you do if you won the lottery?" },
            { name: "You", text: "If I won the lottery, I would buy a house in St. John!" }
        ],
        vocab: [
            { word: "Ambition", def: "A strong desire to achieve success", ex: "Her ambition is to study at Harvard." },
            { word: "Achieve", def: "To reach or attain a goal by effort", ex: "He worked hard to achieve his dream." },
            { word: "Network", def: "Connect with people for career support", ex: "It is important to network at university." },
            { word: "Opportunity", def: "A set of circumstances that makes it possible to do something", ex: "This job is a great opportunity." },
            { word: "Dream", def: "A cherished aspiration, ambition, or ideal", ex: "My dream is to travel the world." },
            { word: "Success", def: "The accomplishment of an aim or purpose", ex: "Hard work leads to success." }
        ],
        grammar_title: "First Conditional vs. Second Conditional",
        grammar_rule: "Use the **First Conditional** (If + Present, Will + Verb) for realistic future situations. Use the **Second Conditional** (If + Past, Would + Verb) for imaginary, unlikely, or impossible situations.<br><br>• <strong>Realistic (First):</strong> If it rains, I will stay home.<br>• <strong>Imaginary (Second):</strong> If I were rich, I would buy a beach resort.",
        grammar_listen: "If it rains, I will stay home. If I were rich, I would buy a beach resort.",
        quiz: [
            { q: "Complete: 'If he _____ hard, he will pass the test.'", options: ["studies", "studied", "will study", "study"], correct: 0 },
            { q: "Complete: 'If I _____ more money, I would travel to Europe.'", options: ["had", "have", "will have", "would have"], correct: 0 },
            { q: "Choose: 'If she gets a promotion, she _____ a new car.'", options: ["will buy", "bought", "would buy", "buys"], correct: 0 }
        ]
    },
    7: {
        num: "Unit 7",
        title: "Consumer Society",
        video_id: "4G4Cg_3G4l4",
        tiktok_url: "https://www.tiktok.com/@rachels_english",
        reading_title: "Shopping Malls and E-Commerce",
        reading_text: "Modern consumer society relies heavily on technology. Every day, millions of products are ordered online and shipped to houses across the country. In the past, most clothing items were bought at shopping malls, but now e-commerce platforms handle the majority of retail transactions.",
        dialogue: [
            { name: "Cashier", text: "Was this product ordered online?" },
            { name: "Customer", text: "Yes, it was purchased yesterday and delivered to my house this morning." },
            { name: "Cashier", text: "Great. The return was processed successfully." }
        ],
        vocab: [
            { word: "Consumer", def: "A person who purchases goods and services", ex: "Consumer preferences are changing." },
            { word: "Retail", def: "The sale of goods to the public", ex: "The retail industry is shifting online." },
            { word: "Transaction", def: "An instance of buying or selling something", ex: "The online transaction was secure." },
            { word: "Purchase", def: "To acquire something by paying money for it", ex: "He purchased sneakers online." },
            { word: "Deliver", def: "Bring and hand over letters, goods, or mail", ex: "They deliver packages to St. John." },
            { word: "Process", def: "Perform a series of mechanical or systematic operations", ex: "The payment was processed." }
        ],
        grammar_title: "Passive Voice: Present and Past Simple",
        grammar_rule: "Use the **Passive Voice** when the focus is on the action or the object receiving the action, rather than the person performing it.<br><br>• <strong>Present Passive:</strong> Online transactions **are processed** by software.<br>• <strong>Past Passive:</strong> This smartphone **was invented** in 2007.",
        grammar_listen: "Online transactions are processed by software. This smartphone was invented in 2007. The package was delivered to St. John.",
        quiz: [
            { q: "Complete: 'Many packages _____ to St. John every week.'", options: ["are delivered", "delivered", "is delivered", "deliver"], correct: 0 },
            { q: "Complete: 'This website _____ created in 2024.'", options: ["was", "were", "is", "has"], correct: 0 },
            { q: "Choose: 'Millions of credit card transactions _____ online daily.'", options: ["are made", "is made", "were make", "make"], correct: 0 }
        ]
    },
    8: {
        num: "Unit 8",
        title: "Entertainment and Media",
        video_id: "s2_yV7P_K0A",
        tiktok_url: "https://www.tiktok.com/@speakenglishwithvanessa",
        reading_title: "The Rise of Streaming Services",
        reading_text: "Streaming platforms have transformed how people consume entertainment. Instead of watching traditional cable television, Americans use digital apps to watch movies, series, and documentaries. Subscriptions are cheap, allowing viewers to access thousands of shows from any screen.",
        dialogue: [
            { name: "Friend A", text: "Do you know the actor who stars in this new movie?" },
            { name: "Friend B", text: "Yes, he is the actor who won the award last year." },
            { name: "Friend A", text: "Awesome. I want to watch the documentary that you recommended." }
        ],
        vocab: [
            { word: "Streaming", def: "Transmitting or receiving data over the internet in real time", ex: "I use streaming apps to watch series." },
            { word: "Subscription", def: "An agreement to pay recurringly for a service", ex: "My subscription is paid monthly." },
            { word: "Cable", def: "Traditional television transmission system", ex: "We canceled our cable television." },
            { word: "Documentary", def: "A movie or TV show documenting real facts", ex: "I watched an interesting documentary." },
            { word: "Viewers", def: "People who watch a television program or video", ex: "The show has millions of viewers." },
            { word: "Recommend", def: "Advise as being good or suitable", ex: "I recommend this movie." }
        ],
        grammar_title: "Relative Clauses: Who, Which, That, Where",
        grammar_rule: "Use **who** for people, **which** or **that** for things, and **where** for places to add detail without starting a new sentence.<br><br>• <strong>People (who):</strong> He is the student who won the spelling bee.<br>• <strong>Things (that/which):</strong> This is the book that I bought.<br>• <strong>Places (where):</strong> This is the school where I study.",
        grammar_listen: "He is the student who won the spelling bee. This is the book that I bought. This is the school where I study.",
        quiz: [
            { q: "Complete: 'This is the movie _____ I watched last night.'", options: ["that", "who", "where", "whom"], correct: 0 },
            { q: "Complete: 'She is the teacher _____ helped me learn English.'", options: ["who", "which", "where", "whose"], correct: 0 },
            { q: "Choose: 'Trunk Bay is the beach _____ we saw sea turtles.'", options: ["where", "which", "who", "that"], correct: 0 }
        ]
    },
    9: {
        num: "Unit 9",
        title: "Active Lifestyles",
        video_id: "c2M9K8L6x7y",
        tiktok_url: "https://www.tiktok.com/@rachels_english",
        reading_title: "Fitness Routines",
        reading_text: "Maintaining an active lifestyle requires planning and commitment. Many people enjoy jogging in local parks, practicing yoga, or swimming at the beach. Health experts recommend avoiding processed sugars and drinking plenty of water during physical exercise.",
        dialogue: [
            { name: "Trainer", text: "You should avoid eating heavy meals before working out." },
            { name: "Runner", text: "I know. I prefer eating a banana and drinking water." },
            { name: "Trainer", text: "Perfect. Don't forget to stretch after running." }
        ],
        vocab: [
            { word: "Fitness", def: "The condition of being physically fit and healthy", ex: "Fitness is important for longevity." },
            { word: "Commitment", def: "The state or quality of being dedicated to a cause", ex: "Regular exercise requires commitment." },
            { word: "Jogging", def: "Running at a gentle, slow pace", ex: "She goes jogging every morning." },
            { word: "Nutrition", def: "Providing or obtaining the food necessary for health", ex: "Good nutrition is key to weight loss." },
            { word: "Stretch", def: "Straighten or extend one's body or limbs", ex: "You must stretch before you run." },
            { word: "Avoid", def: "Keep away from or stop doing something", ex: "Try to avoid eating junk food." }
        ],
        grammar_title: "Gerunds vs. Infinitives",
        grammar_rule: "Some verbs are followed by **gerunds** (verb-ing), while others are followed by **infinitives** (to + verb).<br><br>• **Followed by Gerund (enjoy, avoid, practice):** I enjoy swimming in Trunk Bay. Avoid eating sugar.<br>• **Followed by Infinitive (want, hope, plan, decide):** I want to swim in the pool. She plans to run a marathon.",
        grammar_listen: "I enjoy swimming in Trunk Bay. Avoid eating sugar. I want to swim in the pool. She plans to run a marathon.",
        quiz: [
            { q: "Complete: 'They decided _____ to the gym instead of the beach.'", options: ["to go", "going", "go", "went"], correct: 0 },
            { q: "Complete: 'I really enjoy _____ soccer with my friends on Saturdays.'", options: ["playing", "to play", "play", "played"], correct: 0 },
            { q: "Choose: 'You should avoid _____ coffee late at night.'", options: ["drinking", "to drink", "drink", "drank"], correct: 0 }
        ]
    },
    10: {
        num: "Unit 10",
        title: "History and Mysteries",
        video_id: "B2J9T3P5a6o",
        tiktok_url: "https://www.tiktok.com/@speakenglishwithvanessa",
        reading_title: "The Mysteries of the Past",
        reading_text: "Historians study ancient ruins and artifacts to solve mysteries of the past. Before archeologists discovered the site, local residents had told stories about an ancient city hidden under the forest. When they finally excavated, they realized that a sophisticated civilization had lived there centuries ago.",
        dialogue: [
            { name: "Guide", text: "Before the museum opened, we had collected hundreds of artifacts." },
            { name: "Visitor", text: "Had anyone solved the mystery of the ancient coins?" },
            { name: "Guide", text: "Yes, our researchers had identified their origins before the exhibition started." }
        ],
        vocab: [
            { word: "Ruins", def: "The remains of a building or city that has suffered destruction", ex: "The ancient ruins are open to tourists." },
            { word: "Artifact", def: "An object made by a human being, typically of historical interest", ex: "The museum displays gold artifacts." },
            { word: "Excavate", def: "Make a hole or channel by digging", ex: "They planned to excavate the site." },
            { word: "Civilization", def: "The stage of human social development and organization", ex: "The Maya had a highly advanced civilization." },
            { word: "Mystery", def: "Something that is difficult or impossible to understand or explain", ex: "No one has solved the mystery of the coins." },
            { word: "Historian", def: "An expert in or student of history", ex: "The historian wrote a book about the islands." }
        ],
        grammar_title: "Past Perfect Simple",
        grammar_rule: "Use the **Past Perfect** (had + past participle) to describe an action that happened before another action in the past.<br><br>• **Past Perfect:** When the police arrived, the thief **had escaped**.<br>• **Past Simple:** When we arrived, the movie **started**.",
        grammar_listen: "When the police arrived, the thief had escaped. Before the museum opened, we had collected hundreds of artifacts.",
        quiz: [
            { q: "Complete: 'Before they excavated the site, they _____ historical records.'", options: ["had read", "read", "have read", "reading"], correct: 0 },
            { q: "Complete: 'When we arrived at the harbor, the ferry _____ already left.'", options: ["had", "has", "did", "was"], correct: 0 },
            { q: "Choose: 'She realized that she _____ her passport at the hotel.'", options: ["had forgotten", "forgot", "has forgotten", "forget"], correct: 0 }
        ]
    }
};

let currentUnit = 1;
let completedUnits = new Set();

// Speech Synthesis
function speakText(text) {
    if ('speechSynthesis' in window) {
        window.speechSynthesis.cancel(); // Stop current speech
        const utterance = new SpeechSynthesisUtterance(text);
        utterance.lang = 'en-US';
        utterance.rate = 0.9; // Fluid and clear pacing
        window.speechSynthesis.speak(utterance);
    } else {
        alert("Text-to-speech is not supported in this browser.");
    }
}

function stopAudio() {
    if ('speechSynthesis' in window) {
        window.speechSynthesis.cancel();
    }
}

// Tab Switching
function switchTab(tabId) {
    document.querySelectorAll('.tab-button').forEach(btn => btn.classList.remove('active'));
    document.querySelectorAll('.tab-panel').forEach(panel => panel.classList.remove('active'));

    const activeBtn = document.querySelector(`.tab-button[onclick="switchTab('${tabId}')"]`);
    const activePanel = document.getElementById(tabId);
    
    if (activeBtn && activePanel) {
        activeBtn.classList.add('active');
        activePanel.classList.add('active');
    }
}

// Load Unit Data
function loadUnit(unitId) {
    currentUnit = unitId;
    const data = courseData[unitId];

    // Update active class in sidebar
    document.querySelectorAll('.unit-item').forEach(item => item.classList.remove('active'));
    const activeItem = document.querySelector(`.unit-item[onclick="loadUnit(${unitId})"]`);
    if (activeItem) activeItem.classList.add('active');

    // Update Headers
    document.getElementById('active-unit-num').innerText = data.num;
    document.getElementById('active-unit-title').innerText = data.title;

    // Load Tab 1: Video & Reading
    document.getElementById('yt-iframe').src = `https://www.youtube.com/embed/${data.video_id}?rel=0`;
    document.getElementById('tiktok-link').href = data.tiktok_url;
    document.getElementById('reading-title').innerText = data.reading_title;
    document.getElementById('reading-body').innerText = data.reading_text;
    document.getElementById('reading-audio-btn').setAttribute('onclick', `speakText(courseData[${unitId}].reading_text)`);

    // Load Dialogue
    let dialogueHtml = '';
    data.dialogue.forEach(line => {
        dialogueHtml += `<div class="speaker-line"><span class="speaker-name">${line.name}:</span> <span class="speaker-text">${line.text}</span></div>`;
    });
    document.getElementById('dialogue-lines').innerHTML = dialogueHtml;
    
    // Create voice dialogue text
    let dialogueCombinedText = data.dialogue.map(l => `${l.name} says, ${l.text}`).join(". ");
    document.getElementById('dialogue-audio-btn').setAttribute('onclick', `speakText(\`${dialogueCombinedText}\`)`);

    // Load Tab 2: Vocabulary
    let vocabHtml = '';
    data.vocab.forEach((v, index) => {
        // Include illustrations for the first 3 units
        let imgHtml = '';
        if (unitId === 1 && index === 2) {
            // Unit 1 / Spacious (uses home illust)
            imgHtml = `<img src="images/unit5_home.png" alt="Spacious house illustration" style="width: 100%; height: 120px; object-fit: cover; border-radius: 8px; margin-bottom: 0.75rem;">`;
        } else if (unitId === 2 && index === 5) {
            // Unit 2 / Hiking (uses home/beach illust)
            imgHtml = `<img src="images/unit5_home.png" alt="Hiking beach illustration" style="width: 100%; height: 120px; object-fit: cover; border-radius: 8px; margin-bottom: 0.75rem;">`;
        } else if (unitId === 3 && index === 0) {
            // Unit 3 / Platform (uses town/map grid)
            imgHtml = `<img src="images/unit6_town.png" alt="Digital platform map illustration" style="width: 100%; height: 120px; object-fit: cover; border-radius: 8px; margin-bottom: 0.75rem;">`;
        }
        
        vocabHtml += `
            <div class="vocab-card">
                ${imgHtml}
                <div class="vocab-header">
                    <span class="vocab-word">${v.word}</span>
                    <button class="audio-btn" onclick="speakText('${v.word}. ${v.ex.replace(/'/g, "\\'")}')">🔊</button>
                </div>
                <div class="vocab-def">${v.def}</div>
                <div class="vocab-ex">"${v.ex}"</div>
            </div>
        `;
    });
    document.getElementById('vocab-container').innerHTML = vocabHtml;

    // Load Tab 3: Grammar
    document.getElementById('grammar-title-text').innerText = data.grammar_title;
    document.getElementById('grammar-rule-body').innerHTML = data.grammar_rule;
    document.getElementById('grammar-audio-btn').setAttribute('onclick', `speakText(courseData[${unitId}].grammar_listen)`);

    // Load Tab 4: Practice & Quiz
    let quizHtml = '';
    data.quiz.forEach((qData, qIndex) => {
        let optionsHtml = '';
        qData.options.forEach((opt, optIndex) => {
            optionsHtml += `
                <button class="option-btn" onclick="selectOption(${qIndex}, ${optIndex}, this)">
                    ${opt}
                </button>
            `;
        });
        
        quizHtml += `
            <div class="question-card" data-qindex="${qIndex}">
                <div class="question-text">${qIndex + 1}. ${qData.q}</div>
                <div class="options-grid">
                    ${optionsHtml}
                </div>
            </div>
        `;
    });
    
    quizHtml += `
        <button class="submit-quiz-btn" onclick="submitQuiz()">Submit Quiz</button>
        <div id="quiz-feedback" class="feedback-msg"></div>
    `;
    document.getElementById('quiz-container').innerHTML = quizHtml;
    
    // Reset workspace view to the first tab
    switchTab('tab-video');
}

// Select Quiz Option
let selectedAnswers = {};
function selectOption(qIndex, optIndex, btnElement) {
    // Deselect other buttons in the same question card
    const questionCard = btnElement.closest('.question-card');
    questionCard.querySelectorAll('.option-btn').forEach(btn => btn.classList.remove('selected'));
    
    // Select this button
    btnElement.classList.add('selected');
    selectedAnswers[qIndex] = optIndex;
}

// Submit Quiz
function submitQuiz() {
    const data = courseData[currentUnit];
    let correctCount = 0;
    
    data.quiz.forEach((qData, qIndex) => {
        const questionCard = document.querySelector(`.question-card[data-qindex="${qIndex}"]`);
        const buttons = questionCard.querySelectorAll('.option-btn');
        
        buttons.forEach((btn, optIndex) => {
            btn.classList.remove('correct', 'incorrect');
            
            if (optIndex === qData.correct) {
                // Highlight correct answer
                btn.classList.add('correct');
            }
            
            if (selectedAnswers[qIndex] === optIndex && optIndex !== qData.correct) {
                // Highlight incorrect answer selected by user
                btn.classList.add('incorrect');
            }
        });
        
        if (selectedAnswers[qIndex] === qData.correct) {
            correctCount++;
        }
    });

    const feedback = document.getElementById('quiz-feedback');
    feedback.style.color = correctCount === data.quiz.length ? '#059669' : '#dc2626';
    feedback.innerText = `You scored ${correctCount}/${data.quiz.length}!`;

    if (correctCount === data.quiz.length) {
        // Mark unit as completed
        markUnitCompleted(currentUnit);
    }
}

// Mark Unit as Completed
function markUnitCompleted(unitId) {
    completedUnits.add(unitId);
    
    // Update sidebar UI
    const unitItem = document.querySelector(`.unit-item[onclick="loadUnit(${unitId})"]`);
    if (unitItem) {
        unitItem.classList.add('completed');
        unitItem.querySelector('.unit-status').innerHTML = '✓';
    }
    
    // Update progress bar
    updateProgressBar();
}

// Update Progress Bar
function updateProgressBar() {
    const totalUnits = Object.keys(courseData).length;
    const completedCount = completedUnits.size;
    const percentage = Math.round((completedCount / totalUnits) * 100);
    
    document.getElementById('progress-bar').style.width = `${percentage}%`;
    document.getElementById('progress-text').innerText = `${percentage}% Complete`;
}

// Initialize on Load
window.addEventListener('DOMContentLoaded', () => {
    loadUnit(1);
    updateProgressBar();
});
"""

with open("a2b/script.js", "w", encoding="utf-8") as f:
    f.write(js_content.strip())
print("Created 'a2b/script.js'")

# 5. Create a2b/index.html
html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>A2-B1 University Learning Portal</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="portal-container">
        <!-- Sidebar Navigation -->
        <aside class="sidebar">
            <div class="portal-header">
                <h1 class="portal-title">🎓 EduPortal</h1>
                <p class="portal-subtitle">A2-B1 Transition Course</p>
            </div>
            
            <!-- Progress Section -->
            <div class="progress-section">
                <div class="progress-header">
                    <span>Course Progress</span>
                    <span id="progress-text">0% Complete</span>
                </div>
                <div class="progress-bar-container">
                    <div id="progress-bar" class="progress-bar"></div>
                </div>
            </div>

            <!-- Unit Selector -->
            <ul class="unit-list">
                <li class="unit-item active" onclick="loadUnit(1)">
                    <div class="unit-info">
                        <span class="unit-num">Unit 1</span>
                        <span class="unit-name">People & Lifestyles</span>
                    </div>
                    <div class="unit-status"></div>
                </li>
                <li class="unit-item" onclick="loadUnit(2)">
                    <div class="unit-info">
                        <span class="unit-num">Unit 2</span>
                        <span class="unit-name">Travel Adventures</span>
                    </div>
                    <div class="unit-status"></div>
                </li>
                <li class="unit-item" onclick="loadUnit(3)">
                    <div class="unit-info">
                        <span class="unit-num">Unit 3</span>
                        <span class="unit-name">Tech & Innovation</span>
                    </div>
                    <div class="unit-status"></div>
                </li>
                <li class="unit-item" onclick="loadUnit(4)">
                    <div class="unit-info">
                        <span class="unit-num">Unit 4</span>
                        <span class="unit-name">Future Possibilities</span>
                    </div>
                    <div class="unit-status"></div>
                </li>
                <li class="unit-item" onclick="loadUnit(5)">
                    <div class="unit-info">
                        <span class="unit-num">Unit 5</span>
                        <span class="unit-name">Health & Wellness</span>
                    </div>
                    <div class="unit-status"></div>
                </li>
                <li class="unit-item" onclick="loadUnit(6)">
                    <div class="unit-info">
                        <span class="unit-num">Unit 6</span>
                        <span class="unit-name">Dreams & Ambitions</span>
                    </div>
                    <div class="unit-status"></div>
                </li>
                <li class="unit-item" onclick="loadUnit(7)">
                    <div class="unit-info">
                        <span class="unit-num">Unit 7</span>
                        <span class="unit-name">Consumer Society</span>
                    </div>
                    <div class="unit-status"></div>
                </li>
                <li class="unit-item" onclick="loadUnit(8)">
                    <div class="unit-info">
                        <span class="unit-num">Unit 8</span>
                        <span class="unit-name">Entertainment & Media</span>
                    </div>
                    <div class="unit-status"></div>
                </li>
                <li class="unit-item" onclick="loadUnit(9)">
                    <div class="unit-info">
                        <span class="unit-num">Unit 9</span>
                        <span class="unit-name">Active Lifestyles</span>
                    </div>
                    <div class="unit-status"></div>
                </li>
                <li class="unit-item" onclick="loadUnit(10)">
                    <div class="unit-info">
                        <span class="unit-num">Unit 10</span>
                        <span class="unit-name">History & Mysteries</span>
                    </div>
                    <div class="unit-status"></div>
                </li>
            </ul>
        </aside>

        <!-- Main Workspace -->
        <main class="workspace">
            <header class="workspace-header">
                <span id="active-unit-num" class="active-unit-num">Unit 1</span>
                <h2 id="active-unit-title" class="active-unit-title">People and Lifestyles</h2>
            </header>

            <!-- Learning Tabs Selector -->
            <nav class="tabs-container">
                <button class="tab-button active" onclick="switchTab('tab-video')">📺 Video & Reading</button>
                <button class="tab-button" onclick="switchTab('tab-vocab')">📚 Vocabulary</button>
                <button class="tab-button" onclick="switchTab('tab-grammar')">📝 Grammar Box</button>
                <button class="tab-button" onclick="switchTab('tab-quiz')">🎯 Practice & Quiz</button>
            </nav>

            <!-- Workspace Cards Container -->
            <div class="glass-container">
                
                <!-- Tab 1: Video & Reading -->
                <div id="tab-video" class="tab-panel active">
                    <div class="two-column-layout">
                        <!-- Left: video -->
                        <div style="display: flex; flex-direction: column; gap: 1rem;">
                            <div class="video-container">
                                <iframe id="yt-iframe" src="" allowfullscreen></iframe>
                            </div>
                            <div style="display: flex; gap: 10px;">
                                <a id="tiktok-link" href="#" target="_blank" class="tiktok-btn">
                                    🎵 Practice on TikTok
                                </a>
                            </div>
                        </div>
                        
                        <!-- Right: Reading and Dialogue -->
                        <div class="reading-passage-box">
                            <h3 id="reading-title" style="color: #1e293b; font-size: 1.35rem; margin-bottom: 1rem; border-bottom: 2px solid #e2e8f0; padding-bottom: 0.5rem;">American Lifestyles</h3>
                            <p id="reading-body" class="reading-text"></p>
                            <button id="reading-audio-btn" class="audio-btn primary">🔊 Listen to Text</button>
                        </div>
                    </div>
                </div>

                <!-- Tab 2: Vocabulary Grid -->
                <div id="tab-vocab" class="tab-panel">
                    <div id="vocab-container" class="vocab-grid"></div>
                </div>

                <!-- Tab 3: Grammar Rule Box -->
                <div id="tab-grammar" class="tab-panel">
                    <div class="grammar-box">
                        <h3 id="grammar-title-text" style="font-size: 1.5rem; margin-bottom: 1rem; color: #1e293b;"></h3>
                        <div id="grammar-rule-body" class="grammar-rule"></div>
                        <div style="display: flex; gap: 10px;">
                            <button id="grammar-audio-btn" class="audio-btn primary">🔊 Listen to Examples</button>
                            <button class="audio-btn primary" style="background: #64748b;" onclick="stopAudio()">⏹️ Stop</button>
                        </div>
                    </div>
                </div>

                <!-- Tab 4: Practice Dialogue & Quizzes -->
                <div id="tab-quiz" class="tab-panel">
                    <div class="two-column-layout">
                        <!-- Left: Dialogue role-play -->
                        <div class="reading-passage-box">
                            <h3 style="color: #1e293b; font-size: 1.35rem; margin-bottom: 1.5rem;">🗣️ Real World Conversation</h3>
                            <div id="dialogue-lines" class="dialogue-box"></div>
                            <button id="dialogue-audio-btn" class="audio-btn primary">🔊 Listen to Dialogue</button>
                        </div>

                        <!-- Right: Interactive Quiz -->
                        <div id="quiz-container" class="quiz-section"></div>
                    </div>
                </div>

            </div>
        </main>
    </div>
    <script src="script.js"></script>
</body>
</html>
"""

with open("a2b/index.html", "w", encoding="utf-8") as f:
    f.write(html_content.strip())
print("Created 'a2b/index.html'")
print("All a2b coursebook assets and source files generated successfully!")
