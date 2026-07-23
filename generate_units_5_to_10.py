import re, sys
sys.stdout.reconfigure(encoding='utf-8')
from expand_units_5_to_10 import build_unit_html

print("Defining datasets for Units 5 to 10...")

# ==========================================
# UNIT 5: MY HOME & FURNITURE
# ==========================================
u5_culture_title = "Homes in the Suburbs"
u5_culture_notes = "Many American families live in the suburbs. These are quiet neighborhoods outside the big city. Houses usually have a front yard and a backyard for barbecues. People park their cars in the garage."
u5_dialogue_lines = [
    ("Agent", "This is a beautiful house. It has three bedrooms and two bathrooms."),
    ("Buyer", "Is there a garage?"),
    ("Agent", "Yes, a two-car garage. And a big backyard!"),
    ("Buyer", "Awesome. I love it.")
]
u5_video_url = "https://www.youtube.com/watch?v=xOcmG4H3K20"
u5_video_text = "Watch VOA Learning English Lesson 5 on YouTube"

u5_vocab_cat1 = "Rooms of the House"
u5_vocab_items1 = [
    ("Living room", "The room where you relax and watch TV", "The sofa is in the living room.", "🛋️"),
    ("Kitchen", "The room where you cook food", "My mother cooks in the kitchen.", "🍳"),
    ("Bedroom", "The room where you sleep", "I have a big bedroom with a comfortable bed.", "🛏️"),
    ("Bathroom", "The room with a shower and toilet", "The bathroom is upstairs.", "🚿"),
    ("Dining room", "The room where you eat meals", "We eat dinner in the dining room.", "🍽️"),
    ("Garden / Yard", "The outdoor area around a house", "The children play in the yard.", "🏡"),
    ("Garage", "The place where you park your car", "The car is parked in the garage.", "🚗"),
    ("Basement", "The room below ground level", "We store old boxes in the basement.", "📦"),
    ("Attic", "The space under the roof", "The attic is full of old paintings.", "🏚️"),
    ("Hallway", "The passage connecting rooms", "Walk down the hallway to find the bathroom.", "🚪")
]
u5_vocab_cat2 = "Furniture & Appliances"
u5_vocab_items2 = [
    ("Table & Chairs", "Furniture for eating or working", "There is a wooden table and four chairs.", "🪑"),
    ("Sofa / Couch", "A comfortable long seat", "The sofa is very comfortable.", "🛋️"),
    ("Bed", "Furniture used for sleeping", "My bed is next to the large window.", "🛏️"),
    ("Wardrobe / Closet", "A tall cabinet for hanging clothes", "My clothes are in the bedroom closet.", "👔"),
    ("Refrigerator / Fridge", "Appliance to keep food cold", "The fresh milk is inside the fridge.", "🧊"),
    ("Lamp", "A light fixture", "There is a bright reading lamp on the desk.", "💡"),
    ("Desk", "A table used for study or work", "I do my English homework at my desk.", "🖥️"),
    ("Bookcase", "Shelves for keeping books", "The bookcase is filled with storybooks.", "📚"),
    ("Mirror", "Glass that reflects your image", "She looks in the mirror before going out.", "🪞"),
    ("Stove & Oven", "Appliance for cooking meals", "The soup is boiling on the stove.", "🍲")
]

u5_grammar_rules = [
    ("There is (Singular)", "Used with singular nouns.", "There is a sofa in the living room."),
    ("There are (Plural)", "Used with plural nouns.", "There are three bedrooms upstairs."),
    ("Prepositions of Place", "Describe where something is located.", "The book is on the table. The cat is under the chair.")
]
u5_grammar_ex = [
    ("_____ a mirror in the bathroom.", ["There is", "There are", "Is there"], "There is"),
    ("_____ four chairs in the dining room.", ["There is", "There are", "Are there"], "There are"),
    ("The cat is sleeping _____ the table.", ["under", "between", "next"], "under"),
    ("_____ any windows in the basement?", ["Are there", "There are", "Is there"], "Are there"),
    ("There _____ a lamp on the study desk.", ["is", "are", "be"], "is"),
    ("The fridge is _____ the kitchen.", ["in", "on", "at"], "in"),
    ("There _____ two cars in the garage.", ["are", "is", "was"], "are"),
    ("Is _____ a television in your bedroom?", ["there", "it", "they"], "there"),
    ("The sofa is right _____ to the armchair.", ["next", "near", "opposite"], "next"),
    ("There _____ any milk in the fridge.", ["isn't", "aren't", "is"], "isn't"),
    ("The garden is _____ the house.", ["behind", "under", "in"], "behind"),
    ("_____ a rug on the living room floor.", ["There is", "There are", "Are"], "There is"),
    ("The books are _____ the bookcase.", ["on", "under", "at"], "on"),
    ("There _____ five posters on the wall.", ["are", "is", "am"], "are"),
    ("Is there a garage? Yes, there _____.", ["is", "are", "has"], "is")
]

u5_listening_title = "Listening: House Tour & Descriptions"
u5_listening_items = [
    ("Welcome to my house! There is a living room, a kitchen, and two bedrooms.", "How many bedrooms are in the house?", ["One", "Two", "Three"], 1),
    ("The kitchen is very modern. There is a large fridge and a new stove.", "What is in the kitchen?", ["A sofa", "A large fridge and stove", "A bathtub"], 1),
    ("Where is the cat? Oh, it is sleeping under the dining room table.", "Where is the cat sleeping?", ["On the bed", "Under the dining room table", "In the garden"], 1),
    ("Our house has a beautiful backyard with green trees.", "What does the house have?", ["A garage", "A backyard with green trees", "A swimming pool"], 1),
    ("Is there a television in the bedroom? No, there isn't. The TV is in the living room.", "Where is the TV located?", ["In the bedroom", "In the kitchen", "In the living room"], 2),
    ("There are three chairs in the study room.", "How many chairs are in the study room?", ["Two", "Three", "Four"], 1),
    ("The car is parked inside the garage.", "Where is the car?", ["In the street", "In the garage", "In the yard"], 1),
    ("My bedroom is on the second floor.", "Where is the bedroom?", ["On the first floor", "On the second floor", "In the basement"], 1),
    ("There is a mirror above the bathroom sink.", "What is above the bathroom sink?", ["A mirror", "A picture", "A clock"], 0),
    ("The family eats dinner together in the dining room at 7 PM.", "When does the family eat dinner?", ["At 6 PM", "At 7 PM", "At 8 PM"], 1),
    ("Is there a basement? Yes, we store old luggage there.", "What is stored in the basement?", ["Old luggage", "Cars", "Bicycles"], 0),
    ("The lamp is next to the bed on the nightstand.", "Where is the lamp?", ["Next to the bed", "Under the bed", "On the desk"], 0),
    ("There aren't any stairs because it is a single-story home.", "Why are there no stairs?", ["It has no roof", "It is a single-story home", "It is an apartment"], 1),
    ("The garden is full of colorful flowers.", "What is in the garden?", ["Colorful flowers", "Vegetables", "A car"], 0),
    ("There is a comfortable red sofa in the living room.", "What color is the sofa?", ["Blue", "Red", "Green"], 1)
]

