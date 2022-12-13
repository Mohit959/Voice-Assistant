import random
import replit
from cardsv import printcard


replit.clear()
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10,11,2,3,4,5,6,7,8,9,10,10,10,10,11,2,3,4,5,6,7,8,9,10,10,10,10,11,2,3,4,5,6,7,8,9,10,10,10,10]

logo="""

  ____  _            _       _            _     
 | __ )| | __ _  ___| | __  | | __ _  ___| | __ 
 |  _ \| |/ _` |/ __| |/ _  | |/ _` |/ __| |/ / 
 | |_) | | (_| | (__|   | |_| | (_| | (__|   <  
 |____/|_|\__,_|\___|_|\_\___/ \__,_|\___|_|\_\ 
                                                
"""

#print(logo)


def draw_deck():
    hand = []
    for i in range(2):
        random.shuffle(cards)
        card = cards.pop()
        hand.append(card)
    return hand

def printcards(list):
    for object in list:
        printcard(object)

def check_blackjack(your_cards,computer):
    if (sum(your_cards) == 21 and 11 in your_cards) and (sum(computer)==21 and 11 in computer):
        print("Your Cards")
        printcards(your_cards)
        
        print("Computer")
        printcards(computer)
        print("Draw")
        return True
    elif sum(your_cards) == 21 and 11 in your_cards:
        print("Your Cards")
        printcards(your_cards)
        
        print("Computer")
        printcards(computer)
        print("You Win")
        return True
    elif sum(computer)==21 and 11 in computer:
        print("Your Cards")
        printcards(your_cards)
        
        print("Computer")
        printcards(computer)
        print("You Lose")
        return True
    
    # print("Your Cards")
    # printcards(your_cards)
    # print(f"Computer : [{computer[0]},hidden]" )
   # printcards(computer)
    return False

def draw_card():
    random.shuffle(cards)
    return cards.pop()

def play_again():
    choice = input("Play again y or n:")
    if choice == "y":
        game()


def game():
    replit.clear()
    print(logo)
    your_cards=[]
    computer=[]
    global cards
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10,11,2,3,4,5,6,7,8,9,10,10,10,10,11,2,3,4,5,6,7,8,9,10,10,10,10,11,2,3,4,5,6,7,8,9,10,10,10,10]

    your_cards=draw_deck()
    computer = draw_deck()

    game_decided = False
    if check_blackjack(your_cards,computer):
        game_decided=True

    continue_game= not game_decided
    while continue_game:
        
        print(f"Your Cards: ")
        printcards(your_cards)
        print(f"Computer : [{computer[0]},hidden...] ")
        choice = input("Do you want to draw another card:")

        replit.clear()
        
        if choice == "y":
            your_cards.append(draw_card())
            if sum(computer)<17:
                computer.append(draw_card())        
        else:
            if sum(computer)<17:
                computer.append(draw_card())
            break
        
        if sum(your_cards)>21 and sum(computer)>21:
            if (not 11 in your_cards) and (not 11 in computer):
                #replit.clear()
                print("Your Cards")
                printcards(your_cards)
                print("Computer")
                printcards(computer)
                print("Draw")
                game_decided=True
        if sum(your_cards)>21:
            if 11 in your_cards:
                your_cards[your_cards.index(11)] = 1
                if(sum(your_cards)>21):
                    #replit.clear()
                    print("Your Cards")
                    print(your_cards)
                    print("Computer")
                    print(computer)
                    print("You lose")
                    game_decided=True
            else:
                #replit.clear()
                print("Your Cards")
                printcards(your_cards)
                print("Computer")
                printcards(computer)
                
                print("You lose")
                game_decided=True


        if sum(computer)>21:
            if 11 in computer:
                computer[computer.index(11)] = 1
                if(sum(computer)>21):
                    #replit.clear()
                    print("Your Cards")
                    print(your_cards)
                    print("Computer")
                    printcards(computer)
                    printcards("You Win")
                    game_decided=True
            else:
                #replit.clear()
                print("Your Cards")
                printcards(your_cards)
                print("Computer")
                printcards(computer)
                print("You win")
                game_decided=True
        continue_game=not game_decided
        
    if not game_decided:
    #print("aaya")
        if sum(computer)>21:
            print("Your Cards")
            printcards(your_cards)
            print("Computer")
            printcards(computer)
            print("You Win")
        elif sum(your_cards)>21:
            print("Your Cards")
            printcards(your_cards)
            print("Computer")
            printcards(computer)
            print("You Lose")
        elif sum(your_cards) >= sum(computer):
            print("Your Cards")
            printcards(your_cards)
            print("Computer")
            printcards(computer)
            print("You Win")
        else:
            print("Your Cards")
            printcards(your_cards)
            print("Computer")
            printcards(computer)
            print("You lose")

        game_decided=True
            
    play_again()

game()


       
   
