// Course Data Source
const courseData = {
    1: {
        num: "Unit 1",
        title: "People and Lifestyles",
        video_id: "51kO3-Jm5-s",
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
            { q: "What is the definition of 'routine'?", options: ["A sequence of actions regularly followed", "A type of vehicle", "A restaurant style", "A fast commute"], correct: 0 },
            { q: "What is the meaning of 'commute'?", options: ["To cook dinner at home", "To travel regularly to work or school", "To buy something quickly", "To live in a spacious house"], correct: 1 },
            { q: "What does 'spacious' mean?", options: ["Tiny and cramped", "Having ample space", "Very expensive", "Located in the city"], correct: 1 },
            { q: "What is the meaning of 'grab' in 'grab a coffee'?", options: ["To drop something", "To get or buy something quickly", "To throw away", "To make slowly"], correct: 1 },
            { q: "What is a 'diner'?", options: ["A large hotel", "A small, informal restaurant", "A private kitchen", "A train station"], correct: 1 },
            { q: "What does 'fast-paced' mean?", options: ["Slow and relaxed", "Moving or developing very quickly", "Quiet and silent", "Boring"], correct: 1 },
            { q: "Which word describes a house with lots of rooms and yard space?", options: ["Cramped", "Spacious", "Tiny", "Fast-paced"], correct: 1 },
            { q: "Which word means 'regularly traveling to work'?", options: ["Commute", "Grab", "Routine", "Diner"], correct: 0 },
            { q: "Which word means 'a sequence of daily habits'?", options: ["Diner", "Commute", "Routine", "Spacious"], correct: 2 },
            { q: "Complete: 'I usually _____ a quick snack at the corner shop.'", options: ["grab", "commute", "routine", "diner"], correct: 0 }
        ],
        conv_spot: {
            tiktok_id: "7181056586071854341",
            q: "In Vanessa's TikTok lesson, what daily action does she present?",
            options: ["How to order at a diner", "How to describe your morning commute", "How to wash dishes", "How to buy clothes"],
            correct: 0
        }
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
            { q: "What is the definition of 'destination'?", options: ["The starting point of a trip", "The place to which someone is going", "A type of vehicle", "A map outline"], correct: 1 },
            { q: "What is the meaning of 'encounter'?", options: ["To avoid completely", "To meet or run into unexpectedly", "To plan in advance", "To invite someone"], correct: 1 },
            { q: "What does 'unpredictable' mean?", options: ["Stable and certain", "Not able to be foreseen or known beforehand", "Very expensive", "Extremely hot"], correct: 1 },
            { word: "What is a 'redwood'?", options: ["A red flower", "A giant coniferous tree", "A small desert plant", "A type of rock"], correct: 1 },
            { q: "What is the meaning of 'waterfall'?", options: ["A dry riverbed", "A stream of water falling from a height", "A rain shower", "An indoor pool"], correct: 1 },
            { q: "What is the definition of 'hiking'?", options: ["Sailing on a boat", "Walking in nature, mountains, or forests", "Flying in a plane", "Sleeping in a hotel"], correct: 1 },
            { q: "Which word describes something that changes suddenly and cannot be guessed?", options: ["Predictable", "Unpredictable", "Spacious", "Fast-paced"], correct: 1 },
            { q: "Which word means 'meeting wild animals unexpectedly'?", options: ["Commuting", "Encountering", "Graduating", "Streaming"], correct: 1 },
            { q: "Which word means 'the final location of your vacation'?", options: ["Destination", "Routine", "Diner", "Ferry"], correct: 0 },
            { q: "Complete: 'We went _____ in the National Park last Sunday.'", options: ["hiking", "destination", "encounter", "redwood"], correct: 0 }
        ],
        conv_spot: {
            tiktok_id: "7215904562058775813",
            q: "What travel advice does Vanessa offer in this short lesson?",
            options: ["Useful travel phrases for asking directions", "How to pack a suitcase", "How to book a hotel room", "How to buy plane tickets"],
            correct: 0
        }
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
            { word: "Platform", def: "A digital system or software tool", ex: "We use a video call platform for classrooms." },
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
            { q: "What is a 'platform' in technology?", options: ["A train station floor", "A digital system or software tool", "A hardware cable", "A type of desk"], correct: 1 },
            { q: "What does 'wearable' mean?", options: ["Easy to wash", "A technological device worn on the body", "Heavy to carry", "Broken easily"], correct: 1 },
            { q: "What is an 'assistant' in 'smart assistant'?", options: ["A human secretary", "A device or software helper", "A computer repairman", "A retail clerk"], correct: 1 },
            { q: "What is the definition of 'remote' in 'remote work'?", options: ["Close by", "Distant, from a separate location", "Broken down", "Fast-paced"], correct: 1 },
            { q: "What does 'integrate' mean?", options: ["To separate into parts", "To combine or make part of a whole", "To delete permanently", "To buy online"], correct: 1 },
            { q: "What is the meaning of 'software'?", options: ["Physical computer parts", "Programs used by a computer", "Soft plastic accessories", "Digital screens"], correct: 1 },
            { q: "Which word means 'working from home or another distant location'?", options: ["Remote", "Spacious", "Severe", "Integrated"], correct: 0 },
            { q: "Which word describes a smartwatch or smart ring?", options: ["Wearable", "Software", "Diner", "Platform"], correct: 0 },
            { q: "Which word means 'combining different tools into one system'?", options: ["Separating", "Integrating", "Commuting", "Escaping"], correct: 1 },
            { q: "Complete: 'We updated the computer _____ yesterday.'", options: ["software", "remote", "wearable", "assistant"], correct: 0 }
        ],
        conv_spot: {
            tiktok_id: "7198503810011565318",
            q: "What is the main topic of Rachel's English technology lesson?",
            options: ["Pronouncing technology and software terms", "How to build a website", "How to repair a computer screen", "Using smart home gadgets"],
            correct: 0
        }
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
            { q: "What is a 'career'?", options: ["A hobby", "An occupation undertaken for a significant period", "A short vacation", "A school course"], correct: 1 },
            { q: "What does it mean to 'graduate'?", options: ["To start high school", "To complete a course of study at a school or college", "To fail an exam", "To look for a job"], correct: 1 },
            { q: "What is a 'sector'?", options: ["A small town", "A distinct part or branch of an economy", "A math equation", "A business partner"], correct: 1 },
            { q: "What is the definition of 'predict'?", options: ["To remember the past", "To say or estimate what will happen in the future", "To tell a joke", "To buy online"], correct: 1 },
            { q: "What does 'emerging' mean?", options: ["Disappearing completely", "Becoming apparent, important, or prominent", "Old and traditional", "Damaged"], correct: 1 },
            { q: "What is a 'business'?", options: ["A school campus", "An organization engaged in commercial activities", "A park area", "A government office"], correct: 1 },
            { q: "Which word means 'new industries that are growing quickly'?", options: ["Emerging", "Declining", "Traditional", "Spacious"], correct: 0 },
            { q: "Which word describes finishing college and receiving a degree?", options: ["Graduating", "Commuting", "Encoutering", "Reading"], correct: 0 },
            { q: "Which word means 'guessing what technology will look like in ten years'?", options: ["Remembering", "Predicting", "Integrating", "Achieving"], correct: 1 },
            { q: "Complete: 'He wants to have a successful _____ in medicine.'", options: ["career", "graduate", "sector", "predict"], correct: 0 }
        ],
        conv_spot: {
            tiktok_id: "7204005696030919941",
            q: "In this TikTok lesson, how does Vanessa explain talking about your future goals?",
            options: ["Using planned 'going to' structures naturally", "Discussing travel itineraries", "How to write a business resume", "How to order food"],
            correct: 0
        }
    },
    5: {
        num: "Unit 5",
        title: "Health and Wellness",
        video_id: "aPzY5_9zO2A",
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
            { q: "What is a 'symptom'?", options: ["A type of medicine", "A physical sign of an illness", "A healthy recipe", "A fitness workout"], correct: 1 },
            { q: "What does 'advise' mean?", options: ["To force someone to do something", "To offer suggestions about the best action", "To ignore warnings", "To get sick"], correct: 1 },
            { q: "What does 'severe' mean?", options: ["Mild and light", "Very intense, serious, or painful", "Cheap", "Fast-paced"], correct: 1 },
            { q: "What is the definition of a 'pill'?", options: ["A liquid syrup", "A small round piece of medicine to swallow", "A bandage", "A type of fruit"], correct: 1 },
            { q: "What does it mean to 'rest'?", options: ["To exercise heavily", "To relax, sleep, or recover strength", "To go to work", "To study all night"], correct: 1 },
            { q: "What is a 'fever'?", options: ["A common cold", "An abnormally high body temperature", "A muscle pain", "A stomach ache"], correct: 1 },
            { q: "Which word describes a very strong, painful headache?", options: ["Mild", "Severe", "Spacious", "Wearable"], correct: 1 },
            { q: "Which word means 'offering health recommendations'?", options: ["Advising", "Predicting", "Encountering", "Delivering"], correct: 0 },
            { q: "Which word means 'resting to recover from an illness'?", options: ["Commuting", "Resting", "Integrate", "Achieve"], correct: 1 },
            { q: "Complete: 'A cough is a typical _____ of a cold.'", options: ["symptom", "pill", "fever", "rest"], correct: 0 }
        ],
        conv_spot: {
            tiktok_id: "7181056586071854341",
            q: "What does the doctor advise the patient to do for their recovery?",
            options: ["rest for two days and drink warm tea", "exercise in the gym", "go to work", "go shopping"],
            correct: 0
        }
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
            { q: "What is 'ambition'?", options: ["A fear of failure", "A strong desire to achieve success", "A lazy attitude", "A university class"], correct: 1 },
            { q: "What does 'achieve' mean?", options: ["To give up on a task", "To reach or attain a goal by effort", "To start a new hobby", "To fail an exam"], correct: 1 },
            { q: "What does it mean to 'network'?", options: ["To watch television online", "To connect with people for career support", "To play computer games", "To work alone"], correct: 1 },
            { q: "What is the definition of an 'opportunity'?", options: ["A difficult problem", "A set of circumstances that makes it possible to do something", "A business loss", "A boring routine"], correct: 1 },
            { q: "What is a 'dream' in the context of ambitions?", options: ["Sleeping at night", "A cherished aspiration, ambition, or ideal", "A false story", "A past memory"], correct: 1 },
            { q: "What is 'success'?", options: ["A total failure", "The accomplishment of an aim or purpose", "A heavy workload", "A remote job"], correct: 1 },
            { q: "Which word describes having a strong drive to get a better job?", options: ["Spacious", "Ambition", "Restroom", "Fever"], correct: 1 },
            { q: "Which word means meeting professionals to help your career?", options: ["Networking", "Commuting", "Hiking", "Streaming"], correct: 0 },
            { q: "Which word means reaching your personal goals?", options: ["Achieving", "Encountering", "Predicting", "Advising"], correct: 0 },
            { q: "Complete: 'This internship is a wonderful _____ for your career.'", options: ["opportunity", "success", "dream", "network"], correct: 0 }
        ],
        conv_spot: {
            tiktok_id: "7218305695029013765",
            q: "Where would the speaker buy a house if they won the lottery?",
            options: ["St. John", "Seattle", "Florida", "California"],
            correct: 0
        }
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
            { q: "What is a 'consumer'?", options: ["A seller of goods", "A person who purchases goods and services", "A store manager", "A delivery driver"], correct: 1 },
            { q: "What does 'retail' mean?", options: ["Wholesale manufacturing", "The sale of goods to the public", "Trading stocks", "Importing goods"], correct: 1 },
            { q: "What is a 'transaction'?", options: ["A commercial advertisement", "An instance of buying or selling something", "A product return", "A shopping list"], correct: 1 },
            { q: "What is the definition of 'purchase'?", options: ["To sell at a loss", "To acquire something by paying money for it", "To rent temporarily", "To borrow money"], correct: 1 },
            { q: "What does it mean to 'deliver'?", options: ["To make products", "To bring and hand over letters, goods, or mail", "To throw away packages", "To buy items"], correct: 1 },
            { q: "What does it mean to 'process' a payment?", options: ["To cancel the order", "To perform systematic operations to handle it", "To pay in cash", "To delay shipment"], correct: 1 },
            { q: "Which word describes the final customer in an economy?", options: ["Seller", "Consumer", "Developer", "Historian"], correct: 1 },
            { q: "Which word refers to physical shopping stores open to the public?", options: ["Retail", "Platform", "Software", "Ferry"], correct: 0 },
            { q: "Which word means bringing a package to your front door?", options: ["Delivering", "Purchasing", "Commuting", "Encoutering"], correct: 0 },
            { q: "Complete: 'The bank approved the online credit card _____.'", options: ["transaction", "retail", "consumer", "deliver"], correct: 0 }
        ],
        conv_spot: {
            tiktok_id: "7223605698031021317",
            q: "When was the product in the dialogue purchased by the customer?",
            options: ["yesterday", "today", "last week", "one month ago"],
            correct: 0
        }
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
            { q: "What is 'streaming' in media?", options: ["Downloading files completely", "Transmitting or receiving data over the internet in real time", "A type of camera lens", "A film studio"], correct: 1 },
            { q: "What is a 'subscription'?", options: ["A one-time donation", "An agreement to pay recurringly for a service", "A free trial", "A user password"], correct: 1 },
            { q: "What is 'cable' in television context?", options: ["A wireless signal", "Traditional television transmission system", "A phone charger", "A streaming app"], correct: 1 },
            { q: "What is the definition of a 'documentary'?", options: ["A fictional action movie", "A movie or TV show documenting real facts", "A musical show", "A children's cartoon"], correct: 1 },
            { q: "Who are 'viewers'?", options: ["The actors in a show", "People who watch a television program or video", "The film directors", "Sound engineers"], correct: 1 },
            { q: "What does it mean to 'recommend'?", options: ["To criticize negatively", "To advise as being good or suitable", "To ignore a book", "To delete a show"], correct: 1 },
            { q: "Which word means paying a monthly fee for Netflix or Spotify?", options: ["Subscription", "Transaction", "Ambition", "Ferry"], correct: 0 },
            { q: "Which word describes a show about real space exploration history?", options: ["Documentary", "Redwood", "Diner", "Routine"], correct: 0 },
            { q: "Which word means watching a video live without downloading first?", options: ["Streaming", "Commuting", "Hiking", "Integrating"], correct: 0 },
            { q: "Complete: 'My friend _____ this movie, so I watched it.'", options: ["recommended", "streamed", "purchased", "delivered"], correct: 0 }
        ],
        conv_spot: {
            tiktok_id: "7228905691028019461",
            q: "Who is the actor that Friend A wants to know about?",
            options: ["the one who won the award last year", "the director of the movie", "the writer of the screenplay", "none"],
            correct: 0
        }
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
            { q: "What is 'fitness'?", options: ["A type of diet", "The condition of being physically fit and healthy", "A medical symptom", "A sleep disorder"], correct: 1 },
            { q: "What is a 'commitment'?", options: ["A broken promise", "The state or quality of being dedicated to a cause", "A casual suggestion", "A vacation plan"], correct: 1 },
            { q: "What is the definition of 'jogging'?", options: ["Sprinting at top speed", "Running at a gentle, slow pace", "Walking slowly", "Climbing stairs"], correct: 1 },
            { q: "What is the meaning of 'nutrition'?", options: ["Eating fast food", "Providing or obtaining the food necessary for health", "Diet pills", "Starving"], correct: 1 },
            { q: "What does it mean to 'stretch'?", options: ["To sit down on a sofa", "To straighten or extend one's body or limbs", "To lift heavy weights", "To run fast"], correct: 1 },
            { q: "What does 'avoid' mean?", options: ["To seek out actively", "To keep away from or stop doing something", "To enjoy doing", "To purchase online"], correct: 1 },
            { q: "Which word means staying dedicated to a daily workout routine?", options: ["Commitment", "Fever", "Routine", "Ambition"], correct: 0 },
            { q: "Which word refers to healthy eating habits and food science?", options: ["Nutrition", "Fitness", "Symptom", "Diner"], correct: 0 },
            { q: "Which word means running slowly in the park every morning?", options: ["Jogging", "Hiking", "Commuting", "Streaming"], correct: 0 },
            { q: "Complete: 'You should _____ eating heavy meals right before you sleep.'", options: ["avoid", "commit", "stretch", "jog"], correct: 0 }
        ],
        conv_spot: {
            tiktok_id: "7234205694030018821",
            q: "What does the runner prefer eating before their workout?",
            options: ["a banana", "a sandwich", "a pizza", "a cookie"],
            correct: 0
        }
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
            { q: "What are 'ruins'?", options: ["Brand new buildings", "The remains of a building or city that has suffered destruction", "Digital software tools", "Underground subways"], correct: 1 },
            { q: "What is an 'artifact'?", options: ["A modern smartphone", "An object made by a human being, typically of historical interest", "A heavy suitcase", "A new clothing item"], correct: 1 },
            { q: "What does 'excavate' mean?", options: ["To build a wall", "To make a hole or channel by digging", "To paint a picture", "To read historical books"], correct: 1 },
            { q: "What is a 'civilization'?", options: ["A small wild forest", "The stage of human social development and organization", "A private company", "A local community center"], correct: 1 },
            { q: "What is the definition of a 'mystery'?", options: ["A clear explanation", "Something that is difficult or impossible to understand or explain", "A historical timeline", "A school quiz"], correct: 1 },
            { q: "Who is a 'historian'?", options: ["A medical doctor", "An expert in or student of history", "A tour guide", "A video editor"], correct: 1 },
            { q: "Which word refers to ancient collapsed temples visited by tourists?", options: ["Ruins", "Malls", "Hospitals", "Dinners"], correct: 0 },
            { q: "Which word means digging into the earth to find ancient bones or objects?", options: ["Excavating", "Delivering", "Commuting", "Hiking"], correct: 0 },
            { q: "Which word describes a historical object like a 1000-year-old clay pot?", options: ["Artifact", "Symptom", "Ferry", "Redwood"], correct: 0 },
            { q: "Complete: 'The origin of the ancient gold coins remains a _____.'", options: ["mystery", "historian", "ruins", "excavate"], correct: 0 }
        ],
        conv_spot: {
            tiktok_id: "7239505697029019397",
            q: "Had they collected the artifacts before the museum opened?",
            options: ["yes, they had", "no, they hadn't", "they didn't collect any", "not mentioned"],
            correct: 0
        }
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

