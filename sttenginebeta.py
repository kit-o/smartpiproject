# pip install SpeechRecognition pyaudio
import speech_recognition as sr
import time
import threading
r = sr.Recognizer()
timeisupforspeech = False
with sr.Microphone() as source:
    audio = r.listen(source)
def scream():
    pass
 #   print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"*20)
def countd():
    time.sleep(30)
    timeisupforspeech = True
try:
 
    text = r.recognize_google(audio)
    if text == "smart pi":
        timer = threading.Thread(target=countd,dameon=True)
        timer.start()
        while not timeisupforspeech:
            command = r.recognize_google(audio)
            try:
                exec(f"{command}()")
            except:
                print("I don't understand.")
        timeisupforspeech = False
       
except sr.UnknownValueError:
    print("Please repeat that")
