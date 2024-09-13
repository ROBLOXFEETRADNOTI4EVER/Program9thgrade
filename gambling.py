import time
import random
import os
import sys
#gambling game 

user_money = 100 
spins = 0 
free_spin = 1


def animation():
    animation = "|/-\\"
    start_time = time.time()
    while True:
        for i in range(4):
            time.sleep(0.2)  # Feel free to experiment with the speed here
            sys.stdout.write("\r" + animation[i % len(animation)])
            sys.stdout.flush()
        if time.time() - start_time > 3:  # The animation will last for 10 seconds
            break
    sys.stdout.write("\rDone!")


print(user_money)

money_list = [10, 20, 40]
money_remove = [20, 40, 80]



def chances():
    listofminus = [-10,-20,-30,-40,-50,-60,-70,-80,-90,-100]
    user_money = 40
    bbc = user_money
    spins = 0 
    free_spin = 1
#in this game you will have a 50%50 (70 for the game 30% for you) chance to win more user_money 
    print("Would you like to play?")    
while True:
    
        listofminus = [-10,-20,-30,-40,-50,-60,-70,-80,-90,-100]
        if user_money < 0:

            print("breaking the loop since you are in minus credit ")
            break
        else:
            playornot = input("Would you like to gamble all your credits? n/Yes/nNo")
            if playornot in("no","No","nNo","nno"):
                break
            else:
                animation()    
                jkjkj = random.randint(0, 1)
                print(jkjkj)
                if jkjkj == 0:
                    animation()
                    print("You lost money womp womp")
                    moneyrandom = random.choice(money_remove)
                    user_money = user_money - moneyrandom
                    print(" user credits --> ", user_money,"$")
                elif jkjkj == 1:
                    animation()
                    moneyrandom = random.choice(money_list) 
                    print(f"you got more money {moneyrandom}" )
                    user_money  = user_money + moneyrandom
                    print("$", " user credits --> ", user_money)
                


print("You got a free spin")

chances()

#moneyrandom = random.choice(money_list)  
#print(moneyrandom)

#lottory    