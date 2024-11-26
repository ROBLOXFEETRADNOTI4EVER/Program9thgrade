import  random
import os 

lyrics = [
    "Kisses in the alley, where the sun don't shine|her shadow fades just like mine",
    "She wore regret like a second skin|but never let the sorrow in",
    "A Polaroid smile fades with time|just like your hand slipping out of mine",
    "I heard your laugh in an old tape hiss|like a memory I can't dismiss",
    "You left your name in the condensation|a fleeting ghost of conversation",
    "Echoes of goodbye haunt the payphone line|but I’m still waiting for a sign",
    "The party ended, but you're still dancing|lost in a song that's always chancing",
    "Love letters torn, scattered in the breeze|like secrets whispered to the trees"
]


guessshits = []

endings = [lyric.split("|")[0].strip() for lyric in lyrics]
#prints the end of the string  the 0 indicating that its the 0 

endings1 = [lyric.split("|")[0].strip() for lyric in lyrics]

"""so i should first select a random then slice it and compare the value of the first part to the last part 
and if the user input is same as the secound thing sliced and use trim method 
for spaces to remove and lower case aswell to avoid furter issues"""


def spliceit():
    selectors = random.choice(lyrics)
    # print("".join(selectors))
    guessshits.append(selectors)
    firstpart = [guessshit.split("|")[0].strip() for guessshit in guessshits]
    secoundpart = [guessshit.split("|")[1].strip() for guessshit in guessshits]
    # print("".join(firstpart))
    os.system('cls' if os.name == 'nt' else 'clear')
    #now that i got this i sliced the sting and added it to a list i will do that i will empty the list later on to nothing
    #ask user for a imput and compare it to the secound part
spliceit()
def askuser():
    firstpart = [guessshit.split("|")[0].strip() for guessshit in guessshits]
    secoundpart = [guessshit.split("|")[1].strip() for guessshit in guessshits]
    userinput = input(f" first part is \n<>{"".join(firstpart)}\nenter what you think the end is \n>")
    if userinput == secoundpart[0].lower(): # use [0] method to conpare a string to a string and not  a string to a list if i don't add [0] it will become string
        print("You got a match")
    else: print("not a mach") , print(userinput) , print(secoundpart)

askuser()

#issues to fix it doesn't compare even if its a good value 
#solutions ? maybe make the secound part into a list and check if from there since it will work betther 