u5_oral_title = "Oral Drills: Describing Your Home"
u5_oral_items = [
    ("There is a sofa in the living room.", "Practice 'There is' with singular nouns."),
    ("There are two bedrooms upstairs.", "Practice 'There are' with plural nouns."),
    ("The lamp is on the wooden table.", "Focus on preposition 'on'."),
    ("The cat is resting under the chair.", "Focus on preposition 'under'."),
    ("Is there a garage in your house?", "Practice question intonation."),
    ("Yes, there is a one-car garage.", "Practice short affirmative answers."),
    ("No, there isn't a swimming pool.", "Practice short negative answers."),
    ("Where is the kitchen located?", "Wh-question practice."),
    ("The kitchen is next to the dining room.", "Focus on 'next to'."),
    ("My bedroom is cozy and bright.", "Describing personal spaces."),
    ("There are books on the bookshelf.", "Plural noun drill."),
    ("Is there a mirror in the hallway?", "Question practice with 'is there'."),
    ("The car is inside the garage.", "Preposition 'inside' drill."),
    ("There aren't any chairs in the hall.", "Negative plural drill 'there aren't'."),
    ("We eat breakfast in the kitchen every morning.", "Daily home routine phrase.")
]

u5_reading_title = "Reading: My New Apartment in Chicago"
u5_reading_text = "Hello! My name is Mark. I live in a new apartment in Chicago. My apartment is on the third floor. It has a spacious living room, a modern kitchen, one bedroom, and a small bathroom. In the living room, there is a gray sofa, a coffee table, and a large TV on the wall. My bedroom has a comfortable bed and a big closet for my clothes. I don't have a garden, but there is a lovely balcony with green plants. I really love my home!"
u5_reading_items = [
    ("Where does Mark live?", ["In New York", "In Chicago", "In Boston"], 1),
    ("What floor is his apartment on?", ["First floor", "Second floor", "Third floor"], 2),
    ("How many bedrooms are in his apartment?", ["One", "Two", "Three"], 0),
    ("What color is the sofa in the living room?", ["Blue", "Gray", "Black"], 1),
    ("Where is the large TV?", ["On a table", "On the wall", "In the bedroom"], 1),
    ("Does Mark have a garden?", ["Yes, a big garden", "No, he has a balcony instead", "No, he has a garage"], 1),
    ("What is on the balcony?", ["A table and chairs", "Green plants", "A barbecue"], 1),
    ("What is in his bedroom?", ["A bed and a big closet", "A sofa and TV", "A desk and stove"], 0),
    ("Is the kitchen modern or old?", ["Modern", "Old", "Small"], 0),
    ("How does Mark feel about his home?", ["He dislikes it", "He wants to move", "He really loves it"], 2),
    ("Is the apartment on the ground floor?", ["Yes", "No", "Not mentioned"], 1),
    ("Where is the closet located?", ["In the living room", "In the bedroom", "In the bathroom"], 1),
    ("What is next to the sofa?", ["A coffee table", "A bed", "A fridge"], 0),
    ("How many bathrooms are there?", ["One small bathroom", "Two bathrooms", "None"], 0),
    ("What city is the apartment in?", ["Chicago", "Miami", "Seattle"], 0)
]

u5_writing_title = "Writing & Sentence Structure: Home Descriptions"
u5_writing_items = [
    ("Complete: There _____ a rug on the floor.", ["is", "are", "have"], "is"),
    ("Complete: There _____ three pillows on the couch.", ["are", "is", "be"], "are"),
    ("Fill in: The keys are _____ top of the kitchen table.", ["on", "under", "between"], "on"),
    ("Fill in: My desk is placed _____ the window and the bed.", ["between", "in", "at"], "between"),
    ("Choose correct form: _____ there a TV in your room?", ["Is", "Are", "Do"], "Is"),
    ("Choose correct form: _____ there any towels in the bathroom?", ["Are", "Is", "Has"], "Are"),
    ("Fill in: The shoes are _____ the bed.", ["under", "on", "into"], "under"),
    ("Complete: There _____ a garage behind the house.", ["is", "are", "were"], "is"),
    ("Complete: There _____ many trees in the yard.", ["are", "is", "am"], "are"),
    ("Fill in: We store old boxes _____ the basement.", ["in", "on", "to"], "in"),
    ("Choose: Is there a garden? No, there _____.", ["isn't", "aren't", "not"], "isn't"),
    ("Choose: Are there two bathrooms? Yes, there _____.", ["are", "is", "have"], "are"),
    ("Fill in: The clock is hanging _____ the wall.", ["on", "in", "under"], "on"),
    ("Complete: There isn't _____ armchair in the bedroom.", ["an", "a", "some"], "an"),
    ("Complete: There aren't _____ books on the table.", ["any", "some", "a"], "any")
]

u5_quiz_title = "Unit 5 Review: My Home & Furniture"
u5_quiz_items = [
    ("Which room is used for sleeping?", ["Kitchen", "Bedroom", "Garage"], 1, "Bedroom is the room with a bed."),
    ("Where do you park a car?", ["Attic", "Garage", "Bathroom"], 1, "Garage is used for parking vehicles."),
    ("Complete: _____ a sofa in the living room.", ["There is", "There are", "They are"], 0, "'Sofa' is singular so use 'There is'."),
    ("Complete: _____ three chairs around the table.", ["There are", "There is", "It is"], 0, "'Three chairs' is plural so use 'There are'."),
    ("Where is the milk kept?", ["In the wardrobe", "In the fridge", "On the bookcase"], 1, "Fridge keeps food cold."),
    ("Where do you cook meals?", ["Bathroom", "Kitchen", "Living room"], 1, "Kitchen is for cooking."),
    ("The cat is hiding _____ the bed.", ["under", "between", "on top"], 0, "Under means beneath."),
    ("Is there a bathroom on the first floor? Yes, _____.", ["there is", "there are", "it is"], 0, "Affirmative answer for singular is 'there is'."),
    ("Are there any plants in the garden? Yes, _____.", ["there are", "there is", "they are"], 0, "Affirmative answer for plural is 'there are'."),
    ("Where do you hang your clothes?", ["In the closet / wardrobe", "In the oven", "On the mirror"], 0, "Closet / wardrobe stores clothes."),
    ("Complete: The lamp is _____ the desk.", ["on", "in", "into"], 0, "'On' indicates surface contact."),
    ("Which space is under the roof?", ["Attic", "Basement", "Garage"], 0, "The attic is under the roof."),
    ("Which space is below ground level?", ["Basement", "Attic", "Balcony"], 0, "The basement is below ground."),
    ("Complete: There _____ any pictures on the wall.", ["aren't", "isn't", "not"], 0, "'Pictures' is plural negative so 'aren't'."),
    ("Complete: The dining table is _____ the living room and kitchen.", ["between", "on", "under"], 0, "'Between' refers to a middle position.")
]


# ==========================================
# UNIT 6: AROUND TOWN & DIRECTIONS
# ==========================================
u6_culture_title = "Around Town & Directions"
u6_culture_notes = "American cities often use a grid pattern with numbered streets and avenues. A block is the space between two intersecting streets. People ask for directions using polite phrases like 'Excuse me, where is...?' or 'How do I get to...?'. Downtown is the commercial center of a city."
u6_dialogue_lines = [
    ("Tourist", "Excuse me! Is there a bank near here?"),
    ("Local", "Yes, there is one on Main Street. Go straight for two blocks and turn left."),
    ("Tourist", "Is it next to the supermarket?"),
    ("Local", "That's right! It's right opposite the city park.")
]
u6_video_url = "https://www.youtube.com/watch?v=xOcmG4H3K20"
u6_video_text = "Watch VOA Learning English Lesson 6 on YouTube"

