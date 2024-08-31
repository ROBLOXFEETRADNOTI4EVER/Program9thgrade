#calculatoeworkfucksake
import math
import time
import keyboard 
from time import sleep
import datetime



def plusminus():
    plusminusinput = int(input("Enter 1 for add 2 subtract: "))
    if plusminusinput == 1:
        print("okay add coming up")
        addnum1 = int(input("first number: "))
        addnum2 = int(input("Secound number: "))
        print(addnum1 + addnum2)
        print("above me is your number")
    elif plusminusinput == 2:
        print("okay Homie subtracting now")
        subnum1 = int(input("first number: "))
        subnum2 = int(input("Secound number: "))
        print(subnum1 - subnum2)
        print("above me is your number")
        


def devineandmultiply():
    devineandmultiplyunput = int(input("Enter 1 for multiply 2 devine: "))
    if devineandmultiplyunput == 1:
        print("okay multiply coming up")
        multiplynum1 = int(input("first number: "))
        multiplynum2 = int(input("Secound number: "))
        print(multiplynum1 * multiplynum2)
        print("above me is your number")
    elif devineandmultiplyunput == 2:
        print("okay Homie devining now")
        devinenumb1 = int(input("first number: "))
        devinenumb2 = int(input("Secound number: "))
        print(devinenumb1 / devinenumb2)
        print("above me is your number")



def rootidkhowitworks():
    rootinput = int(input("Enter the number you want to get the root of: "))
    math.sqrt(rootinput)
    m = math.sqrt(rootinput) 
    print(math.sqrt(rootinput))
    print(f"Above me is the square root of {rootinput} thats {m}")


def powertoskibidi():
    xskibidi = int(input("Enter a number which represents the base "))
    yskibidi = int(input("Enter a number which represents the exponent"))
    print(math.pow(xskibidi, yskibidi))



   
    
        


    
while True:
    userinput = int(input("Press a number 1 +- , 2, /* , 3  √ , 4 x²"))
    if userinput == 1:
        print("You pressed 1")
        plusminus()
    elif userinput == 2:
        print("You pressed 2: ")
        devineandmultiply()
    elif userinput == 3:
        print("You pressed 3: ")
        rootidkhowitworks()
    elif userinput == 4:
        print("You pressed 4: ")
        powertoskibidi()
    else:
        print("you can only press 1,2,3,4 nothing else")
        
    again = input("Do you want to calculate more? (yes/no): ").strip().lower()
    if again != "yes":
        print("Okay, bye!")
        break