// Stop Audio
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
    document.getElementById('yt-iframe').src = `https://www.youtube.com/embed/${data.video_id}?rel=0&enablejsapi=1`;
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
            imgHtml = `<img src="images/unit5_home.png" alt="Spacious house illustration" style="width: 100%; height: 120px; object-fit: cover; border-radius: 8px; margin-bottom: 0.75rem;">`;
        } else if (unitId === 2 && index === 5) {
            imgHtml = `<img src="images/unit5_home.png" alt="Hiking beach illustration" style="width: 100%; height: 120px; object-fit: cover; border-radius: 8px; margin-bottom: 0.75rem;">`;
        } else if (unitId === 3 && index === 0) {
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

    // Load Conversation Spot TikTok Video & Exercise
    document.getElementById('conv-spot-iframe').src = `https://www.tiktok.com/player/v1/${data.conv_spot.tiktok_id}?music_info=0&description=0`;
    
    let convSpotHtml = `
        <div class="question-card" id="conv-spot-card">
            <div class="question-text">${data.conv_spot.q}</div>
            <div class="options-grid" style="margin-top: 1rem;">
    `;
    data.conv_spot.options.forEach((opt, optIndex) => {
        convSpotHtml += `
            <button class="option-btn" onclick="selectConvSpotOption(${optIndex}, this)">
                ${opt}
            </button>
        `;
    });
    convSpotHtml += `
            </div>
            <button class="submit-quiz-btn" style="margin-top: 1.5rem;" onclick="checkConvSpotAnswer()">Check Answer</button>
            <div id="conv-spot-feedback" class="feedback-msg"></div>
        </div>
    `;
    document.getElementById('conv-spot-exercise-container').innerHTML = convSpotHtml;
    
    // Reset workspace view to the first tab
    switchTab('tab-video');
}

