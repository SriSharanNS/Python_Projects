import random

ladder={1:38,4:14,8:30,21:42,28:74,50:67,71:92,88:99}
snake={32:10,36:6,48:26,62:18,88:24,95:56,97:78}
pos1=0
pos2=0

def Move(pos):
    dice=random.randint(1,6)
    print(f"Dice:{dice}")
    pos+=dice
    if pos in snake:
        print("Bitten By Snake")
        pos=snake[pos]
        print(f"Position:{pos}")
    elif pos in ladder:
        print("Climbed Ladder ")
        pos+=ladder[pos]
        print(f"Position:{pos}")
    else:
        print(f"Position:{pos}")
    print("\n")
    return pos

while True:
    A=input("Player 1 Enter \"A\" to throw dice:")
    pos1=Move(pos1)
    if pos1>=100:
        print("Game Over !!! \n Player 1 Wins. ")
        break
    B=input("Player 2 Enter \"B\" to throw dice:")
    pos2=Move(pos2)
    if pos2>=100:
        print("Game Over !!! \n Player 2  Wins. ")
        break 

    
         

          

