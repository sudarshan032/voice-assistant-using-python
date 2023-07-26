import speech_recognition as sr
import pyttsx3
import datetime

def speak(text):
    """
    Function to convert text into speech using pyttsx3.

    Args:
        text (str): The text to be spoken.
    """
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    """
    Function to listen to user's voice input and convert it to text.

    Returns:
        str: The user's query in lowercase text.
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio).lower()
        print(f"User said: {query}")
        return query
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
        return ""
    except sr.RequestError:
        print("Sorry, I couldn't reach the Google Speech Recognition service.")
        return ""

def main():
    """
    The main function to run the voice assistant.

    The voice assistant greets the user and listens to their queries.
    It responds to specific queries like greetings, asking about its name,
    getting the current date, time, and an exit command to terminate the program.
    """
    speak("Hello! How can I assist you today?")

    while True:
        query = listen()

        if "hello" in query:
            speak("Hello there!")
        elif "how are you" in query:
            speak("I'm just a program, but thanks for asking!")
        elif "what's your name" in query:
            speak("I'm your Python voice assistant.")
        elif "date" in query:
            today = datetime.date.today().strftime("%B %d, %Y")
            speak(f"Today's date is {today}.")
        elif "time" in query:
            now = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {now}.")
        elif "exit" in query:
            speak("Goodbye!")
            break
        else:
            speak("Sorry, I don't have an answer for that.")

if __name__ == "__main__":
    main()
