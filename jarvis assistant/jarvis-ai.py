import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import os

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
        return None
    except sr.RequestError:
        print("Could not request results, check internet connection.")
        return None

def execute_command(command):
    if 'time' in command:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {current_time}")
    elif 'open youtube' in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif 'open google' in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif 'play music' in command:
        music_dir = "C:\\Users\\Public\\Music"  # Change to your music directory
        songs = os.listdir(music_dir)
        if songs:
            os.startfile(os.path.join(music_dir, songs[0]))
            speak("Playing music")
        else:
            speak("No music files found")
    elif 'exit' in command or 'stop' in command:
        speak("Goodbye! Have a great day!")
        exit()
    else:
        speak("sanjit is a good boy.")

if __name__ == "__main__":
    speak("Hello, I am Jarvis. How can I help you?")
    while True:
        user_command = listen()
        if user_command:
            execute_command(user_command)