u6_vocab_cat1 = "Places in Town"
u6_vocab_items1 = [
    ("Bank", "A place to keep or withdraw money", "I need to deposit money at the bank.", "🏦"),
    ("Post Office", "A place to buy stamps and mail letters", "Send this package at the post office.", "📮"),
    ("Supermarket", "A large grocery store", "We buy fresh vegetables at the supermarket.", "🛒"),
    ("Library", "A place to borrow books and study", "The public library is very quiet.", "📚"),
    ("Park", "A green outdoor public area", "Children play soccer in the city park.", "🌳"),
    ("Hospital", "A medical center for sick people", "The ambulance drove to the hospital.", "🏥"),
    ("Pharmacy / Drugstore", "A store selling medicines", "Buy your aspirin at the pharmacy.", "💊"),
    ("Bus Station", "Where buses arrive and depart", "Wait for bus line 5 at the bus station.", "🚌"),
    ("Restaurant", "A place where cooked meals are served", "We ate dinner at an Italian restaurant.", "🍽️"),
    ("Movie Theater / Cinema", "A venue for watching films", "Let's watch a film at the movie theater.", "🎬")
]

u6_vocab_cat2 = "Directions & Location Phrases"
u6_vocab_items2 = [
    ("Turn left", "Change direction to the left", "Turn left at the next traffic light.", "⬅️"),
    ("Turn right", "Change direction to the right", "Turn right onto 5th Avenue.", "➡️"),
    ("Go straight ahead", "Move forward without turning", "Go straight ahead for two blocks.", "⬆️"),
    ("Cross the street", "Walk from one side of the road to the other", "Cross the street carefully.", "🚶"),
    ("On the corner", "Where two streets meet", "The coffee shop is on the corner.", "📐"),
    ("Opposite / Across from", "Facing something on the other side", "The library is opposite the park.", "↔️"),
    ("Next to", "Beside or by the side of", "The bakery is next to the pharmacy.", "👥"),
    ("Between", "In the middle of two places", "The bank is between the museum and cafe.", "⏸️"),
    ("Traffic light", "Signal light controlling street traffic", "Stop when the traffic light turns red.", "🚦"),
    ("Block", "Distance from one street intersection to the next", "Walk three blocks north.", "🏙️")
]

u6_grammar_rules = [
    ("Imperatives for Directions", "Use base verbs to give directions.", "Turn right. Go straight. Cross the street."),
    ("Prepositions of Location", "Describe spatial position in town.", "The bank is opposite the park. The hospital is next to the library."),
    ("Asking for Directions", "Polite questions for finding places.", "Excuse me, where is the post office? How do I get to the bus station?")
]

u6_grammar_ex = [
    ("_____ left at the intersection.", ["Turn", "Turning", "Turns"], "Turn"),
    ("Go _____ ahead for two blocks.", ["straight", "direct", "right"], "straight"),
    ("The supermarket is _____ to the post office.", ["next", "near", "opposite"], "next"),
    ("Excuse me, _____ is the nearest bank?", ["where", "what", "who"], "where"),
    ("_____ the street at the pedestrian crossing.", ["Cross", "Across", "Crossing"], "Cross"),
    ("The library is _____ the park and the school.", ["between", "among", "next"], "between"),
    ("Turn right _____ 3rd Avenue.", ["onto", "in", "at"], "onto"),
    ("The pharmacy is on the _____ of Elm Street.", ["corner", "edge", "middle"], "corner"),
    ("_____ straight until you see the gas station.", ["Walk", "Walking", "Walks"], "Walk"),
    ("How do I _____ to the train station?", ["get", "go to get", "arriving"], "get"),
    ("The coffee shop is _____ from the bank.", ["across", "opposite to", "next"], "across"),
    ("Don't _____ left here; it's a one-way street.", ["turn", "turning", "turned"], "turn"),
    ("The hospital is _____ Second Street.", ["on", "in", "at"], "on"),
    ("Is there a post office near here? Yes, there _____ one nearby.", ["is", "are", "has"], "is"),
    ("_____ me, can you help me find the hotel?", ["Excuse", "Pardon to", "Sorry"], "Excuse")
]

u6_listening_title = "Listening: Asking & Giving Directions"
u6_listening_items = [
    ("Excuse me! Where is the public library? It is on Oxford Street, opposite the city park.", "Where is the public library?", ["Next to the bank", "Opposite the city park", "In the hospital"], 1),
    ("To get to the supermarket, go straight ahead for two blocks and turn left.", "What should you do after two blocks?", ["Turn right", "Turn left", "Stop"], 1),
    ("Is the pharmacy open? Yes, it is next to the post office.", "What is next to the pharmacy?", ["The post office", "The park", "The school"], 0),
    ("Turn right at the traffic lights and the bank is on your left.", "Where is the bank after turning right?", ["On your right", "On your left", "Behind you"], 1),
    ("Excuse me, how do I get to the bus station? Walk straight for one block.", "How far is the bus station?", ["One block", "Three blocks", "Five blocks"], 0),
    ("The hospital is located on 5th Avenue, across from the gas station.", "What is across from the hospital?", ["A park", "A gas station", "A library"], 1),
    ("Is there a good restaurant near here? Yes, there is a Italian place on the corner.", "Where is the Italian restaurant?", ["On the corner", "In the park", "Under the bridge"], 0),
    ("Don't turn left at the street light; go straight.", "What direction should the person follow?", ["Turn left", "Go straight", "Turn back"], 1),
    ("The museum is situated between the cinema and the art gallery.", "What is next to the museum?", ["The cinema and art gallery", "The bank and park", "The school"], 0),
    ("You can find the post office next to the police station.", "Where is the post office?", ["Next to the police station", "Opposite the lake", "Far away"], 0),
    ("Cross the street at the green signal.", "When should you cross the street?", ["At the green signal", "At the red light", "Anytime"], 0),
    ("The movie theater is on Main Street.", "What street is the movie theater on?", ["Main Street", "Broadway", "5th Avenue"], 0),
    ("Is there a coffee shop nearby? Yes, walk past the bank and turn right.", "What building do you walk past?", ["The bank", "The school", "The hospital"], 0),
    ("Walk two blocks north to find the park entrance.", "What direction do you walk?", ["North", "South", "West"], 0),
    ("The train station is at the end of the road.", "Where is the train station?", ["At the end of the road", "At the beginning", "On the left"], 0)
]

