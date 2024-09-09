import random
from random import shuffle
import pyfiglet
from colorama import Fore, Style, init
import os
import subprocess
from time import sleep

easy = ['cat', 'dog', 'fish', 'bird', 'hat', 'car', 'star', 'frog', 'wolf', 'cake', 'lion', 'pear', 'leaf', 
        'snow', 'corn', 'rock', 'duck', 'tree', 'kite', 'shoe', 'moon', 'frog', 'hand', 'boat', 'ball', 
        'book', 'sand', 'wind', 'rain', 'rose', 'fire', 'deer', 'milk', 'golf', 'bell', 'sock', 'gold', 
        'bear', 'card', 'bike', 'flag', 'ship', 'mole', 'frog', 'barn', 'palm', 'gift', 'tape', 'pen', 
        'rope', 'lock', 'coat', 'soap', 'clam', 'deer', 'fork', 'salt', 'lamp', 'bowl', 'mask', 'wave', 
        'leaf', 'coin', 'bark', 'hill', 'nail', 'milk', 'star', 'wind', 'note', 'seal', 'ring', 'coin', 
        'nest', 'flag', 'ship', 'bell', 'sock', 'fire', 'mask', 'star']

medium = ['ribbon', 'basket', 'orange', 'pencil', 'giraffe', 'turtle', 'window', 'rabbit', 'flower', 'pepper', 
          'rocket', 'candle', 'butter', 'ladder', 'camera', 'cherry', 'carrot', 'cookie', 'hammer', 'garden', 
          'pillow', 'trophy', 'guitar', 'donkey', 'gloves', 'castle', 'forest', 'pirate', 'scales', 'spider', 
          'jacket', 'wallet', 'bridge', 'helmet', 'bottle', 'spoons', 'garlic', 'shield', 'glider', 'bananas', 
          'bicycle']

hard = ['inflammation', 'translucent', 'exponential', 'proficiency', 'metamorphic', 'hieroglyph', 'unbreakable', 
        'complicated', 'circumcision', 'disposition', 'constellation', 'transformer', 'perpendicular', 
        'unprecedented', 'malnutrition', 'substitution', 'conglomerate', 'philosopher', 'embellishment', 
        'misinterpret'] #Ai generated words no one goona paste and get all of them one by one
score = 0

instructions = [
    "Welcome to the Anagram Game!",
    "Your task is simple:",
    "- You'll be shown a word that has been scrambled (the letters will be mixed up).",
    "- Your job is to guess the original word.",
    "",
    "Select your difficulty:",
    "- Easy: Short and common words.",
    "- Medium: Slightly longer and trickier words.",
    "- Hard: Complex and challenging words.",
    "",
    "Can you unscramble them all? Have fun!"
]
#printing instructions line by line with color cool
for line in instructions:
    print(f"{Fore.GREEN}{line}{Style.RESET_ALL}")
#press any key to continue
input(f"{Fore.YELLOW}Yeah, I read it! Press any key to continue...{Style.RESET_ALL}")


def play_game():
    global score
    os.system('clear')
    print(f"{Fore.GREEN}Game has started...{Style.RESET_ALL}")
    if score == 0:
        print(f"{Fore.LIGHTWHITE_EX}{score}{Style.RESET_ALL} <-- is your current score")
    elif 0 < score < 5:
        print(f"{Fore.YELLOW}{score}{Style.RESET_ALL} <-- is your current score. Keep going!")
    elif 5 <= score < 10:
        print(f"{Fore.GREEN}{score}{Style.RESET_ALL} <-- is your current score. Woah, a smart guy...")
    elif score >= 15:
        print(f"{Fore.GREEN}{score}{Style.RESET_ALL} <-- is your current score. You must be cheating bruh.")    

    choice = input(f"PRESS {Fore.GREEN}/1 easy{Style.RESET_ALL} / PRESS {Fore.YELLOW}/2 medium{Style.RESET_ALL} / PRESS {Fore.RED}/3 hard{Style.RESET_ALL}: ")
    if choice == "1":
        word_list = easy
    elif choice == "2":
        word_list = medium
    elif choice == "3":
        word_list = hard
    else:
        print("You didn't select anything. Please select 1, 2, or 3")
        word_list = None

    if word_list:
        ifk = random.choice(word_list)
        bbc = ifk
        shuffled_word = list(ifk)
        random.shuffle(shuffled_word)
        shuffled_word = ''.join(shuffled_word)
        while shuffled_word == ifk:
            shuffled_word = list(ifk)
            random.shuffle(shuffled_word)
            shuffled_word = ''.join(shuffled_word)
        title = pyfiglet.figlet_format(f'{shuffled_word} ', font='doom')
        print(f'{Fore.YELLOW}{title}{Style.RESET_ALL}')
        checkbbc = input("")
        if checkbbc == bbc:
            print("You got it right")
            score += 1
        else:
            title = pyfiglet.figlet_format(f'{bbc} ', font='doom')
            print(f'{Fore.YELLOW}{title}{Style.RESET_ALL}')
            print("You got it wrong")
            print(bbc + " Was the right word")
#Loop for the game stackoverflow help and ai to understand it 
while True:
    play_game()
    playagain = input("Would you like to play again? Yes/No: ").lower()
    if playagain not in ["yes", "y", "s"]:
        print(f"Your final score is: {score}")
        print("meh you should play my game again sometime!")
        break
    else:
        print(f"GREAT! Your current score is {score}")
