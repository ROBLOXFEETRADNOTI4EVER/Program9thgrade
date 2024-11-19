import  random


f = open("szotar.txt", "r")
print(f.read())

mylist = []
mylist.append(f)

class console:
    @staticmethod
    def log(thing):
        print(thing)

console.log(mylist)
userin = input("Entersomethinghere\n>")

print(userin)

chars = []

chars.append(userin)

slicedchars = []

for i in userin:    
    i = [userin]
    i  + 1

print(len(userin))