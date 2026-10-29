import pyttsx3 as tts
import requests
import threading
import time
from os import system as s
from bs4 import BeautifulSoup
from math import *
import sys
s('clear')
stopdrop = []
engine = tts.init()

def weather():
    raw = requests.get("https://api.weather.gov/stations/klaf/observations/latest")
    if raw.status_code == 200:
        data = raw.json()
        temp = data["properties"]["temperature"]["value"]
        scribe = data["properties"]["textDescription"]

        ftemp = (temp*9/5)+32
        # s('espeak -a 1000 '+f"'{ftemp}'")
    else:
        # s('espeak -a 1000 '+"'Error: Weather Data Unaviable'")
        print("Error Fetching Data...")
        s('espeak -a 1000 '+"Something went wrong...")
    # 
    print("--"*40)
    print(f"{ftemp}°F")
    s('espeak -a 1000 "Here is the weather right now."')
    s('espeak -a 1000 '+f"'{ftemp} degrees fair-in-height'")
    
    print(f"{temp}°C")
    s('espeak -a 1000 '+f"'{temp} degrees Celcius'")
    
    print(f"The weather is desrcibed as: {scribe}.")
    s('espeak -a 1000 '+f"'The weather is described as: {scribe}.'")
    
def google():
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/114.0.0.0 Safari/537.36"
        )
    }
    s('espeak -a 1000 '+"'Please type your search term.'")
    
    requests.get("https://lite.duckduckgo.com/")
    html = requests.post("https://lite.duckduckgo.com/lite",data={"q":input("Search Term: ")},headers=headers)



    sup = BeautifulSoup(html.text,"html.parser")
    elements = sup.find_all("a",class_="result-link")
    elements2 = sup.find_all("td",class_="result-snippet")

    with open("file.txt","w") as file:
        file.write(html.text)
    # print(elements)
    # print(html.text)

    first_result = elements[0]
    print("First Result: ")
    s('espeak -a 1000 '+"'First Result'")
    
    print(elements[0].text)
    s('espeak -a 1000 "'+elements[0].text+'"')
    
    print(elements2[1].text)
    s('espeak -a 1000 "'+elements2[1].text+'"')
    
    s('espeak -a 1000 '+"'Would you like more results?'")
    
    
    moreoptions = input("Would you like more results? ")
    if moreoptions.lower() == "yes" or moreoptions == "y":
        for e in elements:

            print(e.text)
            s('espeak -a 1000 "'+e.text+'"')
            
            print(elements2[elements.index(e)].text)
            s('espeak -a 1000 "'+elements2[elements.index(e)].text+'"')
      
    elif moreoptions.lower() == "no" or moreoptions == "n":
        print("Okay! Returning to main screen.")
        s('espeak -a 1000 '+"'Okay! Returning to main screen.'")
        

    else:
        s('espeak -a 1000 '+"'Not a valid option, returning to main screen.'")
        print("Not a valid option. Returning to main screen.")
        


fin=[]
def search():
    google()
def timersys(tim):
    close = False
    
    try:
        tim2 = int(tim)
        close = True
    except:
        s('espeak -a 1000 '+"'Invalid Input'")
        
        print("Invalid Input")
    if close:
        time.sleep(tim2)
        fin.append(tim2)
        print("TIME IS UP (Continue Writing below...)")
        while True:
            if tim2 in stopdrop: 
                stopdrop.remove(tim2)
                break

            s('espeak -a 1000 '+"'TIME IS UP. TIME IS UP. TIME IS UP. TIME IS UP.'")
        
def alarmsys(tom):
    closse = True
    try:
        tom2 = int(tom)
        closse = True
    except:
        s('espeak -a 1000 '+"'Invalid Input'")
        
        print("Invalid Input")
    if closse:
        s('espeak -a 1000 '+"'Offline'")
        

def cls():
    s("clear")

def timer():
    s('espeak -a 1000 '+"'Please type timer time in seconds.'")
    
    t = threading.Thread(target=lambda:timersys(input("Timer Legnth (s): ")), daemon=True)
    t.start()
def alarm():
    s('espeak -a 1000 '+"'Please put in desired alarm time.'")
    
    f = threading.Thread(target=lambda:timersys(input("Alarm Time hh-mm-ss.mmm: ")), daemon=True)
    f.start()
def end():
    s('espeak -a 1000 '+"'Goodbye'")
    
    s('espeak -a 1000 '+"'Disabled press control Z to end'")
    
def calc():
    s('espeak -a 1000 '+'"Insert Math problem (mathematical python symbols only. Math library supported.)"')
    
    try:
        d=input('Math problem (mathematical python symbols only. Math library supported.): ')
        new = eval(d)
        s('espeak -a 1000 '+f"'The result is {new}'")
        
        print(new)
    except:
        print("Invalid expression")
        s('espeak -a 1000 '+"'Invalid expression'")
        
def math():
    calc()
def solve():
    calc()
def dismiss():
    for s in fin:
        stopdrop.append(s)
        fin.remove(s)
#def main():
#    while True:
#        try:
#            commandline = input(">>> ")
#            exec(f"{commandline.lower()}()")
#        except:
#            s('espeak -a 1000 '+"'Unknown command.'")
            
#            print("Unrecongized command.")
#def debmain():
   # while True:
  #      commandline = input('>>> ')
 #       exec(f"{commandline.lower()}()")
#
#mainloop = threading.Thread(target=main,daemon=False)
#mainloop.start()