u6_oral_title = "Oral Drills: Navigation & Directions"
u6_oral_items = [
    ("Excuse me, where is the nearest bank?", "Practice polite question intonation."),
    ("Go straight ahead for two blocks.", "Practice imperative direction phrase."),
    ("Turn left at the next intersection.", "Practice direction command 'Turn left'."),
    ("Turn right onto Main Street.", "Practice direction command 'Turn right'."),
    ("The post office is next to the pharmacy.", "Practice preposition 'next to'."),
    ("The library is opposite the park.", "Practice preposition 'opposite'."),
    ("The cafe is on the corner of 4th Street.", "Practice 'on the corner of'."),
    ("Cross the street carefully at the crosswalk.", "Safety command drill."),
    ("How do I get to the city hospital?", "Asking 'How do I get to...?'"),
    ("Walk past the supermarket.", "Verb phrase 'Walk past'."),
    ("It is between the bakery and the bank.", "Practice 'between'."),
    ("Is there a restaurant near here?", "Asking 'Is there a... near here?'"),
    ("Yes, there is one across from the hotel.", "Answering location questions."),
    ("Go down this street and turn left.", "Direction sentence drill."),
    ("Thank you for your help! You're welcome!", "Polite gratitude exchange.")
]

u6_reading_title = "Reading: Exploring Downtown San Diego"
u6_reading_text = "Welcome to San Diego! Downtown San Diego is easy to explore on foot. If you start at the Central Station, walk straight ahead on Broadway for three blocks. On your right, you will see the City Park. Opposite the park, there is a large public library. If you need money, there is a bank on the corner of Broadway and 4th Avenue, right next to a famous seafood restaurant. To reach the harbor, cross Pacific Highway at the traffic light. Enjoy your day around town!"
u6_reading_items = [
    ("Which city is this reading passage about?", ["San Francisco", "San Diego", "Los Angeles"], 1),
    ("Is downtown San Diego easy to explore on foot?", ["Yes, it is easy", "No, you need a car", "Only by bus"], 0),
    ("Where do you start walking from?", ["Central Station", "The Harbor", "The Airport"], 0),
    ("How many blocks do you walk on Broadway?", ["One block", "Two blocks", "Three blocks"], 2),
    ("Where is the City Park located?", ["On your left", "On your right", "Behind the station"], 1),
    ("What is opposite the park?", ["A large public library", "A bank", "A gas station"], 0),
    ("Where is the bank located?", ["On the corner of Broadway and 4th Avenue", "In the park", "Near the airport"], 0),
    ("What is right next to the bank?", ["A seafood restaurant", "A bakery", "A school"], 0),
    ("What street do you cross to reach the harbor?", ["Pacific Highway", "Broadway", "4th Avenue"], 0),
    ("Where should you cross Pacific Highway?", ["At the traffic light", "Anywhere", "Under the bridge"], 0),
    ("What kind of restaurant is next to the bank?", ["Italian", "Seafood", "Fast food"], 1),
    ("What building is opposite the City Park?", ["The library", "The station", "The bank"], 0),
    ("Is there a bank in downtown San Diego?", ["Yes", "No", "Not mentioned"], 0),
    ("What street do you walk on from Central Station?", ["Broadway", "Main Street", "Ocean Drive"], 0),
    ("What is the general tone of the passage?", ["Welcoming visitor guide", "Technical manual", "History book"], 0)
]

u6_writing_title = "Writing & Sentence Structure: City Directions"
u6_writing_items = [
    ("Complete: _____ left at the corner of 5th street.", ["Turn", "Turning", "Turns"], "Turn"),
    ("Fill in: Walk straight _____ for three blocks.", ["ahead", "to", "at"], "ahead"),
    ("Fill in: The bank is _____ the supermarket.", ["next to", "next", "to"], "next to"),
    ("Complete: Excuse me, _____ is the bus stop?", ["where", "how", "what"], "where"),
    ("Fill in: The library is _____ the park and the hospital.", ["between", "among", "through"], "between"),
    ("Complete: _____ the street at the pedestrian zebra line.", ["Cross", "Across", "Crossing"], "Cross"),
    ("Fill in: The restaurant is opposite _____ the hotel.", ["from", "to", "at"], "from"),
    ("Complete: _____ right onto Broadway Avenue.", ["Turn", "Go", "Walk"], "Turn"),
    ("Fill in: There is a pharmacy _____ the corner.", ["on", "in", "to"], "on"),
    ("Complete: How do I _____ to the train station?", ["get", "going", "arrived"], "get"),
    ("Fill in: Go past _____ bank and turn right.", ["the", "a", "an"], "the"),
    ("Complete: Don't _____ straight; turn right here.", ["go", "going", "went"], "go"),
    ("Fill in: The park is right _____ the library.", ["behind", "under", "in"], "behind"),
    ("Complete: _____ me, is there a post office near here?", ["Excuse", "Pardon", "Sorry"], "Excuse"),
    ("Fill in: Stop when the traffic light is _____.", ["red", "green", "blue"], "red")
]

u6_quiz_title = "Unit 6 Review: Around Town & Directions"
u6_quiz_items = [
    ("Where do you borrow books?", ["At the library", "At the bank", "At the bakery"], 0, "Library is for borrowing books."),
    ("Where do you buy medicines?", ["Pharmacy / Drugstore", "Post Office", "Park"], 0, "Pharmacy sells medical supplies."),
    ("Which direction phrase means moving forward without turning?", ["Go straight ahead", "Turn left", "Cross the street"], 0, "Go straight means keep moving forward."),
    ("Complete: Turn _____ at the traffic light.", ["left", "straight", "over"], 0, "Turn left or right are valid directions."),
    ("Complete: The bank is _____ to the supermarket.", ["next", "near", "opposite"], 0, "'Next to' means beside."),
    ("Where do you mail letters and packages?", ["Post office", "Hospital", "Cinema"], 0, "Post office handles mail."),
    ("Complete: Excuse me, _____ do I get to the hospital?", ["how", "where", "what"], 0, "'How do I get to...?' asks for directions."),
    ("What signal controls street traffic?", ["Traffic light", "Street lamp", "Billboard"], 0, "Traffic light manages traffic flow."),
    ("Complete: The coffee shop is _____ the corner.", ["on", "in", "under"], 0, "We say 'on the corner'."),
    ("Which phrase means walking from one side of the street to the other?", ["Cross the street", "Turn right", "Go past"], 0, "Cross means move across."),
    ("Where do you go to see a film?", ["Movie theater / Cinema", "Pharmacy", "Library"], 0, "Movie theater shows films."),
    ("Complete: The museum is _____ the park.", ["opposite", "between of", "next from"], 0, "Opposite means facing directly across."),
    ("Where do buses arrive and depart?", ["Bus station", "Post office", "Bank"], 0, "Bus station is for bus transit."),
    ("Complete: Walk two _____ down Broadway.", ["blocks", "corners", "lights"], 0, "Blocks measure city distance."),
    ("Complete: The school is _____ the library and the park.", ["between", "next", "opposite"], 0, "Between links two distinct reference points.")
]


# ==========================================
# UNIT 7: CLOTHES, COLORS & SHOPPING
# ==========================================
u7_culture_title = "Clothes and Shopping"
u7_culture_notes = "American shopping malls and outlet centers are popular places to shop. People wear casual clothes like jeans, T-shirts, and sneakers every day. When shopping, salespeople often ask 'Can I help you find something?' or 'What size are you looking for?'."
u7_dialogue_lines = [
    ("Clerk", "Hi! Can I help you find anything today?"),
    ("Customer", "Yes, please. How much is this blue jacket?"),
    ("Clerk", "It's on sale for $45. What size do you need?"),
    ("Customer", "Medium, please. Can I try it on in the fitting room?"),
    ("Clerk", "Sure! The fitting room is right over there.")
]
u7_video_url = "https://www.youtube.com/watch?v=xOcmG4H3K20"
u7_video_text = "Watch VOA Learning English Lesson 7 on YouTube"

