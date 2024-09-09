import random
from random import shuffle
import pyfiglet
from colorama import Fore, Style, init
import os

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
        'misinterpret']  # AI Generated words


def shuffle_word1(list_3_5):
    word = random.choice(list_3_5)
    word = list(word)
    random.shuffle(word)
    return ''.join(word)  # back to a string

cool_print = ["WELCOME TO THIS NEW GAME CALLED ANAGRAM YOUR GOAL IS TO GUESS THE WORDS. HAVE FUN "]

print("Game has started... ,")

choice = input("PRESS /1 easy/ PRESS /2 medium/ PRESS /3 hard/: ")
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
    #Select a random word from the chosen list
    ifk = random.choice(word_list)  #selcets a random word
    #print(f"Selected word: {ifk}")   #displasys the orignal word for test
    bbc = ifk

  


    #shuffles a wrord until its not the same as the original failsafe mechanism

    shuffled_word = list(ifk)  #convers the word to a list of characters
    random.shuffle(shuffled_word)  #shuffle caratcter
    shuffled_word = ''.join(shuffled_word)  #back to a strring

    #if the shuffles word is the same as the original, shuffle again
    while shuffled_word == ifk:
        shuffled_word = list(ifk)
        random.shuffle(shuffled_word)
        shuffled_word = ''.join(shuffled_word)
    

   # print(f"Shuffled word: {shuffled_word}")  #shuffled version of the word
    title = pyfiglet.figlet_format(f'{shuffled_word} ', font='doom')
    print(f'{Fore.YELLOW}{title}{Style.RESET_ALL}')
    checkbbc = input("")

    if checkbbc == bbc:
        print("You got it right")
    else:
        # The correct word will be displayed if the guess is wrong
        title = pyfiglet.figlet_format(f'{bbc} ', font='doom')
        print(f'{Fore.YELLOW}{title}{Style.RESET_ALL}')
        print("You got it wrong")
        print(bbc + " Was the right word")

