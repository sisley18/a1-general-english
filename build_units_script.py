import re, sys
sys.stdout.reconfigure(encoding='utf-8')
from expand_units_5_to_10 import build_unit_html

# --- UNIT DATA DEFINITIONS BELOW ---

# --- UNIT 9 DATA: ABILITIES, TALENTS & SKILLS ---
u9_culture_title = "Abilities and Talents"
u9_culture_notes = "In American schools and workplaces, people encourage sharing unique talents. School talent shows, community sports leagues, and music clubs give people a chance to show what they can do well."
u9_dialogue_lines = [
    ("Emma", "Can you play any musical instruments, Mike?"),
    ("Mike", "Yes, I can play the piano, but I can't play the guitar."),
    ("Emma", "That's cool! Can you speak Spanish?"),
    ("Mike", "I can speak a little bit, but not fluently.")
]
u9_video_url = "https://www.youtube.com/watch?v=xOcmG4H3K20"
u9_video_text = "Watch VOA Learning English Lesson 9 on YouTube"

u9_vocab_cat1 = "Skills & Action Verbs"
u9_vocab_items1 = [
    ("Speak English", "Communicate verbally using the English language", "She can speak English fluently.", "🗣️"),
    ("Swim", "Move through water using body motions", "He can swim across the pool.", "🏊"),
    ("Drive a car", "Operate a motor vehicle safely", "Can you drive a manual car?", "🚗"),
    ("Cook Italian food", "Prepare delicious meals from Italy", "My mom can cook delicious lasagna.", "🍝"),
    ("Play piano", "Perform music on a keyboard instrument", "She plays the piano beautifully.", "🎹"),
    ("Dance salsa", "Move rhythmically to Latin salsa beats", "They can dance salsa very well.", "💃"),
    ("Sing songs", "Produce musical sounds with your voice", "He can sing opera songs.", "🎤"),
    ("Paint pictures", "Create artistic images with brush and paint", "She can paint landscape pictures.", "🎨"),
    ("Ride a bicycle", "Balance and pedal a two-wheeled bike", "The child learned to ride a bicycle.", "🚲"),
    ("Fix computers", "Repair software and hardware technical issues", "He can fix any computer problem.", "💻")
]

u9_vocab_cat2 = "Adverbs of Manner & Modifiers"
u9_vocab_items2 = [
    ("Very well", "With high skill or excellence", "She plays tennis very well.", "⭐"),
    ("Fast / Quickly", "At high speed; rapidly", "He can run very fast.", "⚡"),
    ("Fluently", "Spoken smoothly and accurately without hesitation", "She speaks French fluently.", "💬"),
    ("Easily", "Without difficulty or hard effort", "He solved the math puzzle easily.", "🧩"),
    ("Slowly", "At a low speed or pace", "Please speak more slowly.", "🐢"),
    ("A little bit", "A small amount or degree", "I can speak German a little bit.", "🤏"),
    ("Quite well", "Fairly well; to a good degree", "She sings quite well.", "👍"),
    ("Carefully", "With attention and caution", "Drive carefully on rainy roads.", "🛡️"),
    ("Loudly", "With great volume or sound", "Don't talk loudly in the library.", "🔊"),
    ("Quietly", "With little or no sound", "The students read quietly.", "🤫")
]

u9_grammar_rules = [
    ("Modal Verb Can / Can't", "Use CAN for ability (no 's' for 3rd person, base verb after).", "I can swim. She can speak English. They can't drive."),
    ("Questions with Can", "Put CAN before the subject for questions.", "Can you play piano? Yes, I can. / No, I can't."),
    ("Adverbs of Manner", "Adverbs describe HOW an action is done.", "She sings beautifully. He runs fast. They speak fluently.")
]