u7_vocab_cat1 = "Clothing & Footwear"
u7_vocab_items1 = [
    ("T-shirt", "A casual short-sleeved cotton shirt", "He is wearing a white T-shirt.", "👕"),
    ("Shirt", "A formal button-up garment", "I wear a blue shirt to work.", "👔"),
    ("Pants / Jeans", "Trousers worn on the lower body", "These denim jeans are very comfortable.", "👖"),
    ("Dress", "A one-piece garment for women", "She bought an elegant red dress.", "👗"),
    ("Skirt", "A garment hanging from the waist", "She is wearing a black skirt.", "🥻"),
    ("Jacket / Coat", "Outer clothing worn for warmth", "Put on your warm coat; it is cold outside.", "🧥"),
    ("Shoes", "Footwear worn outdoors", "He polished his black leather shoes.", "👞"),
    ("Sneakers", "Casual athletic shoes", "I wear white sneakers for walking.", "👟"),
    ("Hat / Cap", "A covering for the head", "He wears a baseball cap in the sun.", "🧢"),
    ("Socks", "Garment worn on the feet inside shoes", "I need a pair of warm winter socks.", "🧦")
]

u7_vocab_cat2 = "Shopping & Money Terms"
u7_vocab_items2 = [
    ("Price tag", "Label showing how much an item costs", "Check the price tag before buying.", "🏷️"),
    ("Fitting room", "Private room to try on clothes", "Where is the fitting room?", "🚪"),
    ("Cashier", "Person who collects payment in a store", "Pay for your clothes at the cashier.", "🧑‍💼"),
    ("Size (S / M / L / XL)", "Dimensions of clothing items", "Do you have this sweater in size Large?", "📐"),
    ("Cheap", "Low in price or cost", "This shirt is very cheap; it's only $10.", "💰"),
    ("Expensive", "High in price or costing a lot of money", "That designer coat is too expensive.", "💎"),
    ("Discount / Sale", "Reduction in regular price", "There is a 30% discount on all shoes.", "🏷️"),
    ("Receipt", "Paper showing proof of payment", "Keep your receipt for returns.", "🧾"),
    ("Credit card", "Plastic card used to pay electronically", "Can I pay with a credit card?", "💳"),
    ("Cash", "Paper money and coins", "I paid $20 in cash.", "💵")
]

u7_grammar_rules = [
    ("Present Continuous for Wearing", "Use am/is/are + wearing for current clothing.", "She is wearing a red jacket today. They are wearing sneakers."),
    ("Demonstratives (This/That/These/Those)", "This/These (near), That/Those (far).", "This shirt (singular near). Those shoes (plural far)."),
    ("Asking Prices (How much)", "How much is (singular) / How much are (plural).", "How much is this sweater? How much are these jeans?")
]

u7_grammar_ex = [
    ("Look! She _____ a beautiful yellow dress.", ["is wearing", "wears", "are wearing"], "is wearing"),
    ("How much _____ this pair of shoes?", ["is", "are", "be"], "is"),
    ("How much _____ those blue pants?", ["are", "is", "am"], "are"),
    ("I like _____ shirt right here in my hand.", ["this", "that", "these"], "this"),
    ("Look at _____ coat over there on the wall.", ["that", "this", "these"], "that"),
    ("Are _____ your sneakers near the door?", ["these", "this", "that"], "these"),
    ("Look at _____ high boots over there!", ["those", "this", "these"], "those"),
    ("He _____ a black jacket today.", ["is wearing", "wearing", "is wear"], "is wearing"),
    ("They _____ casual clothes to the park.", ["are wearing", "is wearing", "wears"], "are wearing"),
    ("How much _____ that digital watch?", ["is", "are", "does"], "is"),
    ("_____ shoes are too small for me.", ["These", "This", "That"], "These"),
    ("Excuse me, how much _____ these sunglasses?", ["are", "is", "was"], "are"),
    ("What color is _____ hat you are holding?", ["this", "those", "these"], "this"),
    ("She _____ wearing a winter coat because it's warm.", ["isn't", "aren't", "don't"], "isn't"),
    ("Can I try on _____ pants over there?", ["those", "this", "these near"], "those")
]

u7_listening_title = "Listening: In the Clothes Store"
u7_listening_items = [
    ("Look at that coat! It is red and very stylish. How much is it? It's $80.", "How much is the red coat?", ["$50", "$80", "$100"], 1),
    ("What is Sarah wearing today? She is wearing a green dress and brown shoes.", "What is Sarah wearing?", ["A blue shirt and pants", "A green dress and brown shoes", "A black skirt"], 1),
    ("Excuse me, do you have these jeans in size Small? Yes, here they are.", "What size does the customer want?", ["Small", "Medium", "Large"], 0),
    ("Is this jacket on sale? Yes! There is a 20 percent discount.", "Is the jacket on sale?", ["Yes, 20% discount", "No, full price", "It is free"], 0),
    ("Where can I try on these pants? The fitting room is on the left.", "Where is the fitting room?", ["On the right", "On the left", "Upstairs"], 1),
    ("I want to buy these three shirts. That will be $60 in total.", "How much are the three shirts?", ["$40", "$60", "$80"], 1),
    ("Can I pay by credit card? Yes, we accept all major cards.", "How is the customer paying?", ["By cash", "By credit card", "By check"], 1),
    ("These sneakers are very cheap! They only cost fifteen dollars.", "How much do the sneakers cost?", ["$15", "$50", "$5"], 0),
    ("Look at those boots over there! They look very expensive.", "What looks expensive?", ["The boots over there", "The socks", "The hat"], 0),
    ("What color is David's shirt? He is wearing a dark blue shirt.", "What color is David's shirt?", ["Light red", "Dark blue", "White"], 1),
    ("Here is your change and your receipt. Have a great day!", "What does the clerk hand the customer?", ["Change and receipt", "A new bag", "A credit card"], 0),
    ("This yellow hat costs nine dollars.", "How much is the yellow hat?", ["$9", "$19", "$90"], 0),
    ("I need a large size coat because it's cold.", "What size coat is needed?", ["Small", "Large", "Medium"], 1),
    ("The fitting room is currently occupied.", "Is the fitting room free?", ["Yes", "No, it's occupied", "Not sure"], 1),
    ("She bought two pairs of socks.", "How many pairs of socks did she buy?", ["One pair", "Two pairs", "Three pairs"], 1)
]

u7_oral_title = "Oral Drills: Clothes & Shopping"
u7_oral_items = [
    ("How much is this blue jacket?", "Asking price for singular item."),
    ("How much are these leather shoes?", "Asking price for plural item."),
    ("She is wearing a beautiful red dress.", "Present Continuous clothing drill."),
    ("He is wearing jeans and a white T-shirt.", "Describing everyday outfits."),
    ("Can I try this sweater on in the fitting room?", "Asking permission to try clothes."),
    ("Do you have this shirt in size Large?", "Inquiring about clothing size."),
    ("This hat is very cheap, only ten dollars.", "Using adjective 'cheap'."),
    ("That leather coat is too expensive for me.", "Using adjective 'expensive'."),
    ("I would like to pay by credit card.", "Stating payment method."),
    ("Keep your receipt for any clothing returns.", "Vocabulary practice 'receipt'."),
    ("Look at those boots over there on the shelf.", "Demonstrative 'those' drill."),
    ("I love this soft scarf around my neck.", "Demonstrative 'this' drill."),
    ("What size are you looking for today?", "Clerk question drill."),
    ("There is a big discount on winter clothes.", "Shopping phrase drill."),
    ("Thank you for shopping with us today!", "Customer service farewell.")
]

