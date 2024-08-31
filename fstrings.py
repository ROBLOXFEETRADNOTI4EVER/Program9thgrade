import string
import os
from time import sleep
import spotipy
name= input("Enter your bill bitch: ")
print(f"Hello  Your bill is: {name}! ")


num1 = 5
num2 = 4

print(f" five plus four is {num1 + num2}")

appName = "FEMCORDdd"
print(appName[0])
print(appName[2])
print(appName[:4])
print(appName[2:5])
print(appName[3:])
print(appName[::2])


firstname = "Jhon"
lastname = "DEHAR"
fullname = firstname + " " + lastname 

print(fullname)

firstusername = "GERMAN"
lastusername = "Propaganda"

print(" ".join([firstusername, lastusername]))


str = "Python"
print(str*2)

print("now deleting everything from screen ")
sleep(5)

##This clears the previus things on your screen
os.system('clear')


str = "Python"
print(str.islower())
print(str.upper())
print(str.lower())
print(str.replace('P','A'))