u9_grammar_ex = [
    ("She _____ speak English fluently.", ["can", "cans", "is can"], "can"),
    ("_____ you drive a manual car?", ["Can", "Do", "Are"], "Can"),
    ("He _____ swim because he is afraid of water.", ["can't", "can", "doesn't"], "can't"),
    ("They can _____ the guitar very well.", ["play", "playing", "plays"], "play"),
    ("Can she cook Italian food? Yes, she _____.", ["can", "is", "does"], "can"),
    ("Can they dance salsa? No, they _____.", ["can't", "don't", "aren't"], "can't"),
    ("He runs very _____.", ["fast", "fastly", "more fast"], "fast"),
    ("She speaks French _____.", ["fluently", "fluent", "fluency"], "fluently"),
    ("Please drive _____ on ice.", ["carefully", "careful", "care"], "carefully"),
    ("Can you fix this computer? Yes, I _____ do it easily.", ["can", "could to", "able"], "can"),
    ("My brother _____ play the violin.", ["can", "cans to", "is can"], "can"),
    ("They can't _____ in the deep lake.", ["swim", "swimming", "swams"], "swim"),
    ("Speak _____; the baby is sleeping.", ["quietly", "loudly", "fast"], "quietly"),
    ("Can your mother bake cakes? Yes, she _____.", ["can", "has", "does"], "can"),
    ("I can speak English a _____ bit.", ["little", "small", "short"], "little")
]

u9_listening_title = "Listening: Talent Survey"
u9_listening_items = [
    ("Can you play any sports, Mark? Yes, I can play basketball very well, but I can't play tennis.", "What sport can Mark play well?", ["Tennis", "Basketball", "Golf"], 1),
    ("She can speak three languages fluently: English, Spanish, and French.", "How many languages can she speak fluently?", ["One", "Two", "Three"], 2),
    ("Can your brother drive a car? No, he can't. He is only fifteen years old.", "Can the brother drive a car?", ["Yes", "No, he can't", "He drives every day"], 1),
    ("He is a great chef. He can cook delicious Italian meals.", "What type of meals can he cook?", ["Italian meals", "Chinese food", "Fast food"], 0),
    ("Can you swim across the river? No, I can't swim very far.", "Can the speaker swim far?", ["Yes", "No", "A long distance"], 1),
    ("She plays the grand piano beautifully in concerts.", "How does she play the piano?", ["Beautifully", "Terribly", "Loudly"], 0),
    ("Can they fix broken laptops? Yes, they have a computer repair shop.", "Can they fix laptops?", ["Yes", "No", "They sell books"], 0),
    ("Please speak slowly. I don't understand fast English.", "Why does the listener ask the speaker to talk slowly?", ["Because they don't understand fast English", "Because they are sleeping", "Because it's noisy"], 0),
    ("My sister can draw very detailed portrait pictures.", "What can the sister draw?", ["Detailed portrait pictures", "Cars", "Maps"], 0),
    ("Can you ride a motorcycle? Yes, but I drive carefully.", "How does he drive his motorcycle?", ["Carefully", "Fast", "Dangerously"], 0),
    ("He can sing opera songs very loudly.", "What style of songs can he sing?", ["Pop", "Opera", "Rock"], 1),
    ("Can children dance salsa easily? Yes, if they practice.", "Can children dance salsa with practice?", ["Yes", "No", "Never"], 0),
    ("She can't play the drums because it's too noisy.", "Why can't she play the drums?", ["It's too noisy", "She has no hands", "It's expensive"], 0),
    ("Can you code in Python? Yes, I can write programs easily.", "Can the person code in Python?", ["Yes, easily", "No", "Only a bit"], 0),
    ("They can run five miles without stopping.", "How far can they run?", ["One mile", "Five miles", "Ten miles"], 1)
]

u9_oral_title = "Oral Drills: Expressing Abilities"
u9_oral_items = [
    ("I can speak English fluently.", "Expressing affirmative ability."),
    ("She can play the piano very well.", "Expressing 3rd person ability with 'can'."),
    ("He can't drive a manual car.", "Expressing negative ability 'can't'."),
    ("Can you swim across the pool?", "Practice question intonation with 'can'."),
    ("Yes, I can swim very well!", "Affirmative short answer drill."),
    ("No, I can't swim at all.", "Negative short answer drill."),
    ("Please speak more slowly and clearly.", "Asking someone to adjust speaking manner."),
    ("Drive carefully on the highway.", "Adverb of manner 'carefully' drill."),
    ("She runs very fast in races.", "Adverb of manner 'fast' drill."),
    ("They can dance salsa gracefully.", "Adverb of manner 'gracefully' drill."),
    ("Can he fix this computer problem?", "Ability question drill for 3rd person."),
    ("Yes, he can fix it easily.", "Expressing effortless skill."),
    ("I can speak a little bit of French.", "Modifying ability level 'a little bit'."),
    ("Can you sing opera songs?", "Musical ability inquiry."),
    ("No, I can't sing, but I can play guitar!", "Contrasting abilities drill.")
]

