import math
import random
print(math.sqrt(4))
print(math.fabs(-5))
print(math.floor(4.6))
print(math.pow(2,2))
print(math.trunc(7.999))

#I DON'T UNDERSTAND SIN COS BUT LETS TRY IT

print(math.sin(0))
print(math.sin(4))
print(math.sin(5))
print(math.sin(7))

#sadly not blueberry pie
print(math.pi)

#calculate area of a circle
radius = int(input("ener the radius of the circle:"))
area = math.pi * radius * radius
print("Area of the circle is:", area)

#now we gonna play a  game

generatedNumber = random.randrange(1, 10)
userGuess = int(input("Guess the number 1-10: "))
if userGuess == generatedNumber:
    print("You have guessed it right")
elif userGuess < generatedNumber:
        print("Your guess was to low")
else:
 print ("Your guess was to high")


 