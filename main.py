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
    
wishTheUser()















