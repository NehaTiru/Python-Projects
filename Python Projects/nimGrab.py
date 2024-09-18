#<Neha Tirunagiri>             <10/3/2022>
# <Assignment 3/ Lab/ etc.>
import random 
print("Welcome to NIMGRAB!")
print()

print("By: <Neha Tirunagiri>")
print("[COM S 127 <A>]")
print()
# Constant values
NUM_ITEMS_LOW = 4
NUM_ITEMS_HIGH = 8
NUM_TO_TAKE_LOW = 1
NUM_TO_TAKE_HIGH = 3
gameOver = False
currentTurn = 0 
while gameOver==False:
    choice=input("enter your choice:")
    if choice=="p":
        print("You selected to play!")
        n=random.randint(4,8)
        while n>0:
            if currentTurn==0:               
                print("HUMAN_TURN: ", end="")
                print(f"There are {n} items left in the item pool")
                i=0
                while i<n:
                    print(" | ", end="")
                    i+=1
                print()
                pick=int(input("select the value between [1,3]: "))
                list=(1,2,3)
                while pick not in list:
                    print("Invalid input. Enter a value between [1,3]")
                    pick=int(input("pick a value between [1,3]"))
                print(f"{pick} items taken from the item pool.")
                n=n-pick
                i=0
                while i<n:
                    print(" | ", end="")
                    i+=1
                if n<=0:
                    print("You lost! try again ")
                    break
                print()
                print("*************************************")
                currentTurn+=1
            else:
                print("COMPUTER TURN: ", end="")
                print(f"There are {n} items left in the item pool")
                i=0
                while i<n:
                    print(" |", end="")
                    i+=1
                print()
                pick1=random.randint(1,3)
                if n==3:
                    pick1=random.randint(1,2)
                    n-=pick1
                elif n==2:
                    pick1=1
                    n-=pick1
                elif n==1:
                    print("great, you won the game !")
                    currentTurn-=1
                    break
                else:
                    n-=pick1
                print(f"{pick1} items taken from the item pool")
                i=0
                while i<n:
                    print(" | ", end="")
                    i+=1
                print()
                print("------------------------------------------------")
                currentTurn-=1
    elif choice=="i":
        print('''the instructions of the game are thus:
         Each player, the human and the computer, take turns removing objects from a pool.
Each player can remove between NUM_TO_TAKE_LOW and NUM_TO_TAKE_HIGH items total.
The game progresses until the last item is removed from the pool.The player to take the last item loses the game.''')    
    elif choice=="q":
        gameOver=True
        print("game over")
    else:
        print("incorrect_option")