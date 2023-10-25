import speech_recognition as sr                 # recognize speech
import random                                   # random word in dataset
import pyttsx3                                  # convert speech to text and text to speech
from time import ctime                          # get time details
import webbrowser                               # open browser

import datetime                                 # tell the date
from datetime import date                       

import serial                                   # control arduino
import sys                                      # use for end the system
import keyboard                                 # press to start assistant
import mouse                                    # click to start assistant


# response words dataset

hi_words = ['hi', 'hello', 'yo','heya','hey there!','hi good to see you','whats up? sir']

bye_words = ['bye', 'see ya.', 'see you around mate','i will go now','untill me meet again','adios','see you again mate']

good_words = ['i am fine. thank', 'i am good', 'so chill','nothing bad ready to serve','so fresh!','i am feel powerful','awesome']

connected_words = ['kabin ready to serve','kabin connected']

clear_words = ['all clear sir','reset successful']

doorOpen_words = ['door is now open', 'open se sa mi', 'got it','as you wish sir']

doorClose_words = ['the door is closed', 'nothing can come in now', 'the door is shut','as you wish sir']

windowOpen_words = ['window is now open', 'open se sa mi', 'got it','as you wish sir']

windowClose_words = ['the window is closed', 'no more birds around here', 'the window is shut','as you wish sir']

fanOn_words = ['the fan is turned on', 'spin! spin!', 'wheeee','as you wish sir']

fanOff_words = ['the fan is turned off', 'you spin no more', 'stop stop','as you wish sir']

lightOn_words = ['the light is turned on','as you wish sir']

lightOff_words = ['the light is turned off','light is out','dark mode','as you wish sir']

name_words = ['i am Kabin','yo my name is Kabin']

# set variables
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  



# get string and make a audio file to be played
def speak(audio_string):
    engine.say(audio_string)
    engine.runAndWait()
    
 

# Check connection with UNO board over serial communication
try:
    port = serial.Serial("COM4", 9600)
    print("kabin connected.")
    speak(random.choice(connected_words))
except:
    print("unable to connect to Kabin")
    speak('sorry unable to connect to Kabin ')
    sys.exit()
    

# Check for key word in the command
def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True      
        
                           

def respond(voice_data):
     
    if there_exists(['hey', 'hi', 'hello']):                                                                 # greeting
        speak(random.choice(hi_words))
        
 
       
    if there_exists(["how are you", "how are you doing"]):                                                   # greeting
        speak(random.choice(good_words))
           
        
        
    if there_exists(["who are you", "what is your name"]):                                                   # greeting
        speak(random.choice(name_words))
        
                         
        
        
    if there_exists(['turn the light on', 'turn on the light', 'light on','on the light']):                  # send val O to arduino and control Light ON
        port.write(b'O')
        speak(random.choice(lightOn_words))
        

       
    if there_exists(["turn off the light", "turn the light off","light off",'off the light']):               # send val F to arduino and Light control OFF
        port.write(b'F')
        speak(random.choice(lightOff_words))
        
        
        
    if there_exists(["turn on the fan","turn the fan on"]):                                                  # send val A to arduino and Fan control ON
        port.write(b'A') 
        speak(random.choice(fanOn_words))
        
        
        
    if there_exists(["turn off the fan","turn the fan off"]):                                                # send val a to arduino and Fan control OFF
        port.write(b'a')
        speak(random.choice(fanOff_words))
        
        
        
    if there_exists(["open the door"]):                                                                      # send val B to arduino and Door control OPEN
        port.write(b'B')
        speak(random.choice(doorOpen_words))
        
        
        
    if there_exists(["close the door"]):                                                                     # send val b to arduino and Door control CLOSE
        port.write(b'b')
        speak(random.choice(doorClose_words))
        
        
    if there_exists(["open the window"]):                                                                    # send val C to arduino and Window control OPEN
        port.write(b'C')
        speak(random.choice(doorOpen_words))
        
        
        
    if there_exists(["close the window"]):                                                                   # send val c to arduino and Window control CLOSE
        port.write(b'c')
        speak(random.choice(doorClose_words))    
        
        
        
    if there_exists(["happy face", "smile","enjoy"]):                                                        # send val H to arduino and Matrix LED smile face                                 
        port.write(b'H')
        speak(f"i am smiling")
        
        
        
    if there_exists(["what is the time", "what time now","tell me the time","what time is it"]):             # Tell time
        strTime = datetime.datetime.now().strftime("%H:%M") 
        print(strTime)  
        speak(f"Sir, the time is {strTime}")
        
        
                 
    if there_exists(["what day is today", "what the day now"]):                                              # Tell date
        DateToday = date.today()
        Today = DateToday.strftime('%A')
        print(DateToday)
        print(Today)  
        speak(f"Sir, today is {Today}{DateToday}")   
        
         
    if there_exists(["play song"]):                                                                          # search song on youtube
        search_term = voice_data.split("play")[-1] 
        url = f"https://www.youtube.com/results?search_query={search_term}"
        webbrowser.get().open(url)
        speak(f'Here is what I found for {search_term} on youtube')
        
        
        
    if there_exists(["search for"]) and 'youtube' not in voice_data:                                         # search info on google
        search_term = voice_data.split("for")[-1]
        url = f"https://google.com/search?q={search_term}"
        webbrowser.get().open(url)
        speak(f'Here is what I found for {search_term} on google')  
        
    

    if there_exists(["female"]):                                                                             # change Kabin voice : Female
        engine.setProperty('voice', voices[1].id)       
        speak(f"hi i am kabin ready to serve")
        
        
        
    if there_exists(["male voice"]):                                                                         # change Kabin voice : Male
        engine.setProperty('voice', voices[0].id)       
        speak(f"hi i am kabin ready to serve")
        
        
        
    if there_exists(["reset","clear"]):                                                                       # send val R to arduino and set arduino to begin state
        port.write(b'R')
        speak(random.choice(clear_words))
    
    
    
    if there_exists(["sleep", "exit" , "goodbye"]):                                                           # stop the Kabin   
        speak(random.choice(bye_words))
        sys.exit()

# listen for audio and convert it to text:
def record_audio(ask=False):
    r = sr.Recognizer()
    with sr.Microphone() as source:# microphone as source
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source,duration=1)
            if ask:
                speak(ask)
                
            audio = r.listen(source)# listen for the audio via source
            voice_data = ''
            try:
                voice_data = r.recognize_google(audio)# convert audio to text
            except sr.UnknownValueError:  # error: recognizer does not understand
                speak('I did not get that. say it again please')
            except sr.RequestError: # error: recognizer is not connected
                speak('Microphone is not yet connected')
            print(f"YOU SAID...{voice_data.lower()}")# print what user said  
            return voice_data.lower()

while True:
    if keyboard.is_pressed("space"): # press Space Key to start 
        voice_data = record_audio()  # get the voice input
        respond(voice_data)  # respond
        
    if mouse.is_pressed(button='left'): # press Left mouse button to start
        voice_data = record_audio()  # get the voice input
        respond(voice_data)  # respond
    
     
    
      