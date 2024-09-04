import random
import os
import time

time
security_words = ["bird", "flew", "out", "from", "the", "window", "at", "night", "and", "cried",0 , 1, 2, 3, 4, 5, 6, 7, 8, 9,]
random.shuffle(security_words)
security_words = list(map(str, security_words))

print("".join(security_words))

print(*security_words)



secdownload = input("would you like to download your security words as a txt file?: y/n")

if secdownload.lower() in ["Yes", "y"]:
    #need to add that it connects to a server in case my other python program opened and then it will connect to it and transfer files to it with username+security_words+ip
    print("saving it")
    security_words = [str(word) for word in security_words]
    file_name = "security_words.txt"
    #get the full file pat
    file_path = os.path.join(os.getcwd(), file_name)
    #write the list to a txt file
    with open(file_path, "w") as file:
        file.write(" ".join(security_words))
        print(f"file saved to {file_path}")
else:
    print("exiting")