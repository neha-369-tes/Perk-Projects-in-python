import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand that.")
        return ""
    except sr.RequestError:
        print("Could not request results, check your internet connection.")
        return ""

def voice_assistant():
    speak("Hello! How can I help you?")
    while True:
        command = recognize_speech()
        if "hello" in command:
            speak("Hello! How are you?")
        elif "time" in command:
            now = datetime.datetime.now().strftime("%H:%M")
            speak(f"The current time is {now}")
        elif "date" in command:
            today = datetime.date.today().strftime("%B %d, %Y")
            speak(f"Today's date is {today}")
        elif "search" in command:
            speak("What do you want to search for?")
            query = recognize_speech()
            if query:
                webbrowser.open(f"https://www.google.com/search?q={query}")
                speak(f"Here are the results for {query}")
        elif "exit" in command or "bye" in command:
            speak("Goodbye! Have a great day!")
            break
        else:
            speak("Sorry, I didn't understand that.")

if __name__ == "__main__":
    voice_assistant()