// Select Quiz Option
let selectedAnswers = {};
function selectOption(qIndex, optIndex, btnElement) {
    const questionCard = btnElement.closest('.question-card');
    questionCard.querySelectorAll('.option-btn').forEach(btn => btn.classList.remove('selected'));
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
                btn.classList.add('correct');
            }
            if (selectedAnswers[qIndex] === optIndex && optIndex !== qData.correct) {
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
        markUnitCompleted(currentUnit);
    }
}

// Conversation Spot Selection & Answer checking
let selectedConvSpotAnswer = null;
function selectConvSpotOption(optIndex, btnElement) {
    const card = document.getElementById('conv-spot-card');
    card.querySelectorAll('.option-btn').forEach(btn => btn.classList.remove('selected'));
    btnElement.classList.add('selected');
    selectedConvSpotAnswer = optIndex;
}

function checkConvSpotAnswer() {
    const data = courseData[currentUnit];
    const card = document.getElementById('conv-spot-card');
    const buttons = card.querySelectorAll('.option-btn');
    const feedback = document.getElementById('conv-spot-feedback');
    
    if (selectedConvSpotAnswer === null) {
        feedback.style.color = '#dc2626';
        feedback.innerText = "Please select an answer first.";
        return;
    }
    
    buttons.forEach((btn, optIndex) => {
        btn.classList.remove('correct', 'incorrect');
        if (optIndex === data.conv_spot.correct) {
            btn.classList.add('correct');
        }
        if (selectedConvSpotAnswer === optIndex && optIndex !== data.conv_spot.correct) {
            btn.classList.add('incorrect');
        }
    });

    if (selectedConvSpotAnswer === data.conv_spot.correct) {
        feedback.style.color = '#059669';
        feedback.innerText = "Correct! Well done!";
    } else {
        feedback.style.color = '#dc2626';
        feedback.innerText = "Try again!";
    }
}

// Mark Unit as Completed
function markUnitCompleted(unitId) {
    completedUnits.add(unitId);
    const unitItem = document.querySelector(`.unit-item[onclick="loadUnit(${unitId})"]`);
    if (unitItem) {
        unitItem.classList.add('completed');
        unitItem.querySelector('.unit-status').innerHTML = '✓';
    }
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