u9_reading_title = "Reading: The Talent Show at Lincoln High"
u9_reading_text = "Lincoln High School hosts an annual talent show every spring. Students show their amazing talents to teachers and parents. This year, Jessica sang a famous pop song beautifully, and everyone clapped loudly. A student named Kevin played the violin fluently without looking at any sheet music. Another student, Leo, showed that he can solve a Rubik's Cube in less than thirty seconds! However, not everyone can perform on stage. Sam tried to juggle fire torches, but he couldn't do it safely, so he performed magic tricks instead. The talent show was a great success!"
u9_reading_items = [
    ("What event does Lincoln High School host every spring?", ["A talent show", "A sports day", "A book fair"], 0),
    ("Who watches the talent show?", ["Teachers and parents", "Only students", "Nobody"], 0),
    ("What did Jessica do on stage?", ["Sang a famous pop song", "Danced salsa", "Played violin"], 0),
    ("How did Jessica sing?", ["Beautifully", "Terrible", "Quietly"], 0),
    ("What instrument did Kevin play?", ["Violin", "Piano", "Guitar"], 0),
    ("Did Kevin look at sheet music while playing?", ["No, he played without sheet music", "Yes, constantly", "He didn't play"], 0),
    ("What can Leo solve in less than thirty seconds?", ["A Rubik's Cube", "A math exam", "A puzzle"], 0),
    ("What did Sam try to juggle initially?", ["Fire torches", "Balls", "Apples"], 0),
    ("Could Sam juggle fire torches safely?", ["No, he couldn't do it safely", "Yes, easily", "He was perfect"], 0),
    ("What did Sam perform instead of juggling fire?", ["Magic tricks", "Singing", "Dancing"], 0),
    ("How did the audience react to Jessica's song?", ["They clapped loudly", "They left", "They slept"], 0),
    ("Is the talent show held every spring?", ["Yes, annually", "No, every ten years", "Only once"], 0),
    ("Can Kevin play the violin?", ["Yes, fluently", "No, he can't", "A little bit"], 0),
    ("Was the talent show successful?", ["Yes, a great success", "No, it failed", "It was canceled"], 0),
    ("How fast can Leo solve the Rubik's Cube?", ["In less than 30 seconds", "In one hour", "In ten minutes"], 0)
]

u9_writing_title = "Writing & Sentence Structure: Abilities & Adverbs"
u9_writing_items = [
    ("Complete: She _____ play the piano very well.", ["can", "cans", "is can"], "can"),
    ("Fill in: _____ you speak English?", ["Can", "Do is", "Are"], "Can"),
    ("Complete: He _____ drive a car because he has no license.", ["can't", "can", "don't"], "can't"),
    ("Fill in: They can _____ salsa easily.", ["dance", "dancing", "danced"], "dance"),
    ("Complete: Can she cook? Yes, she _____.", ["can", "is", "does"], "can"),
    ("Fill in: He runs very _____.", ["fast", "fastly", "more fast"], "fast"),
    ("Complete: Please speak _____ in the library.", ["quietly", "loudly", "fast"], "quietly"),
    ("Fill in: Drive _____ when it rains.", ["carefully", "careful", "care"], "carefully"),
    ("Complete: She speaks Spanish _____.", ["fluently", "fluent", "fluency"], "fluently"),
    ("Fill in: I can swim _____ the pool.", ["across", "on", "into"], "across"),
    ("Complete: Can you fix computers? Yes, I _____.", ["can", "do", "am"], "can"),
    ("Fill in: He can't _____ high in the air.", ["jump", "jumping", "jumps"], "jump"),
    ("Complete: She sings _____ in the choir.", ["beautifully", "beautiful", "beauty"], "beautifully"),
    ("Fill in: They can speak a _____ English.", ["little", "small", "short"], "little"),
    ("Complete: Can they play tennis? No, they _____.", ["can't", "don't", "aren't"], "can't")
]

