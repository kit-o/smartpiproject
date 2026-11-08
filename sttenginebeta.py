# pip install SpeechRecognition pyaudio
import speech_recognition as sr
import time
from os import system as s
from libfile import *
r = sr.Recognizer()
print('running init')
init()
while True:
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
 
        text = r.recognize_google(audio)
#        try:
        exec(f"{text.lower()}()")
#        except:
#            print("I do not understand!")
    except sr.UnknownValueError:
        print("Please repeat that")
