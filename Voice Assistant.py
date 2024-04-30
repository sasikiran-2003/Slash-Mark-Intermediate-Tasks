import speech_recognition as sr
import pyttsx3

# Initialize speech recognition and text-to-speech engines
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to listen for user input
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        print("Recognizing...")
        user_input = recognizer.recognize_google(audio)
        print("You said:", user_input)
        return user_input.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError as e:
        print("Error fetching results from Google Speech Recognition service:", e)
        return ""

# Function to speak out responses
def speak(response):
    engine.say(response)
    engine.runAndWait()

# Function to perform tasks based on user input
def perform_task(user_input):
    if "hello" in user_input:
        speak("Hello! How can I assist you?")
    elif "goodbye" in user_input:
        speak("Goodbye! Have a great day!")
    # Add more task handling logic here based on user preferences

# Main function to run the voice assistant
def main():
    speak("Welcome! I'm your customizable voice assistant.")
    while True:
        user_input = listen()
        if "exit" in user_input:
            speak("Exiting voice assistant.")
            break
        perform_task(user_input)

if __name__ == "__main__":
    main()