u7_reading_title = "Reading: Shopping at the Mall"
u7_reading_text = "Saturday is shopping day for Maria and her sister Anna. Today, they are visiting the Grand City Mall. The mall is very busy. Maria is looking for a new outfit for her friend's birthday party. She finds a pink dress that costs $40. She goes to the fitting room to try it on. It fits perfectly! Anna wants a pair of comfortable shoes. She sees white sneakers on sale for $30. They buy the clothes, pay the cashier with a credit card, and get their receipts. They are very happy with their new purchases!"
u7_reading_items = [
    ("What day do Maria and Anna go shopping?", ["Friday", "Saturday", "Sunday"], 1),
    ("Which mall are they visiting?", ["Grand City Mall", "Outlet Plaza", "Metro Mall"], 0),
    ("Why is Maria looking for a new outfit?", ["For work", "For her friend's birthday party", "For school"], 1),
    ("What color dress does Maria find?", ["Blue", "Pink", "Yellow"], 1),
    ("How much does the dress cost?", ["$30", "$40", "$50"], 1),
    ("Where does Maria try on the dress?", ["In the car", "In the fitting room", "In the restaurant"], 1),
    ("Does the dress fit Maria?", ["No, it's too big", "Yes, it fits perfectly", "No, it's too small"], 1),
    ("What does Anna want to buy?", ["A dress", "Comfortable shoes", "A coat"], 1),
    ("What type of shoes does Anna see?", ["Black boots", "White sneakers", "Red sandals"], 1),
    ("How much do the sneakers cost?", ["$20", "$30", "$60"], 1),
    ("How do they pay the cashier?", ["In cash", "With a credit card", "With a check"], 1),
    ("What do they receive after paying?", ["Receipts", "Free gifts", "Coupons"], 0),
    ("How do they feel at the end?", ["Tired", "Sad", "Very happy"], 2),
    ("Is the mall quiet or busy?", ["Quiet", "Very busy", "Empty"], 1),
    ("Who goes shopping with Maria?", ["Her mother", "Her sister Anna", "Her friend"], 1)
]

u7_writing_title = "Writing & Sentence Structure: Shopping Expressions"
u7_writing_items = [
    ("Complete: She _____ wearing a green coat today.", ["is", "are", "am"], "is"),
    ("Fill in: How much _____ these denim jeans?", ["are", "is", "be"], "are"),
    ("Fill in: How much _____ that red hat?", ["is", "are", "were"], "is"),
    ("Complete: Look at _____ shoes in my hand.", ["these", "those", "that"], "these"),
    ("Fill in: Can I try this shirt on in the _____ room?", ["fitting", "living", "dining"], "fitting"),
    ("Complete: He is _____ black sneakers right now.", ["wearing", "wear", "wears"], "wearing"),
    ("Fill in: I would like to pay in _____.", ["cash", "money paper", "coin"], "cash"),
    ("Complete: That coat is $200! It is very _____.", ["expensive", "cheap", "small"], "expensive"),
    ("Fill in: This T-shirt is only $5! It is very _____.", ["cheap", "expensive", "costly"], "cheap"),
    ("Complete: What _____ are you? I am a Size Medium.", ["size", "color", "long"], "size"),
    ("Fill in: Don't forget to get your _____ from the cashier.", ["receipt", "tag", "button"], "receipt"),
    ("Complete: Look at _____ hat on the high shelf over there.", ["that", "this", "these"], "that"),
    ("Fill in: _____ are my favorite pair of socks.", ["These", "This", "That"], "These"),
    ("Complete: They _____ wearing winter jackets.", ["are", "is", "am"], "are"),
    ("Fill in: There is a 50 percent _____ on summer dresses.", ["discount", "cost", "price"], "discount")
]

u7_quiz_title = "Unit 7 Review: Clothes & Shopping"
u7_quiz_items = [
    ("What garment do you wear on your feet inside shoes?", ["Socks", "Gloves", "Hats"], 0, "Socks are worn on feet."),
    ("Complete: She _____ a pretty red dress right now.", ["is wearing", "wears", "wearing"], 0, "Present continuous for present action."),
    ("How do you ask the price of plural items like jeans?", ["How much are these jeans?", "How much is these jeans?", "How many is these jeans?"], 0, "'Jeans' is plural so use 'are'."),
    ("Where do you try on clothing in a store?", ["Fitting room", "Kitchen", "Office"], 0, "Fitting room is for trying on clothes."),
    ("What plastic card is used for electronic payment?", ["Credit card", "Library card", "Business card"], 0, "Credit card pays electronically."),
    ("Opposite of 'expensive' is:", ["Cheap", "Costly", "High"], 0, "Cheap means low in price."),
    ("Complete: Look at _____ sweater right here.", ["this", "those", "these"], 0, "Singular item near speaker is 'this'."),
    ("Complete: Look at _____ shoes over there across the room.", ["those", "this", "these"], 0, "Plural items far from speaker are 'those'."),
    ("What paper proves you paid for an item?", ["Receipt", "Price tag", "Ticket"], 0, "Receipt is proof of payment."),
    ("Complete: What size do you need? I need size _____.", ["Medium (M)", "Blue", "Dollar"], 0, "Medium is a standard clothing size."),
    ("Complete: They _____ wearing raincoats because of the storm.", ["are", "is", "am"], 0, "'They' takes 'are' in continuous tense."),
    ("What label shows how much something costs?", ["Price tag", "Receipt", "Sleeve"], 0, "Price tag shows cost."),
    ("Complete: How much _____ that gold watch?", ["is", "are", "were"], 0, "Gold watch is singular so use 'is'."),
    ("Which footwear is typically worn for sports?", ["Sneakers", "High heels", "Boots"], 0, "Sneakers are athletic shoes."),
    ("Complete: He is wearing a blue shirt and black _____.", ["pants", "jacket singular", "dress"], 0, "Pants complete the outfit.")
]


# ==========================================
# UNIT 8: FREE TIME, HOBBIES & ROUTINE
# ==========================================
u8_culture_title = "Free Time and Hobbies"
u8_culture_notes = "Americans enjoy spending their free time outdoors or doing sports like baseball, basketball, and running. On weekends, people often meet friends for brunch, work on gardening projects, or relax with hobbies like cooking and photography."
u8_dialogue_lines = [
    ("Alex", "What do you usually do on weekends, Sam?"),
    ("Sam", "I usually play soccer on Saturday morning and read books on Sunday."),
    ("Alex", "Nice! Do you like watching movies?"),
    ("Sam", "Yes! I love watching action movies with my family.")
]
u8_video_url = "https://www.youtube.com/watch?v=xOcmG4H3K20"
u8_video_text = "Watch VOA Learning English Lesson 8 on YouTube"

