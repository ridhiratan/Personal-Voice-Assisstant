import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import math
from random import random
import smtplib



engine = pyttsx3.init('sapi5') #sapi5 is microsoft library we are using it for recognising voices
voices = engine.getProperty('voices') #cathes the voices

engine.setProperty('voice',voices[0].id) #using the male inbuilt voice


def speak(audio): #this is the function which will take the input of what we want jarvis to say
    engine.say(audio)#it will make jarvis say
    engine.runAndWait()


def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning")
    elif hour>=12 and hour<18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    speak('hello there, i am jarvis, a virtual AI assistant created by Ridhi. how may i help you')


def takecommand():
    #it takes microphone input from the user and returns string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 0.9
        r.energy_threshold=500
        audio=r.listen(source)
        
    try:
        print("Recognizing....")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")
        
    
    except Exception as e:
        print("Say that again please....")
        return "None"
    return query

def sendmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('xyz@gmail.com','xxxxx')
    server.sendmail('xyz@gmail.com',to,content)
    server.close()

if __name__=='__main__':
    wishme()
    while True:
        query = takecommand().lower()
        #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace('wikipedia','')
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
            
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'what' in query:
            k=query.index('what')
            webbrowser.open(f'google.com/search?q={query[k:]}')
            
        elif 'who' in query:
            k=query.index('who')
            webbrowser.open(f'google.com/search?q={query[k:]}')
            
        elif 'where' in query:
            k=query.index('where')
            webbrowser.open(f'google.com/search?q={query[k:]}')
        
        elif 'when' in query:
            k=query.index('when')
            webbrowser.open(f'google.com/search?q={query[k:]}')
            
        elif 'search youtube' in query:
            speak("what should i search buddy..")
            sc=takecommand()
            webbrowser.open(f'youtube.com/results?search_query={sc}')
            
        elif 'open google' in query:
            webbrowser.open("google.com")
            
        elif 'search google' in query:
            speak("what should i search buddy..")
            sc=takecommand()
            webbrowser.open(f'google.com/search?q={sc}')
            
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            
        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
            
        elif 'open gfg' in query:
            webbrowser.open('geeksforgeeks.org')
            
        elif 'play music' in query:
            music_dir='E:\\music\\favour'
            songs=os.listdir(music_dir)
            r=int(random()*len(songs))
            os.startfile(os.path.join(music_dir,songs[r]))
       
        elif 'the time' in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strtime}, hope your are having it good")
        
        elif 'open code' in query:
            codepath="C:\\Users\\pc\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
            
            
        elif 'mail to me' in query:
            try:
                speak("what should be the content..")
                content = takecommand()
                to='abc@gmail.com'
                sendmail(to,content)
                speak("the mail has been sent,sir")
            except Exception as e:
                speak(" sorry sir, i wasn't able to send the mail")
        
        elif 'thank you' in query:
            speak("the pleasure is mine sir!")
            
        elif 'play a song' in query:
            speak('which song sir')
            sng=takecommand()
            l=''.join(sng.split(' '))
            l=l.lower()
            webbrowser.open(f'gaana.com/song/{l}')
            
        elif 'give direction' in query:
            speak('what is your destination')
            des=takecommand()
            webbrowser.open(f'google.com/maps/place/{des}')
        
        elif 'introduce' in query:
            speak(" i am a virtual assistant created by Ridhi. i can do a lot of things and can make your life easy peasy")
            
        
            
        elif 'create a folder' in query:
            speak('what should be name of folder')
            fn=takecommand()
            parent='c:\\Users\\pc\\OneDrive\\Desktop\\'
            path = os.path.join(parent, fn)
            os.mkdir(path)
            speak('folder created successfully')
            
        elif 'start tetris' in query:
            path='C:\\Users\\pc\\OneDrive\\Desktop\\tetris - starter template\\sd.html'
            os.startfile(path)
        
        
            
        elif 'exit' in query:
            speak("thanks for the time")
            speak("byeee")
            exit()
