import os
from colorama import Style ,Fore ,init
def draw_board(spots):
    board = (f"|{spots[1]}|{spots[2]}|{spots[3]}|\n"
    f"|{spots[4]}|{spots[5]}|{spots[6]}|\n"
    f"|{spots[7]}|{spots[8]}|{spots[9]}|")
    print(board)

spots = {1:'1',2:'2',3:'3',4:'4',5:'5',
         6:'6',7:'7',8:'8',9:'9'}




def CheckForWin(spots):
    #Horizontal Cases
    if     (spots[1] == spots[2] == spots[3]) \
        or (spots[4] == spots[5] == spots[6]) \
        or (spots[7] == spots[8] == spots[9]):
        return True
        #Vertical Cases
    elif   (spots[1] == spots[4] == spots[7]) \
        or (spots[2] == spots[5] == spots[8]) \
        or (spots[3] == spots[6] == spots[9]):
        return True
    #diognal Cases
    elif   (spots[1] == spots[5] == spots[9]) \
        or (spots[3] == spots[5] == spots[7]):
        return True    
    else:
        return False


playing = True
complete = False
turn = 0
prev_turn = -1
entering = True
xPlaying = True

while entering:
    os.system('cls' if os.name == 'nt' else 'clear')
    player1 = input("Player1: Enter a name\n >")
    if len(player1) > 16:
        
        print("PlayerName Must be under 16 caracters\n")
        
    if player1 in [" ",""]:
        print("Username can't contain spaces or can't be left out empty\n")
        
    else:

        player2 = input("Player2 Enter a name \n >")
        if len(player2) > 16:
        
            print("PlayerName Must be under 16 caracters\n")
            break
        if player2 in [" ",""]:
            print("Username can't contain spaces or can't be left out empty\n")   
        else:
            entering = False
                
#Making sure names are nammes


def checkTurn(turn):
    if turn % 2 == 0: 
        xPlaying = False
        print(f"Player {player1}'s turn: Pick your spot or press q to quit\n")
        return f'{Fore.BLUE}O{Style.RESET_ALL}'
        
    else: 
        xPlaying = True
        print(f"Player {player2}'s turn: Pick your spot or press q to quit\n")
        return f'{Fore.RED}X{Style.RESET_ALL}'
        




if entering == True:
    print("You doN't have an username set exiting")
    exit()



while playing:
    os.system('cls' if os.name == 'nt' else 'clear')
    draw_board(spots)
    if prev_turn == turn:
        print(f"Invalid spot: {choice} selected please select another one.")
    prev_turn = turn
    checkTurn(turn)
        
    choice = input()
    if choice == 'q':
        playing = False
        
    elif str.isdigit(choice) and int(choice) in spots:
        if not spots[int(choice)] in {f"{Fore.RED}X{Style.RESET_ALL}", f"{Fore.BLUE}O{Style.RESET_ALL}"}:
            turn += 1
            spots[int(choice)] = checkTurn(turn)
    if CheckForWin(spots): playing, complete = False, True
    if turn > 8: playing = False

os.system('cls' if os.name == 'nt' else 'clear')
draw_board(spots)
if complete:
    if checkTurn(turn) == 'X': print(f"Player {player1} Wins!")
    else: print(f"Player:{player2} Wins!\n")
else:
    print("No Winners\n")

print("Thanks for playing")