u8_vocab_cat1 = "Hobbies & Activities"
u8_vocab_items1 = [
    ("Reading books", "Looking at and understanding written words", "I enjoy reading novels before sleeping.", "📚"),
    ("Playing soccer", "Kicking a ball to score goals in teams", "He plays soccer every Saturday.", "⚽"),
    ("Listening to music", "Enjoying audio songs and tunes", "She loves listening to jazz music.", "🎧"),
    ("Cooking dinner", "Preparing food for meals", "My father likes cooking dinner.", "🍳"),
    ("Watching movies", "Viewing films at home or cinema", "We watch movies on Friday nights.", "🎬"),
    ("Swimming", "Moving through water using arms and legs", "Swimming is great exercise.", "🏊"),
    ("Running / Jogging", "Running at a steady pace for fitness", "He goes running in the park.", "🏃"),
    ("Gardening", "Growing flowers and plants", "My grandmother enjoys gardening.", "🪴"),
    ("Playing guitar", "Making music with a string instrument", "He is learning to play the guitar.", "🎸"),
    ("Traveling", "Visiting new cities or countries", "They love traveling in the summer.", "✈️")
]

u8_vocab_cat2 = "Frequency & Time Words"
u8_vocab_items2 = [
    ("Always (100%)", "At all times; without exception", "I always drink coffee in the morning.", "💯"),
    ("Usually (80%)", "Under normal conditions; generally", "She usually walks to work.", "📊"),
    ("Often (60%)", "Frequently; many times", "We often go to the beach.", "🌊"),
    ("Sometimes (50%)", "Occasionally; on some occasions", "He sometimes eats fast food.", "⚖️"),
    ("Hardly ever (10%)", "Almost never; rarely", "They hardly ever watch TV.", "⏳"),
    ("Never (0%)", "Not at any time; not ever", "I never drink soda.", "🚫"),
    ("Every day", "Daily; each day of the week", "She practices piano every day.", "📅"),
    ("On weekends", "On Saturday and Sunday", "What do you do on weekends?", "🗓️"),
    ("Once a week", "One time during a 7-day period", "I play tennis once a week.", "1️⃣"),
    ("In the evening", "During the late afternoon/night hours", "We relax in the evening.", "🌆")
]

u8_grammar_rules = [
    ("Adverbs of Frequency Position", "Place adverbs before main verbs, but AFTER the verb to be.", "I always read books. She is usually happy."),
    ("Verbs of Liking + -ing", "After like, love, enjoy, hate, use verb+ing.", "I love playing soccer. She enjoys cooking dinner."),
    ("Questions about Routine", "How often do you...? / What do you do on...?", "How often do you go swimming? What do you do on weekends?")
]

u8_grammar_ex = [
    ("I _____ drink coffee in the morning. (100%)", ["always", "never", "sometimes"], "always"),
    ("She enjoys _____ to music in her bedroom.", ["listening", "listen", "listened"], "listening"),
    ("They _____ play soccer on Sundays. (80%)", ["usually", "never", "hardly"], "usually"),
    ("How _____ do you go to the gym?", ["often", "many", "much"], "often"),
    ("He loves _____ books about history.", ["reading", "read", "reads"], "reading"),
    ("We _____ eat fast food. (0%)", ["never", "always", "often"], "never"),
    ("She is _____ late for school.", ["sometimes", "sometimes is", "never is"], "sometimes"),
    ("Do you like _____ in the ocean?", ["swimming", "swim", "swam"], "swimming"),
    ("They hate _____ in the rain.", ["running", "run", "ran"], "running"),
    ("I play tennis _____ a week.", ["once", "one", "first"], "once"),
    ("What do you do _____ weekends?", ["on", "in", "to"], "on"),
    ("She _____ goes to bed before 10 PM. (60%)", ["often", "never", "hardly"], "often"),
    ("My father enjoys _____ dinner for the family.", ["cooking", "cook", "cooks"], "cooking"),
    ("How often _____ you watch movies?", ["do", "are", "does"], "do"),
    ("He _____ ever plays video games.", ["hardly", "never", "always"], "hardly")
]

u8_listening_title = "Listening: Hobbies & Free Time"
u8_listening_items = [
    ("What does Mark do in his free time? He always goes running in the park every morning.", "What does Mark do every morning?", ["He plays guitar", "He goes running in the park", "He sleeps"], 1),
    ("Do you like playing basketball? No, I prefer swimming.", "What activity does the speaker prefer?", ["Basketball", "Swimming", "Soccer"], 1),
    ("How often does Emily travel? She travels twice a year.", "How often does Emily travel?", ["Once a week", "Twice a year", "Never"], 1),
    ("My sister loves cooking Italian pasta on weekends.", "What does the sister love doing on weekends?", ["Cooking Italian pasta", "Reading comic books", "Watching TV"], 0),
    ("Do you ever listen to classical music? Yes, I listen to classical music every night.", "When does the speaker listen to classical music?", ["Every night", "Never", "On Mondays only"], 0),
    ("John hardly ever watches television.", "How often does John watch TV?", ["Always", "Hardly ever", "Every day"], 1),
    ("What is your favorite weekend activity? I enjoy gardening in my backyard.", "What is the favorite activity?", ["Gardening in the backyard", "Shopping", "Playing video games"], 0),
    ("She is learning to play the acoustic guitar.", "What instrument is she learning?", ["Piano", "Acoustic guitar", "Drums"], 1),
    ("Do they play soccer together? Yes, they play soccer every Tuesday afternoon.", "When do they play soccer?", ["Every Tuesday afternoon", "On Sundays", "Every morning"], 0),
    ("I love reading detective stories.", "What genre of books does the speaker love?", ["Detective stories", "Cookbooks", "Math books"], 0),
    ("How often do you clean your room? I clean it once a week.", "How often is the room cleaned?", ["Every day", "Once a week", "Once a month"], 1),
    ("We usually watch movies together on Friday nights.", "What day do they watch movies?", ["Wednesday", "Friday nights", "Sunday mornings"], 1),
    ("He hates running in cold weather.", "Does he like running in cold weather?", ["Yes, he loves it", "No, he hates it", "He doesn't mind"], 1),
    ("She goes swimming at the community pool three times a week.", "Where does she swim?", ["At the beach", "At the community pool", "At home"], 1),
    ("They always eat breakfast together at 8 AM.", "What time do they eat breakfast?", ["7 AM", "8 AM", "9 AM"], 1)
]

u8_oral_title = "Oral Drills: Talking About Free Time"
u8_oral_items = [
    ("I always drink coffee in the morning.", "Adverb of frequency 'always' drill."),
    ("She usually reads books on weekends.", "Adverb of frequency 'usually' drill."),
    ("Do you like listening to pop music?", "Question format with 'like + -ing'."),
    ("Yes, I love listening to music!", "Affirmative answer with 'love + -ing'."),
    ("How often do you go to the gym?", "Wh-question 'How often' drill."),
    ("I go swimming twice a week.", "Expressing frequency 'twice a week'."),
    ("My father enjoys cooking dinner.", "Practice 'enjoys + -ing'."),
    ("They hate waiting in long lines.", "Practice 'hate + -ing'."),
    ("He hardly ever watches television.", "Practice 'hardly ever'."),
    ("We sometimes eat out at restaurants.", "Practice 'sometimes'."),
    ("What are your favorite hobbies?", "General hobby inquiry."),
    ("I love traveling to new places.", "Expressing passion for travel."),
    ("She plays the guitar very well.", "Describing musical skills."),
    ("Do you go running every morning?", "Routine inquiry drill."),
    ("Never say never when trying new hobbies!", "Fun idiomatic drill.")
]

