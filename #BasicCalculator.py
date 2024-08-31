    #BasicCalculator
    #importing stuff
import math
import time
import keyboard 
from time import sleep
import datetime
import os 
import subprocess
import webbrowser
        #done importing stuff

now = datetime.datetime.now()
now
#more time stuff




def openspotifyweb():
    spotifyurl = "https://open.spotify.com/"
    firefox_path = "/usr/bin/firefox"
    webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(firefox_path))
    webbrowser.get('firefox').open(spotifyurl)

print("Select a key #E for opening spotify , esc for exiting")
while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
       # print("Select a key") if needed
        if keyboard.is_pressed('e'):
            openspotifyweb()
            break
        elif keyboard.is_pressed('esc'):
            #idk
            print(f"esc just pressed exiting program  {now}")
            sleep(1)
            break
    except Exception as k:
                print(f"idk {k}")
                break