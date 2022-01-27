import os
from datetime import date, datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import time
import webbrowser

def speak(text):
    print("Robot: " + text)
    speaker = pyttsx3.init()
    voices = speaker.getProperty("voices")
    speaker.setProperty("voice", voices[1].id) 
    speaker.setProperty('rate', 175) 
    speaker.say(text)
    speaker.runAndWait()


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as mic:
        r.adjust_for_ambient_noise(mic)
        print("I'm listening...")
        audio = r.listen(mic)
        said = ""
    try:
        said = r.recognize_google(audio)
        print("You said: " + said)
    except Exception:
        said = ""
    return said

def wishMe():
    hour = int(datetime.now().hour)
    if hour >= 0  and hour < 12:
        speak("Good Morning, What can I do for you?")
    elif hour >=12 and hour <18:
        speak("Good Afternoon, What can I do for you?")
    else:
        speak("Good Evening, What can I do for you?")        

def get_date():
    today = date.today()
    rep = today.strftime("%B %d, %Y")
    return rep

def get_time():
    now = datetime.now()
    rep = now.strftime("%H:%M")
    return rep

if __name__=='__main__':
    wishMe()
    while True:
        text = get_audio().lower()
        if 'wikipedia' in text:
            speak('Searching Wikipedia...')
            text =text.replace("wikipedia", "")
            rep = wikipedia.summary(text, sentences=3)
            speak("According to Wikipedia...")
            speak(rep)

        elif 'open youtube' in text:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now.")
            time.sleep(5)

        elif 'open google' in text:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now.")
            time.sleep(5)

        elif 'open gmail' in text:
            webbrowser.open_new_tab("https://gmail.com")
            speak("Google Mail open now.")
            time.sleep(5)

        elif 'news' in text:
            news = webbrowser.open_new_tab("https://www.nzherald.co.nz")
            speak('Here are news of New Zealand today.')
            time.sleep(6)

        elif 'search' in text:
            text = text.replace("search", "")
            webbrowser.open_new_tab(text)
            time.sleep(5)    
        
        elif ("day" in text) or ("date" in text):
            today = date.today()
            rep = today.strftime("%B %d, %Y") 
            speak(rep)
        
        elif "time" in text:
            now = datetime.now()
            rep = now.strftime("%H:%M")
            speak(rep)

        elif "thanks" in text or "thank you" in text:
            speak("No problem.")

        elif "bye" in text or "stop" in text:
            speak("Goodbye, Have a good day!")
            break
        else:
            speak("I don't understand, can you say again?")     
