import streamlit as st
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pywhatkit

# -------------------------
# Page Config
# -------------------------
st.set_page_config(page_title="🎙️ Kicky Voice Assistant", page_icon="🎤")

st.title("🎙️ Kicky Voice Assistant")
st.write("Click the button and speak your command.")

# -------------------------
# Voice Engine
# -------------------------
engine = pyttsx3.init()

def speak(text):
    st.success(text)
    engine.say(text)
    engine.runAndWait()

# -------------------------
# Voice Input
# -------------------------
def take_command():
    listener = sr.Recognizer()

    with sr.Microphone() as source:
        st.info("🎤 Listening...")
        listener.adjust_for_ambient_noise(source)
        audio = listener.listen(source)

    try:
        command = listener.recognize_google(audio)
        command = command.lower()
        st.write("🗣️ You said:", command)
        return command

    except:
        st.error("Could not understand voice.")
        return ""

# -------------------------
# Assistant Logic
# -------------------------
def run_kicky():
    command = take_command()

    if "time" in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak("Current time is " + time)

    elif "date" in command:
        date = datetime.datetime.now().strftime('%d %B %Y')
        speak("Today's date is " + date)

    elif "wikipedia" in command:
        topic = command.replace("wikipedia", "")
        speak("Searching Wikipedia")
        result = wikipedia.summary(topic, sentences=2)
        speak(result)

    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")

    elif "open google" in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google")

    elif "play" in command:
        song = command.replace("play", "")
        speak("Playing " + song)
        pywhatkit.playonyt(song)

    elif "stop" in command or "exit" in command:
        speak("Goodbye")

    else:
        speak("Please say again")

# -------------------------
# FIXED BUTTON (Unique Key)
# -------------------------
if st.button("🎤 Start Listening", key="listen_btn"):
    run_kicky()