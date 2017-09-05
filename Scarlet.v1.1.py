import pyttsx
from PIL import ImageGrab
import webbrowser
import random,os
import speech_recognition as sr
from time import sleep
from selenium import webdriver
import wikipedia
from time import strftime
import time,sys
import datetime
import subprocess
import pyautogui
import requests
from Tkinter import *
import psutil


engine=pyttsx.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
r=sr.Recognizer()
info=['I am Scarlet, a simple but efficient virtual assistant made by a 16 year old programmer in the summer of 2017','I am your father Luke','I am Scarlet,I said that a ton of times already','I am the one who needs no gun to get respect from no one on the street']
booting=['Scarlet Assistant version 1.0 has begun','Scarlet Assistant at your service','Currently starting Scarlet Virtual Assistant',"Loading drivers and modules","Scarlet assistant is booting up"]
greetings=["hello","hello there","Hi,I am Scarlet","What is up user","Scarlet at your service","Greetings organic lifeform","how can I help you today","Greetings human","Your wish is my command","Hello user","Hello user,what would you like to do"] #Possible responses to user greetings
userGreet=["how can I be of assistance today","your wish is my command","I am Scarlet,your personal virtual assistant","how are you today"]
closing=['Shutting down','Closing Scarlet Assistant','Have a nice day']
feelings=["I have no feelings,I am not sentient like you probably are","I am feeling like a million bytes","I am feeling functional and ready to serve"]
musical=["What are we watching today","Are gonna to sing some karaoke","Listening to some music today","Good thing I have my dancing module in","My favorite youtuber is Shane Dawson","Let's start our own channel"]
engine.say(random.choice(booting))
engine.runAndWait()
engine.say("Please write your name in the window")
engine.runAndWait()
name=raw_input("Your name:")
engine.say("Hello "+name+ random.choice(userGreet))
engine.runAndWait()
def greeting(data):
        engine.say(random.choice(greetings))
        engine.runAndWait()
        main()

def makeJoke():
    responeData = requests.get("http://api.icndb.com/jokes/random/?escape=javascript")
    joke = str(responeData.json()['value']['joke'])
    print joke
    engine.say(joke)
    engine.runAndWait()
    main()
    
def search(data):
    driver=webdriver.Chrome()
    driver.get("http://google.com/search?q="+data.split("search",1)[1])
    wordSearch=data.split("search",1)[1]
    sentence=wikipedia.summary(wordSearch, sentences=4)
    engine.say(sentence)
    engine.runAndWait()
    main()
   
    
    

def youtube(data):
    engine.say(random.choice(musical))
    engine.runAndWait()
    Call_URL="http://youtube.com"
    mycmd = r'start chrome /new-tab {}'.format(Call_URL)
    subprocess.Popen(mycmd,shell = True)
    #webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("http://youtube.com")

    sleep(2)
    main()
def time(data):
    current=strftime("%I:%M")
    engine.say("The current time is "+current)
    engine.runAndWait()
    main()

def tDate(date):
    dateT=strftime("%B:%d:%A:%Y")
    engine.say("Today's date is "+dateT)
    engine.runAndWait()
    main()
def Gmail(data):
        engine.say("Opening Email Client")
        engine.runAndWait
        Call_URL="http://gmail.com"
        mycmd = r'start chrome /new-tab {}'.format(Call_URL)
        subprocess.Popen(mycmd,shell = True)
        #webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("http://gmail.com")
        main()
def Amazon(data):
        engine.say("Opening Amazon to purchase "+data.split('buy',1)[1])
        engine.runAndWait
        webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("https://www.amazon.com/s/field-keywords=",data.split('buy',1)[1])
        main()
def SS():
        engine.say("Taking screenshot")
        engine.runAndWait()
        name=random.randint(1000,300000)
        time.sleep(5)
        ImageGrab.grab().save("screenshot"+str(name),"JPEG")
        engine.say("Screenshot saved at "+name)
        engine.runAndWait()
        print("Screenshot saved at"+name)
        main()
        
def calculate(data):
        if 'plus' in data:
                str.replace("plus","+")
        
        value1,value2= (data.split('calculate',1)[1])
        answer=value1+value2
        engine.say("The answer to that is "+answer)
        engine.runAndWait()
def locate (data):
        place=data.split('locate',1)[1]
        engine.say("Locating "+ place)
        engine.runAndWait()
        Call_URL=place
        mycmd = r'start chrome /new-tab {}'.format(Call_URL)
        subprocess.Popen(mycmd,shell = True)
        #webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("https://www.google.ca/maps/place/"+place+"/")
        main()
def goto(data):
        where=data.split('go to',1)[1]
        Call_URL=where
        engine.say("Navigating to"+where)
        engine.runAndWait()
        mycmd = r'start chrome /new-tab {}'.format(Call_URL)
        subprocess.Popen(mycmd,shell = True)
        #webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("http://"+where.strip())

        main()        
        
                         


def main():        
    with sr.Microphone() as source:
        sleep(1)
        print("Say something then wait.")
        audio=r.listen(source)
        sleep(1)
        print "\n"*50
   
    
    try:
       data = r.recognize_google(audio)
       print("You said:"+data)
       if data=='hello':
            greeting(data)
       if 'search'in data:
           engine.say("Opening web browser to search for "+data.split("search",1)[1])
           engine.runAndWait()
           search(data)
       if 'YouTube' in data:
           youtube(data)
       if 'time' in data:
           time(data)
       if 'date' in data:
            tDate(data)
       if data=='shut down':
           engine.say(random.choice(closing))
           engine.runAndWait()
           sys.exit()
       if 'thank you' in data:
           engine.say("You are welcome")
           engine.runAndWait()
       if data=='Scarlet':
               engine.say("Yes, I am here")
       if data=='email':
               Gmail(data)
       if 'buy' in data:
               Amazon(data)
       if data=='screenshot':
                SS()
       if 'calculate' in data:
               calculate(data)
       if 'locate' in data:
               locate(data)
       if data=='Notepad':
               engine.say("Opening notepad")
               engine.runAndWait()
               subprocess.Popen('notepad.exe')
               
               main()
       if data=='change voice' :
               engine.setProperty('voice',voices[random.randrange(0,2)].id)
               engine.say("Voice now changed,if not use command again")
               engine.runAndWait()
               main()
       if data=='tell me a joke':
               makeJoke()
       if 'go to' in data:
               goto(data)
       if 'type' in data:
               text=data.split('type',1)[1]

               pyautogui.typewrite(text)
               main()
       if data=='who am I':
               engine.say("You are "+ name)
               engine.runAndWait()
               main()
       if data=='who are you':
               engine.say(random.choice(info))
               engine.runAndWait()
               main()
       if data=='how are you':
               engine.say(random.choice(feelings))
               engine.runAndWait()
               main()

               

       else:
            main()
                       
               
               
    except sr.UnknownValueError:
            sleep (2)
            engine.say("Google Speech Recognition could not understand what you were trying to say")
            engine.runAndWait()
            main()
    except sr.RequestError as e:
           print("Could not request results from Google Speech Recoginition Service;{0}".format(e))
           main()
main()  
