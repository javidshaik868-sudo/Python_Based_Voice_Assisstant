import streamlit as st
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pywhatkit

# -----------------------------
# IMPORTANT:
# Save only ONE file with this code.
# Delete old duplicate code below it.
# -----------------------------

st.set_page_config(
    page_title="Kicky Voice Assistant",
    page_icon="🎤",
    layout="centered"
)

# Voice engine
engine = pyttsx3.init()

def speak(text):
    st.success(text)
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        st.info("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        command = command.lower()
        st.write("You said:", command)
        return command
    except:
        st.error("Voice not recognized")
        return ""

def run_assistant():
    command = take_command()

    if "time" in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak("Current time is " + now)

    elif "date" in command:
        today = datetime.datetime.now().strftime("%d %B %Y")
        speak("Today's date is " + today)

    elif "google" in command:
        webbrowser.open("https://google.com")
        speak("Opening Google")

    elif "youtube" in command:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube")

    elif "play" in command:
        song = command.replace("play", "")
        pywhatkit.playonyt(song)
        speak("Playing " + song)

    elif "wikipedia" in command:
        topic = command.replace("wikipedia", "")
        result = wikipedia.summary(topic, sentences=2)
        speak(result)

    else:
        speak("Command not found")

# -----------------------------
# UI
# -----------------------------
st.title("🎙️ Kicky Voice Assistant")
st.write("Click button and speak")

# UNIQUE BUTTON
start = st.button("Start Listening", key="unique_button_12345")

if start:
    run_assistant()