u9_quiz_title = "Unit 9 Review: Abilities & Talents"
u9_quiz_items = [
    ("What modal verb is used to express present ability?", ["Can", "Must", "Should"], 0, "'Can' expresses present ability."),
    ("What is the negative form of 'can'?", ["Can't / Cannot", "Don't can", "Not can"], 0, "'Can't' is the negative form."),
    ("Complete: She can _____ French fluently.", ["speak", "speaks", "speaking"], 0, "Use base verb after modal 'can'."),
    ("How do you ask about someone's ability to drive?", ["Can you drive a car?", "Do you can drive a car?", "Are you drive a car?"], 0, "Start question with 'Can you...'."),
    ("Complete: He runs very _____.", ["fast", "fastly", "more fast"], 0, "'Fast' is both adjective and adverb."),
    ("Which adverb means 'spoken smoothly and accurately'?", ["Fluently", "Slowly", "Loudly"], 0, "'Fluently' means smooth and accurate speech."),
    ("Complete: Can you swim? Yes, I _____.", ["can", "do", "am"], 0, "Short affirmative answer is 'Yes, I can'."),
    ("Complete: Can they dance? No, they _____.", ["can't", "don't", "aren't"], 0, "Short negative answer is 'No, they can't'."),
    ("Which adverb means 'with great care and attention'?", ["Carefully", "Fast", "Quietly"], 0, "Carefully means paying attention."),
    ("Complete: Please talk _____ because the baby is sleeping.", ["quietly", "loudly", "fast"], 0, "Quietly means with low sound."),
    ("Does 'can' change form for he/she/it?", ["No, 'can' stays the same for all subjects", "Yes, it becomes 'cans'", "Yes, it becomes 'is can'"], 0, "Modal verbs do not take 's'."),
    ("What is the base verb in 'She can play piano'?", ["play", "can", "piano"], 0, "Play is the main base verb."),
    ("Complete: He can fix computers _____.", ["easily", "easy", "more easy"], 0, "Easily is the adverb of manner."),
    ("Which action involves producing musical vocal sounds?", ["Singing", "Swimming", "Driving"], 0, "Singing is vocal music."),
    ("Complete: I can speak a _____ bit of German.", ["little", "small", "short"], 0, "'A little bit' expresses small degree.")
]


# --- UNIT 10 DATA: TRAVEL, HOLIDAYS & PAST EVENTS ---
u10_culture_title = "Travel and Holidays"
u10_culture_notes = "Road trips and summer vacations are a major part of American culture. Families visit famous National Parks like Yellowstone and the Grand Canyon, or travel to coastal beaches. People share holiday stories using the past tense ('We visited...', 'The weather was great!')."
u10_dialogue_lines = [
    ("Karen", "How was your vacation in Florida last week, Tom?"),
    ("Tom", "It was wonderful! The weather was warm and sunny every day."),
    ("Karen", "Did you stay at a hotel near the beach?"),
    ("Tom", "Yes, we stayed at a lovely hotel and visited the national park.")
]
u10_video_url = "https://www.youtube.com/watch?v=xOcmG4H3K20"
u10_video_text = "Watch VOA Learning English Lesson 10 on YouTube"

u10_vocab_cat1 = "Travel & Vacation Terms"
u10_vocab_items1 = [
    ("Passport", "Official document for international travel", "Don't forget your passport at the airport.", "🛂"),
    ("Plane Ticket", "Document giving permission to travel by airplane", "I booked my plane ticket online.", "🎟️"),
    ("Hotel", "Establishment providing lodging for travelers", "We stayed at a comfortable hotel.", "🏨"),
    ("Flight", "A journey made by an airplane", "Our flight to Miami was smooth.", "✈️"),
    ("Suitcase / Luggage", "Bags used for carrying personal clothes when traveling", "He packed his clothes in a large suitcase.", "🧳"),
    ("Airport", "Complex where commercial aircraft take off and land", "We arrived at the airport early.", "🛫"),
    ("Tourist", "Person traveling for pleasure and sightseeing", "Many tourists visit the Statue of Liberty.", "📸"),
    ("Beach", "Sandy shore by the ocean or sea", "We walked along the sunny beach.", "🏖️"),
    ("Mountain", "High natural elevation of the Earth's surface", "They hiked up the rocky mountain.", "⛰️"),
    ("Sightseeing", "Visiting interesting places as a tourist", "We went sightseeing in New York City.", "🏙️")
]

