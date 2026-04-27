import sounddevice as sd
import numpy as np
import speech_recognition as sr
import pyttsx3
from datetime import datetime

engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    fs = 16000
    seconds = 5

    print("Listening... Speak now!")

    try:
        recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
        sd.wait()
        sd.stop()  # 🔥 release mic immediately
    except Exception as e:
        print("Mic error:", e)
        return ""

    recording = np.int16(recording * 32767)

    r = sr.Recognizer()

    try:
        audio = sr.AudioData(recording.tobytes(), fs, 2)
        text = r.recognize_google(audio)
        print("You:", text)
        return text.lower()
    except Exception as e:
        print("Error:", e)
        speak("Sorry, I didn't catch that.")
        return ""

def process(command):
    if not command:
        return

    if "hello" in command:
        speak("Hi, how can I help you?")

    elif "time" in command:
        current_time = datetime.now().strftime("%H:%M")
        speak(f"The time is {current_time}")

    elif "date" in command or "day" in command:
        today = datetime.now().strftime("%A, %d %B %Y")
        speak(f"Today is {today}")

    elif "open youtube" in command:
        import webbrowser
        webbrowser.open("https://youtube.com")

    elif "open google" in command:
        import webbrowser
        webbrowser.open("https://google.com")

    elif "exit" in command or "stop" in command:
        speak("Goodbye!")
        return "exit"

    else:
        speak("I don't understand yet.")

speak("Assistant started")

while True:
    user_input = input("Press Enter to continue or type 'q' to quit: ")
    if user_input.lower() == "q":
        break

    cmd = listen()

    if cmd == "exit":
        break

    process(cmd)

sd.stop()
print("Program stopped. Mic released.")