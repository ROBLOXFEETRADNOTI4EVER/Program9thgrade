import os
from time import sleep

from colorama import Style, Fore, init
import string
import time

def list1():
    grociories = ["apple","bread","cheese","fullfatyoghurt","electroliets","ground-beef"]

    grociories.reverse()
    print(grociories)
    grociories.append("bbc")
    print(grociories)
    grociories.reverse()
    print(grociories)
    grociories.append("bbc")
    print(grociories)
    grociories.count("bbc")
    print(grociories.count("bbc"))
    grociories.insert(0, "bone")
    print(grociories)
    grociories.remove("bone")
    print(grociories)


    even = []
    for x in range(1,40):
        if x % 2 ==0:  #all even number starting from 2 all the way to 11
            even.append(x)
            sleep(0.1)
            print(even)

    even.append("a")
    print(even)



def idk1():
    even = []
    even1 = []
    for x in ("Hello"):
        if x in string.ascii_letters:  #all even number starting from 2 all the way to 11
            even.append(x)
            time.sleep(0.09)
            print("".join(even))
    for x in ("World"):
        if x in string.ascii_letters:
            even1.append(x)
            time.sleep(0.09)
            print("".join(even1))

    print("".join(even)+ " " + "".join(even1))

    #print(even)
def idk2():
    str = "Hello list"
    characterList = [x for x in str]
    print(characterList)

    tuple1 = ()

    tuple2 = (1,2,6,3,9)

    tuple3 = ("Jhon",23,56.0,True)

    kfcpoepleibeatup = (1984,1995,1998,13)
    print(kfcpoepleibeatup)


    predators = ("sqc","ishowcock","dream","Crismrbeast","Drnodisrespect")
    print(predators)

    print(predators[0])
    print(predators[2]) #cuts out the 2nd one Remmeber python starts with 0
    print(predators[1:4])

#tuple11 = (1,2,3)
#tuple11 [3] = 5
#print(tuple11)

#del predators
#print(predators) #can't beacuse nothing inside preadators

    tuple1 = (1,2,3)
    tuplle2 = (4,5,6)
    print(tuple1+tuplle2)
    print(tuple1 * 3)


    nitrousers = ("samuel","Jhosn","Alexander")
    print("bbc" in nitrousers)
    print("Alexander" in nitrousers)


    atuple = (2,3,4,5,5,6.3433543,True)
    print(len(atuple))
    print(min(atuple))
    print(max(atuple))

    a = (23,34,45,56,67,89)
    print(a.count(89)) #counts how many of them in the touple
    print(a.index(67)) #checks them on the touple by number like lists 


def dictonary():
    #dict1 = {}
    #dict2 = {1:"Jhon", 2:"Sam"}
    #print(dict2)
    #testdic = {
        #"John": "Discord",
        #"Peter": "Signal",
        #"Sam": ["Matrix,Discord"] #use [] if multiple data stored 
    #}
    #print(testdic)

    #eaxmple = {1:"Bob",2:"Pop",3:"Carl"}
    #print(eaxmple[1])
    #print(eaxmple.get(2)) #if error returns none example 1 is betther []
    #print(eaxmple[3]) #we use [ if keyerror is resed it says not foind in the dictornary instead of error not found]
    
    ex = {1:"Marko",2:"Peka"}
    ex[1] = "Den"
    ex[3] = "Sim"
    print(ex)

    frozenfood = {1:"Pizza",2:"Wifi",3:"connection",4:"GPS"}
    del(frozenfood[1]) #deletes 1st key and its dictonary
    print(frozenfood)
    frozenfood[1] = "Peperoni" #adds peperoni to the list sadly to the back
    print(frozenfood) 
    print(frozenfood.keys()) #prtins keys 2,3,4,1
    print(frozenfood.values()) #only prints wifi conection gps peperoni  this funcitons only returns dicotonary  values
    print(frozenfood.clear())
    frozenfood[1] = "kolbasza"
    frozenfood[2] = "kolbaszabig1"
    frozenfood[3] = "kolbaszabig2"
    frozenfood[4] = "kolbaszabig3"
    frozenfood[5] = "kolbaszabig4"
    frozenfood[6] = "kolbaszabig5"
    print(frozenfood)
    print(frozenfood.get(4))
    print(frozenfood.update(frozenfood))
    print(frozenfood.items()) #makes it a tuple


    emptpyData = {101:"Bravo",102:"Gustavo",102.5:"Eren",103:"Maistero"}
    print(emptpyData.keys())
    print(emptpyData.values())
    print(emptpyData.items())
    emptpyData.update({104:"Jamir",105:"George"})
    print(emptpyData)

    VariablleDictonary = {"Asia": ["Usa","hungary","slovakia","UAE","Bosnia"],101:"Dalmatia"}
    print(VariablleDictonary["Asia"])

    VariablleDictonary = {"Asia": ["Usa","hungary","slovakia","UAE","Bosnia"],101:"Dalmatia"}
    VariablleDictonary["Asia"].append("Japan") #adds japan with append 
    print(VariablleDictonary)
    VariablleDictonary["Asia"].remove("hungary")
    print(VariablleDictonary) #removed hungary
    VariablleDictonary.update({101:"Dalmatia , Bosnia"})
    print(VariablleDictonary)

    dat = {101:"1",102:"2"}
    for i in dat:
        print(i)  #it returns 101,102 the keys not the dicotonaries


    for i in dat.values(): #Since value added it prints the isniede of the key it revails it 
        print(i) #prints 1,2

    dat1 = {1:"szabo",2:"Balazs",3:"bbc team var most rad",4:"i should sleep"}
    for i in dat1.items(): #now what it does it prints own key with its dic/value inside of it (1, 'example')
        print(i)