u10_vocab_cat2 = "Regular Past Verbs & Time Expressions"
u10_vocab_items2 = [
    ("Visited (-ed)", "Went to see a person or place in the past", "We visited Washington D.C. last summer.", "🏛️"),
    ("Stayed (-ed)", "Lived somewhere temporarily as a guest", "They stayed at a hotel by the sea.", "🛌"),
    ("Traveled (-ed)", "Made a journey to another city or country", "She traveled to California last month.", "🚗"),
    ("Arrived (-ed)", "Reached a destination at the end of a journey", "The train arrived at 6:00 PM.", "🛬"),
    ("Booked (-ed)", "Reserved a ticket or room in advance", "I booked a hotel room online.", "📅"),
    ("Walked (-ed)", "Moved on foot in the past", "We walked along the beach at sunset.", "🚶"),
    ("Enjoyed (-ed)", "Took pleasure or delight in something", "We enjoyed our vacation immensely.", "😊"),
    ("Yesterday", "On the day before today", "I arrived home yesterday evening.", "📆"),
    ("Last week / year", "During the previous week or year", "They visited Florida last year.", "🗓️"),
    ("Two days ago", "Two days before the present time", "He booked the flight two days ago.", "⏱️")
]

u10_grammar_rules = [
    ("Simple Past of To Be (Was / Were)", "I/He/She/It WAS. You/We/They WERE.", "The hotel was great. The beaches were crowded. It wasn't cold."),
    ("Regular Simple Past Verbs (-ed)", "Add -ed to base verbs for past actions.", "We visited museum. They stayed at hotel. I booked a ticket."),
    ("Past Time Expressions", "Use yesterday, last (week/month/year), (time) ago.", "I traveled to Miami last month. He arrived two hours ago.")
]

u10_grammar_ex = [
    ("The weather _____ warm and sunny yesterday.", ["was", "were", "is"], "was"),
    ("We _____ at a hotel near the beach last week.", ["stayed", "stay", "staying"], "stayed"),
    ("They _____ the museum two days ago.", ["visited", "visit", "visiting"], "visited"),
    ("The flights _____ very expensive last month.", ["were", "was", "are"], "were"),
    ("I _____ my plane ticket online yesterday.", ["booked", "book", "booking"], "booked"),
    ("_____ you happy with your holiday hotel?", ["Were", "Was", "Did"], "Were"),
    ("She _____ to California last summer.", ["traveled", "travel", "travels"], "traveled"),
    ("The train _____ at the station on time.", ["arrived", "arrive", "arriving"], "arrived"),
    ("Where _____ you last weekend?", ["were", "was", "did"], "were"),
    ("We _____ along the beach for two hours.", ["walked", "walk", "walking"], "walked"),
    ("It _____ rain yesterday morning.", ["didn't", "wasn't", "don't"], "didn't"),
    ("He _____ his vacation in Mexico.", ["enjoyed", "enjoy", "enjoys"], "enjoyed"),
    ("My suitcase _____ very heavy.", ["was", "were", "be"], "was"),
    ("They arrived two hours _____.", ["ago", "last", "yesterday"], "ago"),
    ("Was the hotel clean? Yes, it _____.", ["was", "were", "did"], "was")
]

u10_listening_title = "Listening: Holiday Travel Reports"
u10_listening_items = [
    ("Where did you go last summer, Lisa? I traveled to National Park in Wyoming. It was beautiful!", "Where did Lisa travel last summer?", ["Wyoming National Park", "Florida Beach", "New York"], 0),
    ("How was the flight to Chicago? The flight was delayed for two hours.", "How was the flight delayed?", ["One hour", "Two hours", "Not delayed"], 1),
    ("Did you stay in a hotel? No, we stayed at a cozy cabin near the lake.", "Where did they stay?", ["At a hotel", "At a cozy cabin near the lake", "In a tent"], 1),
    ("The museum was open yesterday. We walked around for three hours.", "How long did they walk around the museum?", ["One hour", "Three hours", "All day"], 1),
    ("Did Tom enjoy his trip to Paris? Yes, he enjoyed the food and sightseeing.", "What did Tom enjoy?", ["The food and sightseeing", "The rain", "The airport"], 0),
    ("My passport was in my backpack.", "Where was the passport?", ["In the suitcase", "In the backpack", "At home"], 1),
    ("We booked our flight tickets three weeks ago.", "When were the flight tickets booked?", ["Three weeks ago", "Yesterday", "Last year"], 0),
    ("Was the beach crowded? Yes, there were many tourists.", "Why was the beach crowded?", ["Many tourists were there", "It was closed", "It was raining"], 0),
    ("The bus arrived at 9:00 PM yesterday.", "What time did the bus arrive?", ["8:00 PM", "9:00 PM", "10:00 PM"], 1),
    ("She visited her grandparents in Oregon last month.", "Who did she visit in Oregon?", ["Her grandparents", "Her friends", "Her teacher"], 0),
    ("The weather wasn't cold; it was warm and sunny.", "How was the weather?", ["Cold", "Warm and sunny", "Snowing"], 1),
    ("We packed two large suitcases for the trip.", "How many suitcases did they pack?", ["One", "Two", "Three"], 1),
    ("He traveled by train across the country.", "How did he travel?", ["By plane", "By train", "By car"], 1),
    ("The tourist guide was very knowledgeable and friendly.", "How was the tourist guide?", ["Knowledgeable and friendly", "Rude", "Bored"], 0),
    ("Did you like the hotel pool? Yes, we swam every afternoon.", "When did they swim?", ["Every morning", "Every afternoon", "Never"], 1)
]

