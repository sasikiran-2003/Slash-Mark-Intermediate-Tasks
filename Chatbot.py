import nltk
import random
from nltk.chat.util import Chat, reflections

# Define patterns for matching user inputs and corresponding responses
patterns = [
    (r"hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]),
    (r"how are you?", ["I'm doing well, thank you!", "I'm good, thanks for asking."]),
    (r"what's your name?", ["I'm a chatbot created by OpenAI.", "You can call me ChatGPT."]),
    (r"what's the weather like today?", ["I'm not sure. You can check a weather website for that!"]),
    (r"bye|goodbye", ["Goodbye!", "See you later!", "Bye!"]),
]

# Create a Chat instance
chatbot = Chat(patterns, reflections)

# Start the conversation
print("Welcome! How can I assist you today?")
while True:
    user_input = input("You: ")
    response = chatbot.respond(user_input)
    print("Bot:", response)
