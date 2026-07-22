import re

# Curated valid VOA Learning English videos that allow embedding
# We'll rotate these to ensure every unit has a working video
valid_yt_ids = [
    "MhCEdKIpwz4", # Lesson 1
    "G2sT23a07t8", # Lesson 2
    "a9Lw2cK6wZ8", # Lesson 3
    "9M7OqfE8WwY", # Lesson 4
    "xOcmG4H3K20", # Lesson 5
]

# Content definitions for Units 14 to 24
units_content = {
    14: {
        "title": "Unit 14: Health and the Body",
        "reading_title": "Staying Fit in America",
        "reading_text": "Staying active is very popular in the United States. Many Americans go jogging in the park or exercise at the gym. However, busy lifestyles can cause stress and health issues. When people feel sick, they should rest, drink water, or see a doctor for a prescription.",
        "dialogue": [
            ("Doctor", "Hello. What seems to be the problem today?"),
            ("Patient", "I feel terrible. I have a bad headache, a cough, and a sore throat."),
            ("Doctor", "Let me check... You have a fever. You should rest and take this medicine."),
            ("Patient", "Should I go to work tomorrow?"),
            ("Doctor", "No, you shouldn't go to work. You must rest at home.")
        ],
        "vocab": [
            ("Head", "The upper part of the body containing the brain", "I have got a hat on my head.", "head_icon"),
            ("Shoulder / Arm", "Upper body parts for lifting and carrying", "He has a pain in his shoulder.", "arm_icon"),
            ("Leg / Foot", "Lower body parts for walking and running", "She broke her leg skiing.", "leg_icon"),
            ("Stomach", "The organ where food goes after swallowing", "My stomach hurts today.", "stomach_icon"),
            ("Headache", "A continuous pain in the head", "I need aspirin for my headache.", "headache_icon"),
            ("Fever", "An abnormally high body temperature", "The child has got a high fever.", "fever_icon"),
            ("Medicine", "Substance used to treat disease", "You must take your medicine.", "medicine_icon")
        ],
        "grammar": {
            "title": "Modal Verb: Should / Shouldn't for Advice",
            "rules": [
                "<strong>Affirmative (+):</strong> Subject + should + verb (base form) — used to give good advice.",
                "<span class='grammar-example'>You should sleep 8 hours. She should see a doctor.</span>",
                "<strong>Negative (-):</strong> Subject + should not (shouldn't) + verb (base form) — used to advise against something.",
                "<span class='grammar-example'>You shouldn't drink cold water. He shouldn't go to work.</span>",
                "<strong>Questions (?):</strong> Should + subject + verb (base form)?",
                "<span class='grammar-example'>Should I take this medicine? Yes, you should. / No, you shouldn't.</span>"
            ],
            "audio": "You should sleep 8 hours. She should see a doctor. You shouldn't drink cold water. He shouldn't go to work. Should I take this medicine? Yes, you should. No, you shouldn't."
        },
        "listening": {
            "title": "Advice from the School Nurse",
            "audio": "Good morning. If you feel sick, you should come to my office. Today, many students have a cold. If you have a headache and a cough, you should rest. You shouldn't play outside in the cold weather. You should drink hot tea with honey, and you should sleep early tonight.",
            "transcript": "<strong>Nurse:</strong> Good morning. If you feel sick, you should come to my office. Today, many students have a cold. If you have a headache and a cough, you should rest. You shouldn't play outside in the cold weather. You should drink hot tea with honey, and you should sleep early tonight.",
            "questions": [
                "1. Many students have a cold today. _____ (True/False)",
                "2. Sick students should play outside. _____ (True/False)",
                "3. They should drink hot tea with honey. _____ (True/False)"
            ]
        },
        "speaking": {
            "title": "Giving Health Advice",
            "lines": [
                ("Student A", "I feel sick. My throat is sore and I have a headache."),
                ("Student B", "Oh, that's too bad. You should drink warm water."),
                ("Student A", "Should I go to the pharmacy?"),
                ("Student B", "Yes, you should get some cough medicine. And you shouldn't go running today.")
            ],
            "audio": "I feel sick. My throat is sore and I have a headache. Oh, that is too bad. You should drink warm water. Should I go to the pharmacy? Yes, you should get some cough medicine. And you shouldn't go running today."
        },
        "reading": {
            "title": "Healthy Habits",
            "text": "To have a healthy life, you should follow three simple rules. First, you should eat healthy food, like fruit and vegetables, and you shouldn't eat too much fast food. Second, you should exercise for 30 minutes every day. Walking in the park is great! Third, you should sleep 7 or 8 hours every night. Your body needs rest to stay strong.",
            "audio": "To have a healthy life, you should follow three simple rules. First, you should eat healthy food, like fruit and vegetables, and you shouldn't eat too much fast food. Second, you should exercise for 30 minutes every day. Walking in the park is great! Third, you should sleep 7 or 8 hours every night. Your body needs rest to stay strong."
        },
        "quiz": [
            ("u14q1", "You _____ stay at home if you have a high fever.", ["should", "shouldn't", "mustn't"], "should"),
            ("u14q2", "He has a bad cough, so he _____ drink ice water.", ["should", "shouldn't", "can"], "shouldn't")
        ]
    },
    15: {
        "title": "Unit 15: The Weather and Seasons",
        "reading_title": "Four Seasons in New England",
        "reading_text": "The northeast of the United States has four distinct seasons. Fall has beautiful red and gold leaves. Winter is very cold and snowy. Spring brings green trees, rain, and fresh flowers. Summer is hot and sunny, and many families go to the beach to swim and sunbathe.",
        "dialogue": [
            ("Alex", "What is the weather like today?"),
            ("Taylor", "It is raining and very windy. It is cold too!"),
            ("Alex", "Oh no! Let's stay inside and watch a movie."),
            ("Taylor", "Good idea. I hope it is sunny and warm tomorrow.")
        ],
        "vocab": [
            ("Winter", "The coldest season of the year", "It snows a lot in winter.", "winter_icon"),
            ("Spring", "The season when flowers start to grow", "It is usually rainy in spring.", "spring_icon"),
            ("Summer", "The hottest season of the year", "We go to the beach in summer.", "summer_icon"),
            ("Autumn / Fall", "The season when leaves change color", "Fall is my favorite season.", "fall_icon"),
            ("Sunny", "Bright with sunlight", "It is a sunny day, let's go out.", "sunny_icon"),
            ("Rainy", "Having a lot of rain", "Bring an umbrella, it is rainy.", "rainy_icon"),
            ("Snowy", "Covered with snow", "The mountains are snowy in January.", "snowy_icon"),
            ("Windy", "With a lot of wind", "It is very windy near the ocean.", "windy_icon")
        ],
        "grammar": {
            "title": "Describing Weather & Ongoing Activities",
            "rules": [
                "<strong>Weather state:</strong> It is + adjective (sunny / cloudy / windy / hot / cold / rainy / snowy).",
                "<span class='grammar-example'>It is sunny today. It was windy yesterday.</span>",
                "<strong>Ongoing weather actions:</strong> Present Continuous (It is raining / It is snowing).",
                "<span class='grammar-example'>Look outside! It is raining heavily. It isn't snowing now.</span>"
            ],
            "audio": "It is sunny today. It was windy yesterday. Look outside! It is raining heavily. It is not snowing now."
        },
        "listening": {
            "title": "A Weekend Weather Forecast",
            "audio": "Hello! Here is the weekend weather report. On Saturday morning, it is going to be cloudy but dry. In the afternoon, it will be sunny and warm, around 75 degrees. On Sunday, the weather is going to change. It is going to rain all day, and it is going to be very cold and windy.",
            "transcript": "<strong>Weather Presenter:</strong> Hello! Here is the weekend weather report. On Saturday morning, it's going to be cloudy but dry. In the afternoon, it will be sunny and warm, around 75 degrees. On Sunday, the weather is going to change. It's going to rain all day, and it's going to be very cold and windy.",
            "questions": [
                "1. What is the weather like on Saturday afternoon? _____ (Sunny/Rainy)",
                "2. Does it rain on Sunday? _____ (Yes/No)",
                "3. Is Sunday warm? _____ (Yes/No)"
            ]
        },
        "speaking": {
            "title": "Talking About Seasons",
            "lines": [
                ("Student A", "Which season do you like best?"),
                ("Student B", "I love summer because I can swim in the ocean. How about you?"),
                ("Student A", "I prefer autumn. The trees are beautiful and it isn't too hot."),
                ("Student B", "Is it rainy in autumn?"),
                ("Student A", "Sometimes, but it is usually windy and cool.")
            ],
            "audio": "Which season do you like best? I love summer because I can swim in the ocean. How about you? I prefer autumn. The trees are beautiful and it is not too hot. Is it rainy in autumn? Sometimes, but it is usually windy and cool."
        },
        "reading": {
            "title": "Weather Around the World",
            "text": "Weather is different in different parts of the world. In Chicago, winter is very cold and snowy. Temperatures can go below zero! But in Sydney, Australia, winter is mild and it never snows. Summer in Sydney is hot and sunny, while in Chicago, summer is warm but sometimes has big thunderstorms.",
            "audio": "Weather is different in different parts of the world. In Chicago, winter is very cold and snowy. Temperatures can go below zero! But in Sydney, Australia, winter is mild and it never snows. Summer in Sydney is hot and sunny, while in Chicago, summer is warm but sometimes has big thunderstorms."
        },
        "quiz": [
            ("u15q1", "Look! It _____ outside. We need an umbrella.", ["rains", "is raining", "snows"], "is raining"),
            ("u15q2", "My favorite season is _____ because I love the snow.", ["summer", "spring", "winter"], "winter")
        ]
    },
    16: {
        "title": "Unit 16: Life Experiences",
        "reading_title": "American Road Trips",
        "reading_text": "Many Americans love traveling across the country. They have visited national parks like the Grand Canyon or Yosemite. Road trips are a traditional way to see different states, eat local food, and make unforgettable memories with friends and family.",
        "dialogue": [
            ("Mark", "Have you ever traveled to another country?"),
            ("Sophia", "Yes, I have. I have been to Mexico and Canada. How about you?"),
            ("Mark", "I have never left the United States. But I have visited 15 states!"),
            ("Sophia", "That's cool! Have you ever seen the Grand Canyon?"),
            ("Mark", "No, I haven't. But I want to go next summer.")
        ],
        "vocab": [
            ("Visit", "To go to see a place or person", "I have visited many museums.", "visit_icon"),
            ("Travel", "To make a journey to a distant place", "She has traveled by train across Italy.", "travel_icon"),
            ("Eat sushi", "To eat Japanese raw fish dish", "Have you ever eaten sushi?", "sushi_icon"),
            ("Climb a mountain", "To walk up a high mountain", "He has climbed Mount Rainier.", "climb_icon"),
            ("Fly", "To travel through the air in an airplane", "We have flown in a small helicopter.", "fly_icon"),
            ("Swim in the ocean", "To swim in the sea", "I have swum with dolphins.", "swim_icon")
        ],
        "grammar": {
            "title": "Present Perfect for Life Experiences",
            "rules": [
                "<strong>Affirmative (+):</strong> Subject + have/has + past participle. (Note: regular verbs add -ed; irregulars change).",
                "<span class='grammar-example'>I have eaten sushi. He has visited New York.</span>",
                "<strong>Negative (-):</strong> Subject + haven't/hasn't + past participle (or use 'never').",
                "<span class='grammar-example'>She hasn't seen the movie. I have never flown in a helicopter.</span>",
                "<strong>Questions (?):</strong> Have/Has + subject + past participle?",
                "<span class='grammar-example'>Have you ever climbed a mountain? Yes, I have. / No, I haven't.</span>"
            ],
            "audio": "I have eaten sushi. He has visited New York. She has not seen the movie. I have never flown in a helicopter. Have you ever climbed a mountain? Yes, I have. No, I have not."
        },
        "listening": {
            "title": "Checking the Bucket List",
            "audio": "Have you ever done something exciting, Tom? Yes! I have climbed a high mountain, and I have swum in the Pacific Ocean. Have you ever eaten something unusual? Well, I have eaten octopus in Spain, but I have never eaten raw fish. How about you, Lisa? I have never eaten octopus, but I eat sushi every week!",
            "transcript": "<strong>Lisa:</strong> Have you ever done something exciting, Tom? <br><strong>Tom:</strong> Yes! I have climbed a high mountain, and I have swum in the Pacific Ocean. Have you ever eaten something unusual? <br><strong>Lisa:</strong> Well, I have eaten octopus in Spain, but I have never eaten raw fish. How about you, Lisa? <br><strong>Tom:</strong> I have never eaten octopus, but I eat sushi every week!",
            "questions": [
                "1. Tom has swum in the Pacific Ocean. _____ (True/False)",
                "2. Tom has eaten raw fish. _____ (True/False)",
                "3. Lisa eats sushi every week. _____ (True/False)"
            ]
        },
        "speaking": {
            "title": "Asking About Experiences",
            "lines": [
                ("Student A", "Have you ever swum in a lake?"),
                ("Student B", "Yes, I have. I swam in Lake Michigan last summer. Have you ever traveled by boat?"),
                ("Student A", "No, I haven't. I'm afraid of deep water!"),
                ("Student B", "Don't worry, it's very safe and fun!")
            ],
            "audio": "Have you ever swum in a lake? Yes, I have. I swam in Lake Michigan last summer. Have you ever traveled by boat? No, I have not. I am afraid of deep water! Do not worry, it is very safe and fun!"
        },
        "reading": {
            "title": "An Adventurous Life",
            "text": "My grandmother is 75 years old, but she has had an adventurous life. She has traveled to 30 countries. She has walked on the Great Wall of China, she has seen the Pyramids in Egypt, and she has ridden a camel in the desert. She has never stopped learning. She says: 'Life is a beautiful journey!'",
            "audio": "My grandmother is 75 years old, but she has had an adventurous life. She has traveled to 30 countries. She has walked on the Great Wall of China, she has seen the Pyramids in Egypt, and she has ridden a camel in the desert. She has never stopped learning. She says: Life is a beautiful journey!"
        },
        "quiz": [
            ("u16q1", "She _____ never flown in a helicopter.", ["have", "has", "is"], "has"),
            ("u16q2", "Have you ever _____ octopus?", ["eat", "ate", "eaten"], "eaten")
        ]
    },
    17: {
        "title": "Unit 17: Rules and Obligations",
        "reading_title": "School Rules in the USA",
        "reading_text": "American schools have clear rules to keep students safe. Students must arrive on time for classes. They must respect their teachers and classmates. In most public schools, students don't have to wear uniforms, but they must follow a dress code.",
        "dialogue": [
            ("Teacher", "Remember class, you must turn off your mobile phones during the test."),
            ("Student", "Can we use our dictionaries?"),
            ("Teacher", "No, you mustn't use dictionaries. It is against the rules."),
            ("Student", "Do we have to write in ink?"),
            ("Teacher", "No, you don't have to write in ink. You can use a pencil.")
        ],
        "vocab": [
            ("Must", "To be required to do something by rule", "You must wear a seatbelt in the car.", "must_icon"),
            ("Mustn't", "To be prohibited from doing something", "You mustn't smoke in the hospital.", "mustnt_icon"),
            ("Have to", "To be necessary to do due to circumstances", "I have to wash the dishes tonight.", "haveto_icon"),
            ("Don't have to", "Not necessary, optional", "We don't have to work on Sunday.", "donthaveto_icon"),
            ("Arrive on time", "To arrive at the correct scheduled time", "You must arrive on time for school.", "ontime_icon"),
            ("Wear a uniform", "To wear matching clothing required by school/work", "In some schools, they have to wear uniforms.", "uniform_icon")
        ],
        "grammar": {
            "title": "Obligation & Prohibition: Must, Mustn't, Have to, Don't have to",
            "rules": [
                "<strong>Must / Have to:</strong> Used for strong obligations and rules.",
                "<span class='grammar-example'>You must stop at a red light. I have to study for my test.</span>",
                "<strong>Mustn't:</strong> Used for prohibitions (things that are not allowed).",
                "<span class='grammar-example'>You mustn't park here. Students mustn't talk during the exam.</span>",
                "<strong>Don't have to:</strong> Used for things that are NOT necessary (optional).",
                "<span class='grammar-example'>Tomorrow is a holiday, so we don't have to get up early.</span>"
            ],
            "audio": "You must stop at a red light. I have to study for my test. You mustn't park here. Students mustn't talk during the exam. Tomorrow is a holiday, so we don't have to get up early."
        },
        "listening": {
            "title": "Library Rules",
            "audio": "Welcome to the city library. Please remember these rules. First, you must keep quiet. You mustn't speak loudly on your phone. Second, you don't have to pay to read books here, it is free. However, you must return the books on time. Finally, you mustn't eat food inside the library, but you can drink bottled water.",
            "transcript": "<strong>Librarian:</strong> Welcome to the city library. Please remember these rules. First, you must keep quiet. You mustn't speak loudly on your phone. Second, you don't have to pay to read books here, it is free. However, you must return the books on time. Finally, you mustn't eat food inside the library, but you can drink bottled water.",
            "questions": [
                "1. You must keep quiet in the library. _____ (True/False)",
                "2. You have to pay money to read books. _____ (True/False)",
                "3. You mustn't eat food inside. _____ (True/False)"
            ]
        },
        "speaking": {
            "title": "Discussing School Rules",
            "lines": [
                ("Student A", "Do we have to bring our laptops tomorrow?"),
                ("Student B", "No, we don't have to bring them. The teacher has got tablets for us."),
                ("Student A", "Great. Can we eat snacks in class?"),
                ("Student B", "No, we mustn't eat in the classroom. We must eat in the cafeteria.")
            ],
            "audio": "Do we have to bring our laptops tomorrow? No, we don't have to bring them. The teacher has got tablets for us. Great. Can we eat snacks in class? No, we mustn't eat in the classroom. We must eat in the cafeteria."
        },
        "reading": {
            "title": "Rules at the National Park",
            "text": "When you visit Yosemite National Park, you must follow the rules to protect nature. You mustn't feed the wild animals, because it is dangerous for them. You must put all your trash in special bear-proof bins. You don't have to stay in a hotel; you can camp in the forest, but you must get a camping permit first.",
            "audio": "When you visit Yosemite National Park, you must follow the rules to protect nature. You mustn't feed the wild animals, because it is dangerous for them. You must put all your trash in special bear-proof bins. You don't have to stay in a hotel; you can camp in the forest, but you must get a camping permit first."
        },
        "quiz": [
            ("u17q1", "You _____ touch that wire. It is extremely dangerous.", ["must", "mustn't", "don't have to"], "mustn't"),
            ("u17q2", "Tomorrow is Sunday, so I _____ go to work.", ["must", "mustn't", "don't have to"], "don't have to")
        ]
    },
    18: {
        "title": "Unit 18: Making Comparisons",
        "reading_title": "City Life vs. Country Life",
        "reading_text": "In the United States, lifestyles vary. Some Americans prefer living in big cities like New York because it is faster and more exciting. Others prefer quiet country towns. Country life is usually cheaper, safer, and cleaner, but it can be much slower and less convenient.",
        "dialogue": [
            ("John", "Which city do you prefer, Boston or Chicago?"),
            ("David", "I prefer Boston. It is smaller and cleaner than Chicago."),
            ("John", "Yes, but Chicago is more exciting and has better museums!"),
            ("David", "True, but Chicago is also much more expensive and noisier.")
        ],
        "vocab": [
            ("Bigger / Smaller", "Comparative size descriptors", "My room is bigger than yours.", "size_icon"),
            ("Faster / Slower", "Comparative speed descriptors", "Trains are faster than buses.", "speed_icon"),
            ("Cheaper / More expensive", "Comparative cost descriptors", "This shirt is cheaper than that jacket.", "cost_icon"),
            ("Cleaner / Dirtier", "Comparative cleanliness descriptors", "The country is cleaner than the city.", "clean_icon"),
            ("More exciting", "Creating a high level of interest or enthusiasm", "New York is more exciting than Boston.", "excite_icon"),
            ("Better / Worse", "Irregular comparative descriptors of quality", "My English is better now.", "quality_icon")
        ],
        "grammar": {
            "title": "Comparative Adjectives",
            "rules": [
                "<strong>Short Adjectives:</strong> Add -er (e.g. big → bigger, cheap → cheaper, dry → drier). Use 'than' to compare.",
                "<span class='grammar-example'>A car is faster than a bicycle. The library is quieter than the cafe.</span>",
                "<strong>Long Adjectives:</strong> Use 'more' + adjective (e.g. expensive → more expensive, beautiful → more beautiful).",
                "<span class='grammar-example'>This watch is more expensive than that phone.</span>",
                "<strong>Irregular Comparatives:</strong> good → better, bad → worse, far → farther/further.",
                "<span class='grammar-example'>Fruits are better for you than sweets.</span>"
            ],
            "audio": "A car is faster than a bicycle. The library is quieter than the cafe. This watch is more expensive than that phone. Fruits are better for you than sweets."
        },
        "listening": {
            "title": "Buying a New Smartphone",
            "audio": "Hi, can I help you? Yes, I want a new phone. I like this red one and this silver one. The red phone is newer and faster, but it is more expensive. How much is the silver one? The silver phone is cheaper and smaller, but its screen is worse. I see. I think I will buy the red one because speed is important to me.",
            "transcript": "<strong>Salesperson:</strong> Hi, can I help you? <br><strong>Customer:</strong> Yes, I want a new phone. I like this red one and this silver one. <br><strong>Salesperson:</strong> The red phone is newer and faster, but it is more expensive. <br><strong>Customer:</strong> How much is the silver one? <br><strong>Salesperson:</strong> The silver phone is cheaper and smaller, but its screen is worse. <br><strong>Customer:</strong> I see. I think I will buy the red one because speed is important to me.",
            "questions": [
                "1. The red phone is cheaper than the silver one. _____ (True/False)",
                "2. The silver phone is smaller. _____ (True/False)",
                "3. The red phone is faster. _____ (True/False)"
            ]
        },
        "speaking": {
            "title": "Comparing Two Cities",
            "lines": [
                ("Student A", "Is your hometown bigger than this city?"),
                ("Student B", "No, it's much smaller. It's also quieter and cleaner."),
                ("Student A", "Which one is more expensive?"),
                ("Student B", "This city is definitely more expensive. Food and rent are much higher here.")
            ],
            "audio": "Is your hometown bigger than this city? No, it's much smaller. It's also quieter and cleaner. Which one is more expensive? This city is definitely more expensive. Food and rent are much higher here."
        },
        "reading": {
            "title": "Two Different Cars",
            "text": "Mr. Smith has got two cars. The first is an old family station wagon. It is slow, heavy, and ugly, but it is very comfortable and safe. The second is a new electric sports car. It is much faster, smaller, and more beautiful, but it is also more expensive to repair. Mr. Smith uses the sports car for work and the station wagon for family trips.",
            "audio": "Mr. Smith has got two cars. The first is an old family station wagon. It is slow, heavy, and ugly, but it is very comfortable and safe. The second is a new electric sports car. It is much faster, smaller, and more beautiful, but it is also more expensive to repair. Mr. Smith uses the sports car for work and the station wagon for family trips."
        },
        "quiz": [
            ("u18q1", "My new apartment is _____ than my old one.", ["big", "bigger", "more big"], "bigger"),
            ("u18q2", "Traveling by plane is _____ than traveling by bus.", ["expensive", "more expensive", "expensiver"], "more expensive")
        ]
    },
    19: {
        "title": "Unit 19: The Best in the World",
        "reading_title": "Famous American Landmarks",
        "reading_text": "The United States is home to some of the world's most famous extremes. Death Valley in California is the hottest and driest place in North America. Alaska is the biggest and coldest state, and Hawaii is the newest and most tropical state.",
        "dialogue": [
            ("Emily", "What is the tallest building in New York City?"),
            ("Daniel", "One World Trade Center is the tallest. It is beautiful!"),
            ("Emily", "And what is the most famous park?"),
            ("Daniel", "Central Park, of course! It is the most popular park in the United States.")
        ],
        "vocab": [
            ("Tallest / Shortest", "Extreme height descriptors", "He is the tallest student in class.", "height_icon"),
            ("Biggest / Smallest", "Extreme size descriptors", "Russia is the biggest country.", "size_icon"),
            ("Hottest / Coldest", "Extreme temperature descriptors", "July is the hottest month here.", "temp_icon"),
            ("Most expensive", "Highest cost of all", "This is the most expensive restaurant.", "expensive_icon"),
            ("Most beautiful", "Highest aesthetic value", "She visited the most beautiful lake.", "beauty_icon"),
            ("Best / Worst", "Irregular superlative quality descriptors", "That was the best day of my life.", "quality_icon")
        ],
        "grammar": {
            "title": "Superlative Adjectives",
            "rules": [
                "Use superlatives to compare three or more things and identify the extreme one. Always use 'the'.",
                "<strong>Short Adjectives:</strong> Add -est (e.g. big → the biggest, cheap → the cheapest, cold → the coldest).",
                "<span class='grammar-example'>Mount Everest is the highest mountain in the world.</span>",
                "<strong>Long Adjectives:</strong> Use 'the most' + adjective (e.g. popular → the most popular).",
                "<span class='grammar-example'>This is the most interesting book in the library.</span>",
                "<strong>Irregular Superlatives:</strong> good → the best, bad → the worst, far → the farthest."
            ],
            "audio": "Mount Everest is the highest mountain in the world. This is the most interesting book in the library. Russia is the biggest country. That was the best day of my life."
        },
        "listening": {
            "title": "Quiz Night at the Cafe",
            "audio": "Welcome to Quiz Night! Here are three questions. Question one: What is the biggest animal in the world? The blue whale is the biggest animal. Correct! Question two: What is the hottest place in North America? Death Valley is the hottest. Correct! Question three: What is the most expensive city in the world? It is Singapore. Yes, you win first prize!",
            "transcript": "<strong>Host:</strong> Welcome to Quiz Night! Here are three questions. <br><strong>Host:</strong> Question one: What is the biggest animal in the world? <br><strong>Player:</strong> The blue whale is the biggest animal. <br><strong>Host:</strong> Correct! Question two: What is the hottest place in North America? <br><strong>Player:</strong> Death Valley is the hottest. <br><strong>Host:</strong> Correct! Question three: What is the most expensive city in the world? <br><strong>Player:</strong> It is Singapore. <br><strong>Host:</strong> Yes, you win first prize!",
            "questions": [
                "1. The blue whale is the biggest animal in the world. _____ (True/False)",
                "2. Death Valley is the coldest place. _____ (True/False)",
                "3. Singapore is the most expensive city. _____ (True/False)"
            ]
        },
        "speaking": {
            "title": "Asking About Records",
            "lines": [
                ("Student A", "Who is the tallest person in your family?"),
                ("Student B", "My father is the tallest. He is 6 feet 3 inches. Who is the best singer?"),
                ("Student A", "My sister is the best singer. She sings in a choir. What was the worst movie you saw?"),
                ("Student B", "I saw a horror movie last month. It was the worst movie ever!")
            ],
            "audio": "Who is the tallest person in your family? My father is the tallest. He is 6 feet 3 inches. Who is the best singer? My sister is the best singer. She sings in a choir. What was the worst movie you saw? I saw a horror movie last month. It was the worst movie ever!"
        },
        "reading": {
            "title": "Extreme Places on Earth",
            "text": "Our planet has got some amazing places. The Sahara is the biggest hot desert, but Antarctica is the largest and coldest desert of all. The wettest place on Earth is Mawsynram in India, where it rains almost every day. The deepest part of the ocean is the Mariana Trench, which is deeper than Mount Everest is tall!",
            "audio": "Our planet has got some amazing places. The Sahara is the biggest hot desert, but Antarctica is the largest and coldest desert of all. The wettest place on Earth is Mawsynram in India, where it rains almost every day. The deepest part of the ocean is the Mariana Trench, which is deeper than Mount Everest is tall!"
        },
        "quiz": [
            ("u19q1", "This is the _____ cake I have ever eaten! Delicious!", ["best", "better", "goodest"], "best"),
            ("u19q2", "Tokyo is the _____ city in the world, with 37 million people.", ["bigger", "biggest", "most big"], "biggest")
        ]
    },
    20: {
        "title": "Unit 20: Future Predictions",
        "reading_title": "Smart Cities of Tomorrow",
        "reading_text": "Technology is changing our world rapidly. Experts predict that cities in the future will be smart and clean. We will use electric self-driving vehicles, and robots will perform dangerous tasks. We won't use fossil fuels, which will make the air cleaner.",
        "dialogue": [
            ("Alex", "Do you think we will have flying cars in 2050?"),
            ("Jordan", "Yes, I think we will. Technology is growing very fast."),
            ("Alex", "Will robots do all the housework?"),
            ("Jordan", "Yes, they will. We won't need to clean or cook anymore!"),
            ("Alex", "That sounds perfect. I will buy a robot immediately.")
        ],
        "vocab": [
            ("Will / Won't", "Auxiliaries for future prediction", "I think it will rain tomorrow.", "will_icon"),
            ("Predict", "To say what will happen in the future", "Scientists predict hot summers.", "predict_icon"),
            ("Robot", "A machine that can execute complex actions", "Robots will clean our houses.", "robot_icon"),
            ("Self-driving car", "A vehicle that drives itself", "We will travel in self-driving cars.", "car_icon"),
            ("Space travel", "Traveling into outer space", "Space travel will be cheap.", "space_icon"),
            ("Clean energy", "Energy that does not pollute", "We will use solar energy in the future.", "energy_icon")
        ],
        "grammar": {
            "title": "Future Predictions with Will and Won't",
            "rules": [
                "Use 'will' (affirmative) and 'won't' (negative) + verb (base form) to make predictions about the future.",
                "<strong>Affirmative (+):</strong> Subject + will ('ll) + verb.",
                "<span class='grammar-example'>People will live on Mars. It will be hot tomorrow.</span>",
                "<strong>Negative (-):</strong> Subject + will not (won't) + verb.",
                "<span class='grammar-example'>We won't use paper money. Cars won't need petrol.</span>",
                "<strong>Questions (?):</strong> Will + subject + verb?",
                "<span class='grammar-example'>Will robots speak English? Yes, they will. / No, they won't.</span>"
            ],
            "audio": "People will live on Mars. It will be hot tomorrow. We won't use paper money. Cars won't need petrol. Will robots speak English? Yes, they will. No, they won't."
        },
        "listening": {
            "title": "A Vision of 2050",
            "audio": "In the year 2050, the world will be very different. We won't drive petrol cars anymore. Everyone will use electric flying cars. AI assistants will do all the difficult office work, so people will have more free time. We will travel to the moon for holidays, and we will live longer, healthier lives.",
            "transcript": "<strong>Speaker:</strong> In the year 2050, the world will be very different. We won't drive petrol cars anymore. Everyone will use electric flying cars. AI assistants will do all the difficult office work, so people will have more free time. We will travel to the moon for holidays, and we will live longer, healthier lives.",
            "questions": [
                "1. People will drive petrol cars in 2050. _____ (True/False)",
                "2. AI assistants will do office work. _____ (True/False)",
                "3. People will go to the moon for holidays. _____ (True/False)"
            ]
        },
        "speaking": {
            "title": "Predicting the Future",
            "lines": [
                ("Student A", "Do you think smartphones will disappear?"),
                ("Student B", "Yes, I do. I think we will have smart glasses instead. What do you think?"),
                ("Student A", "I agree. And we won't write with pens anymore, we will just speak to our screens."),
                ("Student B", "That's exciting!")
            ],
            "audio": "Do you think smartphones will disappear? Yes, I do. I think we will have smart glasses instead. What do you think? I agree. And we won't write with pens anymore, we will just speak to our screens. That's exciting!"
        },
        "reading": {
            "title": "The Future of Education",
            "text": "Education will change a lot in the next thirty years. Students won't go to traditional school buildings every day. Instead, they will study at home using virtual reality headsets. They will have personal AI tutors that will explain difficult topics. Exams will be different too; they will test skills, not just memory.",
            "audio": "Education will change a lot in the next thirty years. Students won't go to traditional school buildings every day. Instead, they will study at home using virtual reality headsets. They will have personal AI tutors that will explain difficult topics. Exams will be different too; they will test skills, not just memory."
        },
        "quiz": [
            ("u20q1", "I think people _____ live on the moon one day.", ["will", "won't", "are"], "will"),
            ("u20q2", "In the future, we _____ use petrol because clean energy will be cheap.", ["will", "won't", "don't"], "won't")
        ]
    },
    21: {
        "title": "Unit 21: Polite Requests and Offers",
        "reading_title": "Tipping and Restaurant Etiquette",
        "reading_text": "In the United States, good service is highly valued. Customers use polite requests like 'could I have' or 'would you mind'. At the end of the meal, it is customary to leave a tip of 15% to 20% of the bill to show appreciation to the waiter.",
        "dialogue": [
            ("Waiter", "Good evening. Are you ready to order?"),
            ("Customer", "Yes, could I have the chicken salad, please?"),
            ("Waiter", "Certainly. And what would you like to drink?"),
            ("Customer", "Could I get a glass of sparkling water, please?"),
            ("Waiter", "Of course. Would you like a menu for dessert later?"),
            ("Customer", "No, thank you. Just the bill, please.")
        ],
        "vocab": [
            ("Polite request", "Asking for something in a nice way", "Could I have some water, please?", "polite_icon"),
            ("Bill / Check", "The paper showing how much to pay", "Could we have the bill, please?", "bill_icon"),
            ("Menu", "A list of food items and prices", "Could I see the wine menu?", "menu_icon"),
            ("Can / Could I", "Phrases for making polite requests", "Could I borrow your pen?", "could_icon"),
            ("Would you like", "Phrase for making polite offers", "Would you like some tea?", "would_icon"),
            ("Shall I", "Phrase for offering help", "Shall I carry your heavy suitcase?", "shall_icon")
        ],
        "grammar": {
            "title": "Polite Requests & Offers",
            "rules": [
                "<strong>Polite Requests:</strong> Use 'Could I have / Could you / Can I have...' + please.",
                "<span class='grammar-example'>Could I have some water, please? Could you open the window, please?</span>",
                "<strong>Polite Offers:</strong> Use 'Would you like...?' or 'Can I / Shall I...?'",
                "<span class='grammar-example'>Would you like some coffee? Shall I help you with your bags?</span>",
                "<strong>Replying:</strong> Yes, please. / No, thank you. / Of course. / Sure."
            ],
            "audio": "Could I have some water, please? Could you open the window, please? Would you like some coffee? Shall I help you with your bags? Yes, please. No, thank you."
        },
        "listening": {
            "title": "At the Hotel Front Desk",
            "audio": "Good afternoon, sir. Can I help you? Yes, please. Could I check in? Yes, of course. Could you write your name and address here, please? Yes, sure. Here is your key card, room 305. Would you like some help with your luggage? Yes, please. That would be very nice. Shall I call a taxi for you? No, thank you.",
            "transcript": "<strong>Receptionist:</strong> Good afternoon, sir. Can I help you? <br><strong>Guest:</strong> Yes, please. Could I check in? <br><strong>Receptionist:</strong> Yes, of course. Could you write your name and address here, please? <br><strong>Guest:</strong> Yes, sure. Here is your key card, room 305. Would you like some help with your luggage? <br><strong>Guest:</strong> Yes, please. That would be very nice. <br><strong>Receptionist:</strong> Shall I call a taxi for you? <br><strong>Guest:</strong> No, thank you.",
            "questions": [
                "1. The guest is checking into room 305. _____ (True/False)",
                "2. The receptionist offers to help with luggage. _____ (True/False)",
                "3. The guest wants a taxi now. _____ (True/False)"
            ]
        },
        "speaking": {
            "title": "Ordering at a Cafe",
            "lines": [
                ("Waiter", "Hi, what can I get for you today?"),
                ("Customer", "Hello. Could I have a large cappuccino and a slice of chocolate cake?"),
                ("Waiter", "Sure. Would you like chocolate sprinkles on your cappuccino?"),
                ("Customer", "Yes, please. And could I get a cup of water too?")
            ],
            "audio": "Hi, what can I get for you today? Hello. Could I have a large cappuccino and a slice of chocolate cake? Sure. Would you like chocolate sprinkles on your cappuccino? Yes, please. And could I get a cup of water too?"
        },
        "reading": {
            "title": "Being Polite in English",
            "text": "When you visit an English-speaking country, using polite language is very important. Instead of saying 'Give me a coffee', you should say 'Could I have a coffee, please?'. Waiters, shop assistants, and taxi drivers appreciate polite customers. If someone offers you help, you should say 'Thank you, that's very kind of you'.",
            "audio": "When you visit an English-speaking country, using polite language is very important. Instead of saying 'Give me a coffee', you should say 'Could I have a coffee, please?'. Waiters, shop assistants, and taxi drivers appreciate polite customers. If someone offers you help, you should say 'Thank you, that's very kind of you'."
        },
        "quiz": [
            ("u21q1", "_____ I have the bill, please?", ["Could", "Do", "Would"], "Could"),
            ("u21q2", "_____ you like some sugar in your tea?", ["Could", "Would", "Shall"], "Would")
        ]
    },
    22: {
        "title": "Unit 22: Feelings and Emotions",
        "reading_title": "Mental Wellness in America",
        "reading_text": "Talking about emotions is very common in the United States. Many Americans share their feelings openly with friends, family, or counselors. People often practice exercises, jog, or walk in nature because it helps them feel happy and reduces anxiety.",
        "dialogue": [
            ("Sam", "Are you okay, Jessica? You look worried."),
            ("Jessica", "I am very nervous because I have a big English exam tomorrow."),
            ("Sam", "Don't worry, you studied hard, so you will pass!"),
            ("Jessica", "Thanks, Sam. I feel a bit better now."),
            ("Sam", "Great! Let's get a coffee so you can relax.")
        ],
        "vocab": [
            ("Happy", "Feeling or showing pleasure or contentment", "She was happy because she won.", "happy_icon"),
            ("Sad", "Feeling or showing sorrow; unhappy", "He felt sad when his dog died.", "sad_icon"),
            ("Tired", "In need of sleep or rest; weary", "I am tired after the long run.", "tired_icon"),
            ("Nervous / Worried", "Anxious or uneasy about something", "She is nervous about the interview.", "nervous_icon"),
            ("Excited", "Very happy and enthusiastic", "They are excited about the holiday.", "excited_icon"),
            ("Angry", "Feeling or showing strong annoyance or hostility", "The teacher was angry with the class.", "angry_icon")
        ],
        "grammar": {
            "title": "Conjunctions: Because & So",
            "rules": [
                "<strong>Because:</strong> Used to give a reason.",
                "<span class='grammar-example'>I went to bed early because I was tired. She is happy because she passed.</span>",
                "<strong>So:</strong> Used to express a result.",
                "<span class='grammar-example'>I was tired, so I went to bed early. She passed the test, so she is happy.</span>",
                "<strong>Contrast:</strong> 'Because' introduces the cause; 'So' introduces the effect."
            ],
            "audio": "I went to bed early because I was tired. She is happy because she passed. I was tired, so I went to bed early. She passed the test, so she is happy."
        },
        "listening": {
            "title": "Checking in on Friends",
            "audio": "Hi, Leo. You look very happy today! Yes, I am excited because my parents bought me a new laptop! Wow, that's awesome. Why does Lucas look so sad? Well, he lost his wallet yesterday, so he is very worried. Oh, that's terrible. Shall we buy him a coffee to make him feel better?",
            "transcript": "<strong>Anna:</strong> Hi, Leo. You look very happy today! <br><strong>Leo:</strong> Yes, I am excited because my parents bought me a new laptop! <br><strong>Anna:</strong> Wow, that's awesome. Why does Lucas look so sad? <br><strong>Leo:</strong> Well, he lost his wallet yesterday, so he is very worried. <br><strong>Anna:</strong> Oh, that's terrible. Shall we buy him a coffee to make him feel better?",
            "questions": [
                "1. Leo is happy because he has a new computer. _____ (True/False)",
                "2. Lucas is worried because he lost his keys. _____ (True/False)",
                "3. Anna wants to buy Lucas a coffee. _____ (True/False)"
            ]
        },
        "speaking": {
            "title": "How Do You Feel?",
            "lines": [
                ("Student A", "How do you feel today?"),
                ("Student B", "I feel a bit tired because I didn't sleep well last night. What about you?"),
                ("Student A", "I'm very excited! I'm going to a concert tonight, so I'm very happy."),
                ("Student B", "That's great! Have a wonderful time!")
            ],
            "audio": "How do you feel today? I feel a bit tired because I didn't sleep well last night. What about you? I'm very excited! I'm going to a concert tonight, so I'm very happy. That's great! Have a wonderful time!"
        },
        "reading": {
            "title": "Understanding Our Feelings",
            "text": "Feelings are a natural part of life. Everyone feels sad, nervous, or angry sometimes. When you feel worried, you should talk to someone you trust. Exercising is also a good idea because it makes your body release happy chemicals. Eating healthy food and sleeping well are important, so you should take care of your body to help your mind.",
            "audio": "Feelings are a natural part of life. Everyone feels sad, nervous, or angry sometimes. When you feel worried, you should talk to someone you trust. Exercising is also a good idea because it makes your body release happy chemicals. Eating healthy food and sleeping well are important, so you should take care of your body to help your mind."
        },
        "quiz": [
            ("u22q1", "I am staying at home today _____ it is raining heavily.", ["because", "so", "but"], "because"),
            ("u22q2", "She didn't eat breakfast, _____ she is very hungry now.", ["because", "so", "or"], "so")
        ]
    },
    23: {
        "title": "Unit 23: In the Kitchen",
        "reading_title": "Home Cooking in America",
        "reading_text": "Many Americans enjoy cooking meals at home. Cooking is a relaxing hobby and a great way to eat fresh, healthy food. Modern American kitchens have many appliances like microwaves, ovens, refrigerators, and blenders to make food preparation quick and easy.",
        "dialogue": [
            ("Emma", "What are we going to cook for dinner?"),
            ("Tom", "Let's make a fresh pasta salad! Is there any cheese?"),
            ("Emma", "Yes, we have a lot of cheese, but we don't have many tomatoes."),
            ("Tom", "No problem, we have got some spinach too. How much olive oil is left?"),
            ("Emma", "There is a lot of olive oil. Let's start cooking!")
        ],
        "vocab": [
            ("Spoon / Fork / Knife", "Utensils for eating and cutting", "Eat your soup with a spoon.", "spoon_icon"),
            ("Plate / Bowl", "Dishes for holding food", "Put the salad in a large bowl.", "plate_icon"),
            ("Pot / Pan", "Containers for cooking on the stove", "Fry the onions in a pan.", "pot_icon"),
            ("Oven / Stove", "Appliances for baking and heating food", "Bake the cake in the oven.", "oven_icon"),
            ("Refrigerator / Fridge", "Appliance for keeping food cold", "The milk is in the fridge.", "fridge_icon"),
            ("Microwave", "Appliance for heating food quickly", "Warm up your soup in the microwave.", "microwave_icon")
        ],
        "grammar": {
            "title": "Quantifiers: Much, Many, A lot of",
            "rules": [
                "<strong>A lot of:</strong> Used in affirmative sentences for both countable and uncountable nouns.",
                "<span class='grammar-example'>We have a lot of apples. There is a lot of milk.</span>",
                "<strong>Many:</strong> Used with plural countable nouns (in negatives and questions).",
                "<span class='grammar-example'>We don't have many tomatoes. How many eggs do we need?</span>",
                "<strong>Much:</strong> Used with uncountable nouns (in negatives and questions).",
                "<span class='grammar-example'>There isn't much cheese. How much water do you drink?</span>"
            ],
            "audio": "We have a lot of apples. There is a lot of milk. We don't have many tomatoes. How many eggs do we need? There isn't much cheese. How much water do you drink?"
        },
        "listening": {
            "title": "Making a Shopping List",
            "audio": "Let's check what we need to buy. Do we have many eggs? No, we don't have many, only two. How about cheese? We have got a lot of cheese, so we don't need any. Is there much milk? No, there isn't much milk in the bottle. We must buy two cartons. And we need some apples too.",
            "transcript": "<strong>Lisa:</strong> Let's check what we need to buy. Do we have many eggs? <br><strong>Mark:</strong> No, we don't have many, only two. <br><strong>Lisa:</strong> How about cheese? <br><strong>Mark:</strong> We have got a lot of cheese, so we don't need any. <br><strong>Lisa:</strong> Is there much milk? <br><strong>Mark:</strong> No, there isn't much milk in the bottle. We must buy two cartons. And we need some apples too.",
            "questions": [
                "1. They have a lot of eggs. _____ (True/False)",
                "2. They don't need any cheese. _____ (True/False)",
                "3. They need to buy milk. _____ (True/False)"
            ]
        },
        "speaking": {
            "title": "Kitchen Inventory",
            "lines": [
                ("Student A", "Is there much juice in the fridge?"),
                ("Student B", "No, there isn't much, just one glass. But we have got a lot of oranges."),
                ("Student A", "How many oranges have we got?"),
                ("Student B", "About ten. We can make fresh orange juice!")
            ],
            "audio": "Is there much juice in the fridge? No, there isn't much, just one glass. But we have got a lot of oranges. How many oranges have we got? About ten. We can make fresh orange juice!"
        },
        "reading": {
            "title": "A Simple Kitchen Recipe",
            "text": "To make a quick tomato pasta, you need a lot of fresh tomatoes, some garlic, and olive oil. First, heat the olive oil in a pan. Add the garlic and fry it. Then, chop the tomatoes and put them in the pan. Cook for ten minutes. Boil a lot of water in a big pot and cook the pasta. Mix the pasta with the tomato sauce. Serve on a plate with cheese!",
            "audio": "To make a quick tomato pasta, you need a lot of fresh tomatoes, some garlic, and olive oil. First, heat the olive oil in a pan. Add the garlic and fry it. Then, chop the tomatoes and put them in the pan. Cook for ten minutes. Boil a lot of water in a big pot and cook the pasta. Mix the pasta with the tomato sauce. Serve on a plate with cheese!"
        },
        "quiz": [
            ("u23q1", "How _____ butter do we need for the cake?", ["many", "much", "any"], "much"),
            ("u23q2", "I don't have _____ friends in this city yet.", ["much", "many", "some"], "many")
        ]
    },
    24: {
        "title": "Unit 24: Modern Technology",
        "reading_title": "Silicon Valley and Tech Devices",
        "reading_text": "Silicon Valley in California is the center of global technology. Major companies build electronic devices and software that we use every day. Smartphones, laptops, and tablets help us connect with the internet, study, work, and chat with friends easily from anywhere.",
        "dialogue": [
            ("Alex", "My laptop is not working. If I press the power button, nothing happens."),
            ("Jordan", "Is the battery flat? If you plug in the charger, does the light turn on?"),
            ("Alex", "Yes, the red light is blinking now."),
            ("Jordan", "Okay, wait 5 minutes. If the battery is completely empty, it takes time to start.")
        ],
        "vocab": [
            ("Smartphone", "A mobile phone that performs many functions of a computer", "I use my smartphone to take photos.", "phone_icon"),
            ("Laptop / Computer", "A portable computer suitable for use while traveling", "He writes emails on his laptop.", "laptop_icon"),
            ("Tablet", "A flat, portable computer with a touchscreen", "She reads books on her tablet.", "tablet_icon"),
            ("Internet", "A global computer network", "We use the internet to study.", "internet_icon"),
            ("Social Media", "Websites and apps for sharing content and networking", "He spends a lot of time on social media.", "media_icon"),
            ("Download / Upload", "Transferring data to/from the internet", "I want to download a movie.", "download_icon")
        ],
        "grammar": {
            "title": "Zero Conditional (General Truths)",
            "rules": [
                "Use the Zero Conditional to talk about facts, scientific laws, or general truths (things that always happen under a certain condition).",
                "<strong>Structure:</strong> If + Present Simple, ... Present Simple.",
                "<span class='grammar-example'>If you heat ice, it melts. If you press this button, the computer turns on.</span>",
                "<strong>Negative:</strong> <span class='grammar-example'>If you don't connect to Wi-Fi, the internet doesn't work.</span>",
                "You can also use 'when' instead of 'if': <span class='grammar-example'>When you charge your phone, the battery icon appears.</span>"
            ],
            "audio": "If you heat ice, it melts. If you press this button, the computer turns on. If you don't connect to Wi-Fi, the internet doesn't work. When you charge your phone, the battery icon appears."
        },
        "listening": {
            "title": "Troubleshooting a Tablet",
            "audio": "My tablet is very slow. If you download many large apps, the memory becomes full. That makes it slow. What should I do? If you delete old photos and unused apps, it works much faster. Should I restart it too? Yes, if you restart the device, it clears temporary files.",
            "transcript": "<strong>Grandpa:</strong> My tablet is very slow. <br><strong>Tech Support:</strong> If you download many large apps, the memory becomes full. That makes it slow. <br><strong>Grandpa:</strong> What should I do? <br><strong>Tech Support:</strong> If you delete old photos and unused apps, it works much faster. <br><strong>Grandpa:</strong> Should I restart it too? <br><strong>Tech Support:</strong> Yes, if you restart the device, it clears temporary files.",
            "questions": [
                "1. The tablet is slow because the memory is full. _____ (True/False)",
                "2. Deleting old photos makes the tablet slower. _____ (True/False)",
                "3. Restarting the device helps it run better. _____ (True/False)"
            ]
        },
        "speaking": {
            "title": "Discussing Gadgets",
            "lines": [
                ("Student A", "How often do you use your tablet?"),
                ("Student B", "I use it every day. If I travel, I always take it to watch movies. Do you use your laptop often?"),
                ("Student A", "Yes. If I have homework, I write it on my laptop. It is much easier than a phone.")
            ],
            "audio": "How often do you use your tablet? I use it every day. If I travel, I always take it to watch movies. Do you use your laptop often? Yes. If I have homework, I write it on my laptop. It is much easier than a phone."
        },
        "reading": {
            "title": "Screen Time and Health",
            "text": "Modern technology makes our lives easier, but too much screen time is bad for our health. If you look at your phone for many hours, your eyes become tired. If you use your laptop late at night, you don't sleep well because of the blue light. If you sit at a desk all day without breaks, your back hurts. You should take regular breaks and walk outside!",
            "audio": "Modern technology makes our lives easier, but too much screen time is bad for our health. If you look at your phone for many hours, your eyes become tired. If you use your laptop late at night, you don't sleep well because of the blue light. If you sit at a desk all day without breaks, your back hurts. You should take regular breaks and walk outside!"
        },
        "quiz": [
            ("u24q1", "If you _____ this icon, the app downloads to your device.", ["press", "pressed", "will press"], "press"),
            ("u24q2", "The screen turns black if the battery _____ completely empty.", ["is", "are", "will be"], "is")
        ]
    }
}

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Build HTML template for the new units
def generate_unit_html(unit_num, u):
    yt_id = valid_yt_ids[(unit_num - 1) % len(valid_yt_ids)]
    
    # 1. Vocab html
    vocab_cards_html = ""
    for word, definition, example, icon in u["vocab"]:
        clean_ex = example.replace("'", "\\'")
        vocab_cards_html += f"""
                <div class="vocab-card">
                    <div class="vocab-word">{word}</div>
                    <div class="vocab-definition">{definition}</div>
                    <div class="vocab-example">"{example}"</div>
                    <button class="audio-btn small" onclick="speakText('{clean_ex}')">🔊</button>
                </div>"""

    # 2. Dialogue lines
    dialogue_lines_html = ""
    dialogue_clean_text = []
    for speaker, line in u["dialogue"]:
        dialogue_lines_html += f'<p style="margin-bottom: 0.5rem;"><strong>{speaker}:</strong> {line}</p>\n                    '
        dialogue_clean_text.append(f"{speaker} says: {line}")
    dialogue_clean_text_str = " ".join(dialogue_clean_text).replace("'", "\\'")

    # 3. Grammar rules
    grammar_rules_html = "<br>\n                ".join(u["grammar"]["rules"])
    clean_grammar_audio = u["grammar"]["audio"].replace("'", "\\'")

    # 4. Listening questions
    listening_questions_html = "".join([f"<li>{q}</li>\n                    " for q in u["listening"]["questions"]])
    clean_listening_audio = u["listening"]["audio"].replace("'", "\\'")
    
    # 5. Speaking lines
    speaking_lines_html = ""
    speaking_clean_text = []
    for speaker, line in u["speaking"]["lines"]:
        speaking_lines_html += f'<div class="dialogue-line"><span class="speaker-label">{speaker}:</span><span class="speaker-text">{line}</span></div>\n                '
        speaking_clean_text.append(f"{speaker} says: {line}")
    speaking_clean_text_str = " ".join(speaking_clean_text).replace("'", "\\'")

    # 6. Reading text
    clean_reading_audio = u["reading"]["text"].replace("'", "\\'")

    # 7. Quiz questions
    quiz_questions_html = ""
    for q_id, text, options, correct in u["quiz"]:
        options_html = "".join([f'<option value="{opt}">{opt}</option>' for opt in options])
        quiz_questions_html += f"""
            <div class="exercise-question" data-question="{q_id}">
                <p><strong>{text}</strong></p>
                <div class="exercise-dropdown">
                    <select data-correct="{correct}">
                        <option value="">Choose...</option>
                        {options_html}
                    </select>
                </div>
                <button class="check-answer-btn" onclick="checkDropdownAnswer('{q_id}')">Check Answer</button>
                <div class="feedback-message"></div>
            </div>"""

    # 8. Render full layout
    return f"""
<div id="unit-{unit_num}" class="course-unit" style="display: none;">
    <div class="container">
        <!-- 🇺🇸 AMERICAN ENGLISH IN USE (OXFORD STYLE) -->
        <section class="culture-section" style="margin-top: 0 !important;">
            <h2 class="section-title">{u["reading_title"]}</h2>
            
            <!-- YouTube Embedded Video -->
            <div class="youtube-container">
                <iframe src="https://www.youtube.com/embed/{yt_id}?rel=0" allowfullscreen></iframe>
            </div>
            
            <p class="video-reference" style="margin-top: 10px; font-size: 0.9rem; color: var(--text-secondary);"><strong>Reference:</strong> <a href="https://www.youtube.com/watch?v={yt_id}" target="_blank" style="color: var(--accent-indigo); text-decoration: none;">VOA Learning English Lesson {unit_num}</a></p>

            <div class="reading-passage" id="am-text-{unit_num}">
                <h3>📖 American Culture Notes</h3>
                <p>{u["reading_text"]}</p>
                <div style="margin-top:1rem;">
                    <button class="audio-btn" onclick="speakText('{clean_reading_audio}')">🔊 Listen to Notes</button>
                    <button class="audio-btn stop" onclick="stopAudio()">⏹️ Stop</button>
                </div>
            </div>

            <div class="american-dialogue" id="am-dialogue-{unit_num}">
                <h3>🗣️ Everyday Dialogue</h3>
                <div class="dialogue-box">
                    {dialogue_lines_html}
                </div>
                <div style="margin-top:1rem;">
                    <button class="audio-btn" onclick="speakText('Dialogue. {dialogue_clean_text_str}')">🔊 Listen to Dialogue</button>
                    <button class="audio-btn stop" onclick="stopAudio()">⏹️ Stop</button>
                </div>
            </div>
        </section>

        <!-- ===== UNIT {unit_num} VOCABULARY ===== -->
        <section class="section-wrapper" id="vocabulary-section-{unit_num}">
            <span class="section-label vocabulary">📚 Vocabulary</span>
            <h2 class="section-title">{u["title"].split(": ")[1]}</h2>
            <div class="vocabulary-grid">
                {vocab_cards_html}
            </div>
        </section>

        <!-- ===== UNIT {unit_num} GRAMMAR ===== -->
        <section class="grammar-box">
            <span class="section-label grammar">📝 Grammar</span>
            <h2 class="section-title">{u["grammar"]["title"]}</h2>
            <div class="grammar-rule">
                {grammar_rules_html}
            </div>
            <div style="margin-top:1rem">
                <button class="audio-btn" onclick="speakText('{clean_grammar_audio}')">🔊 Listen to Examples</button>
                <button class="audio-btn stop" onclick="stopAudio()">⏹️ Stop</button>
            </div>
        </section>

        <!-- ===== UNIT {unit_num} LISTENING ===== -->
        <section class="listening-section" id="listening-section-{unit_num}">
            <span class="section-label listening">🎧 Listening</span>
            <h2 style="margin-bottom:1.5rem">Listening Comprehension</h2>
            <div class="listening-exercise">
                <h3>🔊 Audio: Practice Listening</h3>
                <div class="audio-player">
                    <button class="audio-btn" onclick="speakText('{clean_listening_audio}')">🔊 Listen</button>
                    <button class="audio-btn" onclick="speakText('{clean_listening_audio}', true)">🐢 Slow</button>
                    <button class="audio-btn stop" onclick="stopAudio()">⏹️ Stop</button>
                </div>
                <div class="transcript-box">
                    <p><strong>📝 Transcript:</strong></p>
                    <p>{u["listening"]["transcript"]}</p>
                </div>
                <p><strong>Comprehension Questions:</strong></p>
                <ul style="margin:1rem 0;line-height:2.2">
                    {listening_questions_html}
                </ul>
            </div>
        </section>

        <!-- ===== UNIT {unit_num} SPEAKING ===== -->
        <section class="speaking-section">
            <span class="section-label speaking">🗣️ Speaking</span>
            <h2 class="section-title">Speaking Practice</h2>
            <h3 style="color:#9d174d;margin-bottom:1rem">Dialogue Practice</h3>
            <div class="dialogue-box">
                {speaking_lines_html}
            </div>
            <div style="margin-top:1.5rem">
                <button class="audio-btn" onclick="speakText('{speaking_clean_text_str}')">🔊 Listen to Model</button>
                <button class="audio-btn stop" onclick="stopAudio()">⏹️ Stop</button>
            </div>
        </section>

        <!-- ===== UNIT {unit_num} READING ===== -->
        <section class="reading-section">
            <span class="section-label reading">📖 Reading</span>
            <h2 class="section-title">Reading Comprehension</h2>
            <div class="reading-passage">
                <p>{u["reading"]["text"]}</p>
            </div>
            <div style="margin:1.5rem 0">
                <button class="audio-btn" onclick="speakText('{clean_reading_audio}')">🔊 Listen</button>
                <button class="audio-btn stop" onclick="stopAudio()">⏹️ Stop</button>
            </div>
        </section>

        <!-- ===== UNIT {unit_num} WRITING ===== -->
        <section class="writing-section">
            <span class="section-label writing">✍️ Writing</span>
            <h2 class="section-title">Writing Practice</h2>
            <div class="writing-template">
                <p>{u["reading"]["text"][:100]}...</p>
                <p style="margin-top:1rem;font-style:italic;color:var(--text-secondary)">Task: Write 4 sentences about your own life relating to this unit's topic.</p>
            </div>
        </section>

        <!-- ===== UNIT {unit_num} QUIZ ===== -->
        <section class="practice-section" id="practice-section-{unit_num}">
            <span class="section-label vocabulary">🎯 Quiz</span>
            <h2 class="section-title">Knowledge Check</h2>
            {quiz_questions_html}
            <div style="margin-top:1.5rem;text-align:center">
                <button onclick="checkAllExercises()" style="background:linear-gradient(135deg,#22c55e,#16a34a);border:none;padding:0.8rem 1.5rem;border-radius:8px;cursor:pointer;font-weight:bold;margin-right:1rem">✓ Check All</button>
                <button onclick="resetAllExercises()" style="background:linear-gradient(135deg,#64748b,#475569);border:none;padding:0.8rem 1.5rem;border-radius:8px;cursor:pointer;font-weight:bold">↻ Reset</button>
            </div>
        </section>
        
        {f'''
        <!-- Progress Test Section -->
        <section class="practice-section" id="progress-test-{(unit_num // 4)}" style="border: 2px solid #8b5cf6; background: rgba(139, 92, 246, 0.05); margin-top: 2rem;">
            <span class="section-label" style="background: rgba(139, 92, 246, 0.2); color: #8b5cf6;">Progress Test {(unit_num // 4)} 📝</span>
            <h2 class="section-title">Test {(unit_num // 4)} (Units {unit_num-3}-{unit_num})</h2>
            <div style="background: rgba(0,0,0,0.05); padding: 15px; border-radius: 8px; margin-bottom: 20px;">
                <p style="margin: 0; color: var(--text-primary);">Test your knowledge of the past units.</p>
            </div>
            <div class="exercise-question" data-question="pt{unit_num}q1">
                <p><strong>1. Choose the correct answer:</strong></p>
                <div class="exercise-dropdown"><select data-correct="correct"><option value="">Choose...</option><option value="correct">correct option</option><option value="incorrect">incorrect option</option></select></div>
                <button class="check-answer-btn" onclick="checkDropdownAnswer('pt{unit_num}q1')">Check</button><div class="feedback-message"></div>
            </div>
            <div style="margin-top:1.5rem;text-align:center">
                <button onclick="checkAllExercises()" style="background:linear-gradient(135deg,#8b5cf6,#6d28d9);border:none;padding:0.8rem 1.5rem;border-radius:8px;cursor:pointer;font-weight:bold;">✓ Submit Test</button>
            </div>
        </section>
        ''' if unit_num % 4 == 0 else ''}
    </div>
</div>
"""

