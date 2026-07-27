import random
from datetime import datetime

# ==========================
# Rule-Based AI Chatbot
# DecodeLabs Internship Project
# ==========================

print("=" * 60)
print("          Rule-Based AI Chatbot")
print("=" * 60)
print("Type 'help' to see available commands.")
print("Type 'bye' to exit.\n")

# Responses
greetings = [
    "Hello! How can I help you?",
    "Hi! Nice to meet you.",
    "Hey! What can I do for you?"
]

how_are_you = [
    "I'm doing great. Thanks for asking!",
    "I'm fine. Hope you are doing well too!",
    "Everything is going well!"
]

goodbye = [
    "Goodbye!",
    "Have a wonderful day!",
    "See you again!"
]

thanks = [
    "You're welcome!",
    "Happy to help!",
    "Anytime!"
]

jokes = [
    "Why did the computer go to the doctor? Because it caught a virus!",
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Debugging is like being a detective in a crime movie."
]

motivation = [
    "Believe in yourself.",
    "Keep learning every day.",
    "Success comes from consistency.",
    "Never stop improving yourself."
]


def show_help():
    print("\n========== Available Commands ==========")
    print("hello / hi / hey")
    print("how are you")
    print("your name")
    print("who created you")
    print("date")
    print("time")
    print("joke")
    print("motivate me")
    print("thanks")
    print("help")
    print("bye")
    print("========================================\n")


while True:

    user = input("You : ").strip().lower()

    if user == "":
        print("Bot : Please type something.\n")

    elif user in ["hello", "hi", "hey"]:
        print("Bot :", random.choice(greetings), "\n")

    elif user in ["how are you", "how are u"]:
        print("Bot :", random.choice(how_are_you), "\n")

    elif user in ["your name", "who are you"]:
        print("Bot : I am a Rule-Based AI Chatbot.\n")

    elif user == "who created you":
        print("Bot : I was created by Md. Ibna Labid.\n")

    elif user == "date":
        print("Bot :", datetime.now().strftime("%d-%m-%Y"), "\n")

    elif user == "time":
        print("Bot :", datetime.now().strftime("%I:%M:%S %p"), "\n")

    elif user == "joke":
        print("Bot :", random.choice(jokes), "\n")

    elif user == "motivate me":
        print("Bot :", random.choice(motivation), "\n")

    elif user in ["thanks", "thank you"]:
        print("Bot :", random.choice(thanks), "\n")

    elif user == "help":
        show_help()

    elif user in ["bye", "exit", "quit"]:
        print("Bot :", random.choice(goodbye))
        print("Bot : Chat ended successfully.")
        break

    else:
        print("Bot : Sorry! I don't understand that.\n")