u10_oral_title = "Oral Drills: Past Holiday Experiences"
u10_oral_items = [
    ("How was your vacation last week?", "Wh-question asking about past events."),
    ("It was wonderful! The weather was warm.", "Expressing positive past experience."),
    ("We stayed at a hotel by the ocean.", "Practice past verb 'stayed'."),
    ("I traveled to California last summer.", "Practice past verb 'traveled'."),
    ("We visited famous museums in Washington.", "Practice past verb 'visited'."),
    ("I booked my plane tickets online two weeks ago.", "Practice time phrase 'two weeks ago'."),
    ("Were you happy with the hotel service?", "Question format with past of be 'Were you'."),
    ("Yes, the hotel staff was very helpful.", "Affirmative answer with 'was'."),
    ("No, the flight wasn't on time.", "Negative past statement with 'wasn't'."),
    ("They arrived at the airport yesterday evening.", "Practice time phrase 'yesterday evening'."),
    ("We walked along the sandy beach at sunset.", "Describing past holiday activity."),
    ("Did you enjoy your trip to New York?", "Question with 'Did you enjoy...?'"),
    ("Yes, we enjoyed sightseeing very much!", "Affirmative answer with 'enjoyed'."),
    ("Don't forget your passport at home!", "Travel reminder drill."),
    ("We had an amazing weekend holiday!", "Concluding past travel phrase.")
]

u10_reading_title = "Reading: A Summer Trip to Yellowstone"
u10_reading_text = "Last July, the Miller family traveled to Yellowstone National Park for their summer vacation. They drove from Denver in their family car. The journey was long, but the mountain scenery was breathtaking! They stayed at a rustic wooden lodge inside the park. Every morning, they walked along natural trails and visited famous geysers like Old Faithful. The weather was pleasant and sunny. They saw wild bison and eagles! Mr. Miller booked the lodge reservation six months ago. The family enjoyed their vacation so much that they want to return next year!"
u10_reading_items = [
    ("When did the Miller family travel to Yellowstone?", ["Last July", "Last December", "Two years ago"], 0),
    ("How did they travel to the park?", ["By plane", "In their family car", "By train"], 1),
    ("Where did they drive from?", ["Denver", "Chicago", "Seattle"], 0),
    ("Where did they stay during the trip?", ["At a hotel in town", "At a rustic wooden lodge inside the park", "In a tent"], 1),
    ("What famous geyser did they visit?", ["Old Faithful", "Grand Geyser", "Yellowstone Falls"], 0),
    ("How was the weather during their trip?", ["Pleasant and sunny", "Rainy and cold", "Snowy"], 0),
    ("What wild animals did they see?", ["Wild bison and eagles", "Bears and wolves", "Lions"], 0),
    ("When did Mr. Miller book the lodge reservation?", ["Six months ago", "Yesterday", "One week ago"], 0),
    ("Did the family enjoy their vacation?", ["Yes, they enjoyed it so much", "No, they hated it", "It was boring"], 0),
    ("What do they want to do next year?", ["Return to Yellowstone", "Stay home", "Travel to Europe"], 0),
    ("Was the journey long?", ["Yes, the journey was long", "No, it was short", "Not mentioned"], 0),
    ("What did they do every morning?", ["Walked along trails and visited geysers", "Slept late", "Swam"], 0),
    ("Was Old Faithful a museum or a geyser?", ["A geyser", "A museum", "A mountain"], 0),
    ("What month was the trip?", ["July", "August", "June"], 0),
    ("What kind of scenery did they see?", ["Breathtaking mountain scenery", "Desert sand", "City skyscrapers"], 0)
]