u8_reading_title = "Reading: David's Busy Weekend Routine"
u8_reading_text = "David is a high school teacher in Boston. He works hard during the week, so he loves his weekends! On Saturday morning, David always wakes up early at 7:00 AM and goes running along the Charles River. After running, he usually meets his friend Lisa at a local cafe for breakfast. In the afternoon, he enjoys working in his garden or reading mystery novels. On Sunday evenings, David and his family always watch a movie together and cook a delicious homemade dinner. He never works on Sundays because family time is important to him."
u8_reading_items = [
    ("What is David's profession?", ["High school teacher", "Doctor", "Engineer"], 0),
    ("In which city does David live?", ["Boston", "New York", "Chicago"], 0),
    ("What time does he wake up on Saturday morning?", ["6:00 AM", "7:00 AM", "8:00 AM"], 1),
    ("Where does he go running?", ["Along the Charles River", "In the gym", "On the street"], 0),
    ("Who does he meet at the cafe for breakfast?", ["His friend Lisa", "His brother", "His students"], 0),
    ("What does he enjoy doing on Saturday afternoon?", ["Gardening or reading mystery novels", "Playing soccer", "Shopping"], 0),
    ("What does David's family do on Sunday evenings?", ["Watch a movie and cook dinner", "Go to the cinema", "Visit relatives"], 0),
    ("Does David work on Sundays?", ["Yes, always", "No, he never works on Sundays", "Sometimes"], 1),
    ("Why doesn't he work on Sundays?", ["Because family time is important", "Because he is tired", "Because school is open"], 0),
    ("How often does he wake up early on Saturday?", ["Always", "Sometimes", "Never"], 0),
    ("What genre of books does David read?", ["Mystery novels", "Science fiction", "History"], 0),
    ("Does David run before or after breakfast?", ["Before breakfast", "After breakfast", "At night"], 0),
    ("What meal does David eat with Lisa?", ["Breakfast", "Lunch", "Dinner"], 0),
    ("Does David like his weekends?", ["Yes, he loves his weekends", "No, he dislikes them", "He doesn't care"], 0),
    ("What does David cook on Sunday evening?", ["A delicious homemade dinner", "Fast food", "Breakfast"], 0)
]

u8_writing_title = "Writing & Sentence Structure: Routine & Hobbies"
u8_writing_items = [
    ("Complete: I _____ (100%) eat breakfast at 8 AM.", ["always", "never", "rarely"], "always"),
    ("Fill in: She loves _____ to classical music.", ["listening", "listen", "listened"], "listening"),
    ("Complete: They _____ (0%) arrive late for class.", ["never", "always", "often"], "never"),
    ("Fill in: How _____ do you practice the piano?", ["often", "many", "long"], "often"),
    ("Complete: He enjoys _____ soccer with friends.", ["playing", "play", "plays"], "playing"),
    ("Fill in: We go swimming _____ a week on Saturdays.", ["once", "one", "first"], "once"),
    ("Complete: My mother _____ (80%) cooks dinner.", ["usually", "never", "seldom"], "usually"),
    ("Fill in: Do you like _____ books in English?", ["reading", "read", "reads"], "reading"),
    ("Complete: They hate _____ up early on Sundays.", ["waking", "wake", "woke"], "waking"),
    ("Fill in: I go jogging _____ the morning.", ["in", "on", "at"], "in"),
    ("Complete: She is _____ (50%) happy on Mondays.", ["sometimes", "never", "always"], "sometimes"),
    ("Fill in: What do you do _____ weekends?", ["on", "in", "to"], "on"),
    ("Complete: We _____ (60%) watch movies on Friday.", ["often", "never", "hardly"], "often"),
    ("Fill in: He enjoys _____ photos of nature.", ["taking", "take", "takes"], "taking"),
    ("Complete: They _____ ever go to bed after midnight.", ["hardly", "never", "always"], "hardly")
]

u8_quiz_title = "Unit 8 Review: Free Time & Hobbies"
u8_quiz_items = [
    ("Which adverb of frequency means 100% of the time?", ["Always", "Never", "Sometimes"], 0, "'Always' means 100% frequency."),
    ("Complete: She loves _____ tennis on weekends.", ["playing", "play", "plays"], 0, "Use verb-ing after 'loves'."),
    ("Which adverb means 0% of the time?", ["Never", "Always", "Often"], 0, "'Never' means 0% frequency."),
    ("Complete: How _____ do you go running?", ["often", "much", "many"], 0, "'How often' asks about frequency."),
    ("Where does the adverb of frequency go in a simple sentence?", ["Before the main verb", "After the main verb", "At the very end"], 0, "Adverbs go before main verbs."),
    ("Complete: I enjoy _____ meals for my family.", ["cooking", "cook", "cooked"], 0, "Use verb-ing after 'enjoy'."),
    ("What hobby involves kicking a ball into a goal?", ["Playing soccer", "Reading", "Gardening"], 0, "Soccer involves kicking a ball."),
    ("Complete: We watch movies _____ Friday nights.", ["on", "in", "at"], 0, "We say 'on Friday nights'."),
    ("Complete: They _____ (80%) walk to school.", ["usually", "never", "rarely"], 0, "'Usually' represents ~80% frequency."),
    ("What hobby involves growing flowers and plants?", ["Gardening", "Swimming", "Running"], 0, "Gardening is growing plants."),
    ("Complete: He hates _____ in long traffic jams.", ["waiting", "wait", "waited"], 0, "Use verb-ing after 'hates'."),
    ("How do you say 'one time in a week'?", ["Once a week", "One week", "First week"], 0, "'Once a week' means 1 time per week."),
    ("Complete: She is _____ cheerful in the morning.", ["always", "always is", "never is"], 0, "Adverb goes AFTER the verb to be."),
    ("What hobby involves playing an instrument with strings?", ["Playing guitar", "Reading", "Swimming"], 0, "Guitar is a stringed instrument."),
    ("Complete: I hardly _____ watch horror movies.", ["ever", "never", "always"], 0, "'Hardly ever' means almost never.")
]


# ==========================================
# UNIT 9: ABILITIES, TALENTS & SKILLS
# ==========================================
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


# ==========================================
# UNIT 10: TRAVEL, HOLIDAYS & PAST EVENTS
# ==========================================
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

print("Constructing HTML string for Units 5 through 10...")

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

print("All 6 units built in memory! Reading index.html...")

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

pattern = r'<div id="unit-5"[\s\S]*?(?=<div id="unit-11")'
combined_units_html = u5_html + "\n\n" + u6_html + "\n\n" + u7_html + "\n\n" + u8_html + "\n\n" + u9_html + "\n\n" + u10_html + "\n\n"

if re.search(pattern, html):
    html = re.sub(pattern, combined_units_html, html)
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("SUCCESS: index.html updated with complete Units 5, 6, 7, 8, 9, 10!")
else:
    print("ERROR: Could not find <div id='unit-5'... in index.html")