# Let's rebuild the HTML by replacing the divs for unit-14 through unit-24
for unit_num in range(14, 25):
    # Locate <div id="unit-X" ... >
    start_tag = f'id="unit-{unit_num}"'
    start_idx = html.find(start_tag)
    if start_idx == -1:
        print(f"Could not find Unit {unit_num} to replace!")
        continue
    
    # We find the opening <div before id="unit-X"
    div_start = html.rfind('<div', 0, start_idx)
    
    # We find the matching closing </div> of this unit.
    # Because it is a simple sequence, the end of this unit is either the start of <div id="unit-X+1"
    # or if it's Unit 24, the end of curriculum-container.
    if unit_num < 24:
        next_tag = f'id="unit-{unit_num+1}"'
        next_idx = html.find(next_tag)
        div_end = html.rfind('<div', 0, next_idx)
    else:
        # For unit 24, it's before the container closes
        # Let's search for "</div>\n    </main>" or similar
        div_end = html.find('</div>\n    </main>', div_start)
        # Search backward for the closing div of unit 24
        div_end = html.rfind('</div>', 0, div_end) + len('</div>')
        
    old_block = html[div_start:div_end]
    new_block = generate_unit_html(unit_num, units_content[unit_num])
    
    html = html[:div_start] + new_block + html[div_end:]
    print(f"Replaced Unit {unit_num}")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("All units 14 to 24 successfully generated and updated!")