u10_writing_title = "Writing & Sentence Structure: Past Tense & Travel"
u10_writing_items = [
    ("Complete: The weather _____ warm yesterday.", ["was", "were", "is"], "was"),
    ("Fill in: We _____ at a hotel near the beach.", ["stayed", "stay", "staying"], "stayed"),
    ("Complete: They _____ to California last year.", ["traveled", "travel", "travels"], "traveled"),
    ("Fill in: I _____ my flight tickets online.", ["booked", "book", "booking"], "booked"),
    ("Complete: The tourists _____ the museum yesterday.", ["visited", "visit", "visiting"], "visited"),
    ("Fill in: The plane _____ at 5:00 PM.", ["arrived", "arrive", "arriving"], "arrived"),
    ("Complete: The beaches _____ crowded last summer.", ["were", "was", "are"], "were"),
    ("Fill in: We walked along the beach two hours _____.", ["ago", "last", "yesterday"], "ago"),
    ("Complete: Where _____ you last weekend?", ["were", "was", "did"], "were"),
    ("Fill in: He _____ his trip to Florida.", ["enjoyed", "enjoy", "enjoys"], "enjoyed"),
    ("Complete: It _____ rain yesterday.", ["didn't", "wasn't", "don't"], "didn't"),
    ("Fill in: She packed her clothes in a large _____.", ["suitcase", "ticket", "passport"], "suitcase"),
    ("Complete: Was the hotel clean? Yes, it _____.", ["was", "were", "did"], "was"),
    ("Fill in: They visited Yellowstone National Park _____ month.", ["last", "ago", "yesterday"], "last"),
    ("Complete: Don't forget your _____ at the airport.", ["passport", "bed", "stove"], "passport")
]

u10_quiz_title = "Unit 10 Review: Travel & Past Events"
u10_quiz_items = [
    ("What official document is required for international travel?", ["Passport", "Library card", "Receipt"], 0, "Passport is official travel document."),
    ("Past form of 'is / am' is:", ["Was", "Were", "Did"], 0, "Singular past of be is 'was'."),
    ("Past form of 'are' is:", ["Were", "Was", "Did"], 0, "Plural past of be is 'were'."),
    ("How do you form the regular past tense of 'visit'?", ["Visited", "Visits", "Visiting"], 0, "Add -ed for regular past tense."),
    ("Complete: We _____ at a nice hotel by the beach.", ["stayed", "stay", "staying"], 0, "Regular past verb 'stayed'."),
    ("Which word expresses past time counting backwards (e.g., 'two days ___')?", ["Ago", "Last", "Yesterday"], 0, "Ago counts back from present."),
    ("Complete: I _____ my flight tickets three weeks ago.", ["booked", "book", "booking"], 0, "Past verb 'booked'."),
    ("Where do planes take off and land?", ["Airport", "Bus station", "Hotel"], 0, "Airport handles aircraft traffic."),
    ("Complete: The weather _____ warm and sunny yesterday.", ["was", "were", "are"], 0, "Weather (uncountable singular) takes 'was'."),
    ("Complete: The tourists _____ the ancient ruins.", ["visited", "visiting", "visits"], 0, "Past action 'visited'."),
    ("Where do travelers stay on vacation?", ["Hotel / Lodge", "Library", "Supermarket"], 0, "Hotels provide lodging."),
    ("Complete: They arrived two hours _____.", ["ago", "last", "yesterday"], 0, "We say 'two hours ago'."),
    ("What bag is used for carrying clothes during travel?", ["Suitcase / Luggage", "Wallet", "Envelope"], 0, "Suitcase holds travel clothes."),
    ("Complete: Were you happy with the trip? Yes, I _____.", ["was", "were", "did"], 0, "Subject 'I' takes 'was' in past."),
    ("Complete: We _____ our vacation in California.", ["enjoyed", "enjoy", "enjoys"], 0, "Past verb 'enjoyed'.")
]

print("All datasets generated. Now constructing HTML for Units 5 through 10...")

