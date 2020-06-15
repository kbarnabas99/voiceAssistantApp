import pyttsx3                      
import speech_recognition as sr     
import datetime                     
import wikipedia
import webbrowser
import os
import smtplib

USER = "John"

#init voice engine
voiceEngine = pyttsx3.init("sapi5")
voices = voiceEngine.getProperty("voices")
voiceEngine.setProperty("voice",voices[0])

def speak(text):
    voiceEngine.say(text)
    voiceEngine.runAndWait()

def wishTheUser():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning" + USER)
    elif hour>=12 and hour<18:
        speak("Good Afternoon" + USER)
    else:
        speak("Good Evening"+ USER)
    speak("My name is Jarvis, how can i help you?")
    
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am listening...")
        audioFile = r.listen(source)
    try:
        print("Working on it")
        query = r.recognize_google(audioFile, language="en-uk")
        print(f"user said: {query}\n")
    except Exception as exp:
        speak("I coudn't recognize your command, say it again please")
        print("I coudn't recognize your command, say it again please")
        query = None
    return query

running = 1
wishTheUser()

while(running == 1):
    query = takeCommand()
    query = query.lower()

#with those if statements we are 
#searching for keywords in the voice input
if "wikipedia" in query:
    speak("Searching on wikipedia...")
    query = query.replace("wikipedia","")
    results = wikipedia.summary(query, sentences = 2)
    print(results)
    speak(results)

#it opens youtube in chrome
#we are using the chrome for searching, 
# if your want to use another browser just google it
elif "youtube" in query:
    url = "youtube.com"
    chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chrome_path).open(url)

#it opens google for the user
elif "google" in query:
    url = "google.com"
    chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chrome_path).open(url)








