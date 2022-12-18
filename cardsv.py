import random

cardsset = {
    1:"A",
    11:  "A",
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6:"6",
    7:"7",
    8:"8",
    9:"9",
    10: random.choice(["J","Q","K"])
}

def printcard(n):
    print(f"-------------")
    print(f"| {cardsset[n]}         |")
    print(f"|           |")
    print(f"| BlackJack |")
    print(f"|           |")
    print(f"|           |")
    print(f"-------------")

printcard(10)