# Generate HTML string for each unit
u5_html = build_unit_html(5, "My Home", u5_culture_title, u5_culture_notes, u5_dialogue_lines, u5_video_url, u5_video_text,
                           u5_vocab_cat1, u5_vocab_items1, u5_vocab_cat2, u5_vocab_items2,
                           "There is / There are — Prepositions of Place", u5_grammar_rules, u5_grammar_ex,
                           u5_listening_title, u5_listening_items, u5_oral_title, u5_oral_items,
                           u5_reading_title, u5_reading_text, u5_reading_items,
                           u5_writing_title, u5_writing_items, u5_quiz_title, u5_quiz_items)

u6_html = build_unit_html(6, "Around Town", u6_culture_title, u6_culture_notes, u6_dialogue_lines, u6_video_url, u6_video_text,
                           u6_vocab_cat1, u6_vocab_items1, u6_vocab_cat2, u6_vocab_items2,
                           "Directions, Imperatives & Prepositions of Location", u6_grammar_rules, u6_grammar_ex,
                           u6_listening_title, u6_listening_items, u6_oral_title, u6_oral_items,
                           u6_reading_title, u6_reading_text, u6_reading_items,
                           u6_writing_title, u6_writing_items, u6_quiz_title, u6_quiz_items)

u7_html = build_unit_html(7, "Clothes & Shopping", u7_culture_title, u7_culture_notes, u7_dialogue_lines, u7_video_url, u7_video_text,
                           u7_vocab_cat1, u7_vocab_items1, u7_vocab_cat2, u7_vocab_items2,
                           "Present Continuous for Wearing — Demonstratives & Prices", u7_grammar_rules, u7_grammar_ex,
                           u7_listening_title, u7_listening_items, u7_oral_title, u7_oral_items,
                           u7_reading_title, u7_reading_text, u7_reading_items,
                           u7_writing_title, u7_writing_items, u7_quiz_title, u7_quiz_items)

u8_html = build_unit_html(8, "Free Time & Hobbies", u8_culture_title, u8_culture_notes, u8_dialogue_lines, u8_video_url, u8_video_text,
                           u8_vocab_cat1, u8_vocab_items1, u8_vocab_cat2, u8_vocab_items2,
                           "Adverbs of Frequency & Likes / Dislikes (-ing)", u8_grammar_rules, u8_grammar_ex,
                           u8_listening_title, u8_listening_items, u8_oral_title, u8_oral_items,
                           u8_reading_title, u8_reading_text, u8_reading_items,
                           u8_writing_title, u8_writing_items, u8_quiz_title, u8_quiz_items)

u9_html = build_unit_html(9, "Abilities & Talents", u9_culture_title, u9_culture_notes, u9_dialogue_lines, u9_video_url, u9_video_text,
                           u9_vocab_cat1, u9_vocab_items1, u9_vocab_cat2, u9_vocab_items2,
                           "Modal Verb Can / Can't & Adverbs of Manner", u9_grammar_rules, u9_grammar_ex,
                           u9_listening_title, u9_listening_items, u9_oral_title, u9_oral_items,
                           u9_reading_title, u9_reading_text, u9_reading_items,
                           u9_writing_title, u9_writing_items, u9_quiz_title, u9_quiz_items)

u10_html = build_unit_html(10, "Travel & Holidays", u10_culture_title, u10_culture_notes, u10_dialogue_lines, u10_video_url, u10_video_text,
                           u10_vocab_cat1, u10_vocab_items1, u10_vocab_cat2, u10_vocab_items2,
                           "Simple Past of To Be (Was/Were) & Regular Past Verbs (-ed)", u10_grammar_rules, u10_grammar_ex,
                           u10_listening_title, u10_listening_items, u10_oral_title, u10_oral_items,
                           u10_reading_title, u10_reading_text, u10_reading_items,
                           u10_writing_title, u10_writing_items, u10_quiz_title, u10_quiz_items)

print("All 6 units built in memory! Replacing Units 5 to 10 in index.html...")

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Pattern to replace Units 5 to 10 block in index.html
# Search from <div id="unit-5" to just before <div id="unit-11"
pattern = r'<div id="unit-5"[\s\S]*?(?=<div id="unit-11")'
combined_units_html = u5_html + "\n\n" + u6_html + "\n\n" + u7_html + "\n\n" + u8_html + "\n\n" + u9_html + "\n\n" + u10_html + "\n\n"

if re.search(pattern, html):
    html = re.sub(pattern, combined_units_html, html)
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("SUCCESS: index.html updated with complete Units 5, 6, 7, 8, 9, 10!")
else:
    print("ERROR: Could not find <div id='unit-5'... in index.html")

