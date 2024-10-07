import random
import string

def generate_password(lenght):
    characters = string.ascii_letters + string.digits + string.punctuation


    password = "".join(random.choice(characters)for i in range(lenght))
    
    return password
    
try:

    lenght = int(input("Enter the lenght for your password \n>"))
    if lenght >= 6:
        password = generate_password(lenght)
        print("Your new password is",password)
    else:
        print("For better security, try a password longer than 6 characters.")
except Exception as e:
    print("Please enter only numbers (and numbers above4)",e)