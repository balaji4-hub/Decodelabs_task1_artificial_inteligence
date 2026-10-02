# ============================================
# Project 1: Rule-Based AI Chatbot
# DecodeLabs - Artificial Intelligence
# ============================================


# --------------------------------------------
# 1. KNOWLEDGE BASE
# --------------------------------------------
# This dictionary contains predefined
# questions/intents and their responses.

responses = {
    "hello": "Hi! How can I help you?",
    "hi": "Hello! Nice to meet you.",
    "how are you": "I'm doing great! Thanks for asking.",
    "what is ai": "AI stands for Artificial Intelligence.",
    "what can you do": "I can answer simple predefined questions.",
    "help": "Sure! You can ask me about AI or say hello.",
    "thank you": "You're welcome!",
    "good morning": "Good morning! Have a great day!"
}


# --------------------------------------------
# 2. WELCOME MESSAGE
# --------------------------------------------

print("======================================")
print("       RULE-BASED AI CHATBOT")
print("======================================")
print("Bot: Hello! I am your AI chatbot.")
print("Bot: You can ask me simple questions.")
print("Bot: Type 'bye', 'exit', or 'quit' to stop.")
print("--------------------------------------")


# --------------------------------------------
# 3. CONTINUOUS CHAT LOOP
# --------------------------------------------

while True:

    # Get input from the user
    raw_input = input("You: ")

    # ----------------------------------------
    # 4. INPUT SANITIZATION
    # ----------------------------------------
    # Convert input to lowercase
    # and remove extra spaces.

    user_input = raw_input.lower().strip()


    # ----------------------------------------
    # 5. EXIT CONDITION
    # ----------------------------------------

    if user_input in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a great day!")
        break


    # ----------------------------------------
    # 6. LOOK UP THE RESPONSE
    # ----------------------------------------
    # .get() searches for the user's input
    # in the dictionary.
    #
    # If the input exists:
    #     return the matching response.
    #
    # If it doesn't exist:
    #     return the fallback message.

    reply = responses.get(
        user_input,
        "Sorry, I don't understand that."
    )


    # ----------------------------------------
    # 7. DISPLAY RESPONSE
    # ----------------------------------------

    print("Bot:", reply)
    responses = {

    # Greetings
    "hello": "Hi! How can I help you today?",
    "hi": "Hello! Nice to meet you!",
    "hey": "Hey there! What would you like to know?",
    "good morning": "Good morning! I hope you're having a great day.",
    "good afternoon": "Good afternoon! How can I help you?",
    "good evening": "Good evening! What can I do for you?",

    # About the chatbot
    "who are you": "I am a simple rule-based AI chatbot created using Python.",
    "what is your name": "You can call me AI Buddy!",
    "what can you do": "I can answer predefined questions and have a simple conversation with you.",
    "what do you do": "I respond to questions using predefined rules and a dictionary.",
    "are you ai": "Yes! I am a basic rule-based AI chatbot.",
    "how do you work": "I compare your input with predefined rules and return the matching response.",

    # AI questions
    "what is ai": "AI stands for Artificial Intelligence. It enables computers to perform tasks that normally require human intelligence.",
    "what is artificial intelligence": "Artificial Intelligence is the field of creating systems that can perform tasks requiring human-like intelligence.",
    "what is machine learning": "Machine Learning is a branch of AI where systems learn patterns from data.",
    "what is chatbot": "A chatbot is a program designed to communicate with users through text or speech.",
    "what is python": "Python is a popular programming language known for its simple and readable syntax.",
    "what is programming": "Programming is the process of writing instructions that tell a computer what to do.",

    # Project-related questions
    "what is rule based ai": "Rule-based AI uses predefined rules to decide what response to give.",
    "what is a rule based chatbot": "A rule-based chatbot responds using predefined rules rather than learning from conversations.",
    "what is a dictionary": "A dictionary in Python stores data as key-value pairs.",
    "what is a key": "A key is the identifier used to access a value in a Python dictionary.",
    "what is a value": "A value is the information associated with a key in a dictionary.",
    "what is a loop": "A loop allows a program to repeatedly execute a block of code.",
    "what is while loop": "A while loop repeatedly executes code as long as its condition is true.",
    "what is if else": "If-else statements allow a program to make decisions based on conditions.",

    # Conversation
    "how are you": "I'm doing great! Thanks for asking. How are you?",
    "i am fine": "That's great to hear!",
    "i am good": "Awesome! I'm glad you're doing well.",
    "i am happy": "That's wonderful! Keep that positive energy going.",
    "i am sad": "I'm sorry to hear that. I hope things get better soon.",
    "i am tired": "You should take a short break and get some rest.",

    # Help
    "help": "Sure! You can ask me about AI, Python, chatbots, programming, or this project.",
    "what can i ask": "You can ask me about AI, Python, programming, rule-based systems, or chatbots.",
    "give me an example": "Try asking me: 'What is AI?' or 'What is Python?'",
    "tell me something": "Here's something interesting: Python is widely used in AI and data science.",

    # Politeness
    "thank you": "You're very welcome!",
    "thanks": "No problem! Happy to help.",
    "thank you so much": "You're very welcome! 😊",
    "please": "Of course! What would you like to know?",

    # Fun conversation
    "are you human": "No, I'm a computer program created using Python.",
    "do you sleep": "No! I'm a program, so I don't need to sleep.",
    "do you have feelings": "I don't have real feelings, but I can respond to conversations.",
    "do you like python": "Yes! Python is perfect for building beginner-friendly AI projects.",
    "tell me a joke": "Why did the programmer quit his job? Because he didn't get arrays! 😄",

    # Closing
    "goodbye": "Goodbye! It was nice talking with you.",
    "see you": "See you later! Have a great day.",
}