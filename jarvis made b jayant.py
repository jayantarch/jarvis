import pyttsx3 
import pyaudio
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import requests
from bs4 import BeautifulSoup 
import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis . Please tell me how may I help you")       

def takeCommand():
    

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        
         print("Say that again please...")  
         return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('jervis1411@gmail.com', 'jervisbyjayant')
    server.sendmail('jervis1411@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    
        query = takeCommand().lower()

        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            music_dir = 'C:\\Users\\jayan\\Desktop\\music'
            speak('playing music')
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            
        elif 'open spotify' in query:
            speak('opening spotify')
            codePath = "C:\\Users\\jayan\\AppData\\Local\\Microsoft\\WindowsApps\\Spotify.exe"
            os.startfile(codePath)

        elif 'email to Jayant' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "jayma1411@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")

           
            except Exception as e:
                # print(e)
                speak("Sorry jayant . I am not able to send this email. ")    
        
        elif 'temperature' in query:
            speak("checking current temperature of delhi")
            search = "temperature in delhi"
            url = f"https://www.google.com/search?q={search}"
            r= requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp= data.find("div",class_="BNeawe").text
            speak(f" current {search} is {temp}")
        
        elif 'tell me a joke' in query:
            
            joke= pyjokes.get_joke(language='en',category='all')
            speak(joke)
            