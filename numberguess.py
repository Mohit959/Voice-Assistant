import random

logo="""

 _   _                 _                 _____                     _               _____                      
| \ | |               | |               |  __ \                   (_)             |  __ \                     
|  \| |_   _ _ __ ___ | |__   ___ _ __  | |  \/_   _  ___  ___ ___ _ _ __   __ _  | |  \/ __ _ _ __ ___   ___ 
| . ` | | | | '_ ` _ \| '_ \ / _ \ '__| | | __| | | |/ _ \/ __/ __| | '_ \ / _` | | | __ / _` | '_ ` _ \ / _ |
| |\  | |_| | | | | | | |_) |  __/ |    | |_\ \ |_| |  __/\__ \__ \ | | | | (_| | | |_\ \ (_| | | | | | |  __/
\_| \_/\__,_|_| |_| |_|_.__/ \___|_|     \____/\__,_|\___||___/___/_|_| |_|\__, |  \____/\__,_|_| |_| |_|\___|
                                                                            __/ |                             
                                                                           |___/                              
"""
#print(logo)
def playagain():
    play_again = input("Do You Want To Play Again:").lower()
    if(play_again=="yes"):
        game()


def game():
    # os.clear()
    print(logo)
    answer = random.randint(1,100)
    #print(answer)
    print("----------Welcome to number Guessing Game----------")
    print()
    level = input("Select a level 'easy' or 'hard' : " )
    lives=0
    if(level=="easy"):
        lives=7
    else:
        lives=5
    
    while(lives>0):
        print()
        print(f"You have {lives} lives")
        guess =int(input("Guess the number: "))
        if(answer == guess):
            print(f"\n**** You Won! you have {lives} lives remaining****\n ")
            break
        elif answer>guess:
            print("Too Low")
        else:
            print("Too High")
        lives=lives-1
        if(lives==0):
            print(f"\nToo bad! You Lost! Answer was {answer}\n")
        
    playagain()