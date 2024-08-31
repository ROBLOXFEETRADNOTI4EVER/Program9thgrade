for i in range(5):
 print(i)

 for i in range(5):
    print("FEMCORD")

    for i in "FEMCORD":
        print(i)



uname = input("Enter Your username: ")

while uname == "":
    print("Error type something ")
    uname = input("Enter Your username: ")





print(f"welcome {uname}")
#now here is a age systeam
while True:
        try:
            age = int(input("Enter your age: "))

            if age < 0 or age > 100:
                print(f"{age} <-- can't be  negative or over 100")
            else:
                break #exit's the loop if input is vaild
        except ValueError:
            print("Error: Please enter a valid number.")
                

print(f"Thanks, Mr/MS {age}-year old. ")



