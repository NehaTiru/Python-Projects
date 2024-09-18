# <Neha Tirunagiri>   <10/30/2022>
# <assignment4>

import random
import sys

START_ROOM = 1
FINAL_ROOM = 9999

def combat(player_health, monster_health, player_dmg, monster_dmg, currentRoom, gameOver,player_total_health,defeatedwild_dog):
    print("You have engaged in combat")
    print(f"You have encountered a wild monster")
    while monster_health>0 and player_health>0:
            choice= input("COMBAT: (a)ttack, (f)lee: ")
            if choice=="a":
                if defeatedwild_dog==True:
                    print(f"You slash the monster with your sword and deal {player_dmg} damage")
                    monster_health-=player_dmg
                    print(f"monster health = {monster_health}")
                    print()
                else:
                    wild_cat= random.randint(0,1)
                    if wild_cat== 0:
                        print(f"You tried to stab the monster but it dodged your attack")
                        print(f"monster health = {monster_health}")
                        print()
                    else:
                        print(f"You slash the monster with your sword and deal {player_dmg} damage")
                        monster_health-=player_dmg
                        print(f"monster health = {monster_health}")
                        print()
            elif choice=="f":
                currentRoom=1
                print(f"You succesfully fled to room{currentRoom} (Hint:try togo to another room,it may help you win )")
                break           
            if monster_health<=0:
                print(f"yeah,You have finially defeated the monster!")
                print()
            else:
                wild_cat= random.randint(0,1)
                if wild_cat==0:
                    print(f"The monster tried to bite you but you dodged the attack")
                    print()
                else:
                    print(f"The monster bit you for {monster_dmg} damage")
                    player_health-=monster_dmg
                    print(f"player current health = {player_health}/{player_total_health}")
                    print()
                    if player_health<=0:
                        print(f"You were slayed by the wild monster and perished in the dungeon of doom. (Hint: try togo to another room,it may help you win)")
                        gameOver = True
                        
    print("--------------------------------------------------------------------------------------------------------------------------------------------------")
    return player_health, monster_health, player_dmg, monster_dmg, currentRoom,gameOver, defeatedwild_dog, player_total_health
def shop(goldAmount, player_health, player_dmg, player_total_health):
    choice="z"
    while choice!="c":
        print(f'''The dungeon store   (Current gold = {goldAmount})

 a) 1x potion of healing (heals you to max health) = 30 gold
 b) 1x potion of rage (increase player damage by 1) = 15gold
 c) exit shop
                ''')
        choice= input("enter (a), (b) or (c) : ")   
        if choice=="a":
            if goldAmount<40:
                print("not enough gold")
            else:
                player_health= player_total_health
                goldAmount-=40
                print(f"Transaction succesful!")
                print()
        elif choice=="b":
            if goldAmount<20:
                print("not enough gold")
            else:
                player_dmg+=1
                goldAmount-=20
                print(f"Transaction succesful!")
                print()
    print("--------------------------------------------------------------------------------------------------------------------------------------------------")
    return goldAmount, player_health, player_dmg, player_total_health
def room1(goldAmount, visited_room, currentRoom):

    if visited_room == False:
        
        gold = 20
    
        print()
        print("You enter to an field, barely lit room and spot something shining in the darkness. You step closer to your footsteps and find Gold!")
        print("The room has", gold, "gold pieces in it.")
        goldAmount += gold
        print("After taking the gold, you currently have", goldAmount, "gold pieces in your bag...")
        print()
        visited_room = True
    else:
        print()
        print("You have already visited this room before.")
        print()
    print("where do you want to go?")
    direction = input("[N] [E] [S] [W]?: ")
    while direction != "N" and direction != "E" and direction != "W" and direction != "S":
        print("Invalid input.")
        direction = input("[N] [E] [S] [W]?: ")
    if direction=="N":
        currentRoom=4
    if direction=="W":
        currentRoom=2
    if direction=="E":
        currentRoom=3
    if direction == "S":
        currentRoom = 6
    print("--------------------------------------------------------------------------------------------------------------------------------------------------")
    return goldAmount, visited_room, currentRoom
def room2(currentRoom, goldAmount, visited_room, player_health, player_dmg, gameOver, defeatedwild_dog, player_total_health):
    gold = 30
    monster_health=3
    monster_dmg=1
    if visited_room == False:
        player_health, monster_health, player_dmg, monster_dmg, currentRoom, gameOver, defeatedwild_dog, player_total_health= combat(player_health, monster_health, player_dmg, monster_dmg, currentRoom,gameOver, defeatedwild_dog, player_total_health)
        if gameOver== True:
            return currentRoom, goldAmount, visited_room, player_health, player_dmg, gameOver, defeatedwild_dog, player_total_health
        if currentRoom !=2:
            return currentRoom, goldAmount, visited_room, player_health, player_dmg, gameOver, defeatedwild_dog, player_total_health
        else:
            print()
            print("The room has", gold, "gold pieces in it.")
            goldAmount += gold
            print("After taking the gold, you currently have", goldAmount, "gold pieces in your bag.")
            print()
        visited_room= True
    else:
        print()
        print("You have already visited this room before.")
        print()
    entershop=input("Enter shop? (y),(n)")
    if entershop=="y":
        goldAmount, player_health, player_dmg, player_total_health= shop(goldAmount, player_health, player_dmg, player_total_health)
    print("where do you want to go?")
    direction = input("[E]*: ")
    while direction != "E":
        print("Invalid input.")
        direction = input("[E]*: ")
    if direction=="E":
        currentRoom=1
    print("--------------------------------------------------------------------------------------------------------------------------------------------------")
    return currentRoom, goldAmount, visited_room, player_health, player_dmg, gameOver, defeatedwild_dog, player_total_health
def room3(currentRoom, goldAmount, visited_room, player_health, player_dmg, gameOver, defeatedwild_dog, player_total_health):
    gold=25
    monster_health=3
    monster_dmg=2
    if visited_room == False:
        player_health, monster_health, player_dmg, monster_dmg, currentRoom,gameOver, defeatedwild_dog, player_total_health= combat(player_health, monster_health, player_dmg, monster_dmg, currentRoom,gameOver, defeatedwild_dog, player_total_health)
        if gameOver== True:
            currentRoom=1
            return currentRoom, goldAmount, visited_room, player_health, player_dmg, gameOver, defeatedwild_dog, player_total_health
        if currentRoom !=3:
            return currentRoom, goldAmount, visited_room, player_health, player_dmg, gameOver, defeatedwild_dog, player_total_health
        else:
            print("You have defeated monster and gained some strength. Your accuracy is now 100%!")
            defeatedwild_dog=True
            print("The room has", gold, "gold pieces in it.")
            goldAmount += gold
            print("After taking the gold, you currently have", goldAmount, "gold pieces in your bag.")
            print()
        visited_room= True
    else:
        print()
        print("You have already visited this room before.")
        print() 

    print("where do you want to go?")
    direction = input("[W]?: ")
    while direction != "W":
        print("Invalid input.")
        direction = input("[W]?: ")
 
    if direction=="W":
        currentRoom=1
    print("--------------------------------------------------------------------------------------------------------------------------------------------------")
    return currentRoom, goldAmount, visited_room, player_health, player_dmg, gameOver, defeatedwild_dog, player_total_health

def room4(currentRoom, goldAmount, visited_room, player_health, player_dmg, gameOver, defeatedwild_dog, player_total_health):
    gold = 5 
    monster_health=3
    monster_dmg=1
    if visited_room == False:
        print("You can feel that the exit is nearby. You feel a strange feeling that something is coming from the north")
        player_health, monster_health, player_dmg, monster_dmg, currentRoom, gameOver, defeatedwild_dog, player_total_health= combat(player_health, monster_health, player_dmg, monster_dmg, currentRoom,gameOver, defeatedwild_dog, player_total_health)
        if gameOver== True:
            return currentRoom, goldAmount, visited_room, player_health, player_dmg, gameOver, defeatedwild_dog, player_total_health
        if currentRoom !=4:
            return currentRoom, goldAmount, visited_room, player_health, player_dmg, gameOver, defeatedwild_dog, player_total_health
        else:
            print()
            print("The room has", gold, "gold pieces in it.")
            goldAmount += gold
            print("After taking the gold, you currently have", goldAmount, "gold pieces in your bag.")
            print()
        visited_room= True
    else:
        print()
        print("You have already visited this room before.")
        print()
    entershop=input("Enter shop? (y),(n)")
    if entershop=="y":
        goldAmount, player_health, player_dmg, player_total_health= shop(goldAmount, player_health, player_dmg, player_total_health)
    print("where do you want to go?")
    direction = input("[N],[S]?: ")
    while direction != "N" and direction != "S":
        print("Invalid input.")
        direction = input("[N],[S]?: ")
 
    if direction=="N":
        currentRoom=5
    else:
        currentRoom=1
    print("--------------------------------------------------------------------------------------------------------------------------------------------------")
    return currentRoom, goldAmount, visited_room, player_health, player_dmg, gameOver, defeatedwild_dog, player_total_health
# Room 5 - Final Room
def room5(currentRoom, goldAmount, visited_room, player_health, player_dmg, gameOver, defeatedwild_dog, player_total_health):
    gold=1000
    monster_health=10
    monster_dmg=2
    if visited_room == False:
        print("You feel a strong sense of someone coming . The room smells terrible, you can see the dungeon exit ahead of you but there is a huge crocodile.")
        player_health, monster_health, player_dmg, monster_dmg, currentRoom, gameOver, defeatedwild_dog, player_total_health= combat(player_health, monster_health, player_dmg, monster_dmg, currentRoom, gameOver, defeatedwild_dog, player_total_health)
        if gameOver== True:
            return currentRoom, goldAmount, visited_room, player_health, player_dmg, gameOver, defeatedwild_dog, player_total_health
        if currentRoom !=5:
            return currentRoom, goldAmount, visited_room, player_health, player_dmg, gameOver, defeatedwild_dog, player_total_health
        else:
            print("sorry,You have defeated the dungeon game and are free to leave")
            print("The crocodile is in front of the door has 0 gold pieces near it.instead, it has a huge red diamond worth 1000 gold!")
            goldAmount += gold
            print()
        visited_room= True
        print(visited_room)
    else:
        print()
        print("You have already visited this room before.")
        print()
    print("where do you want to go? ((N)orth to exit dungeon, (S)outh to keep exploring)")
    direction = input("[N],[S]?: ")

    while direction != "N" and direction != "S":
        print("Invalid input.")
        direction = input("[N],[S]?: ")
 
    if direction=="N":
        print("You have exited the dungeon")
        currentRoom=FINAL_ROOM
    else:
        currentRoom=4
    return currentRoom, goldAmount, visited_room, player_health, player_dmg, gameOver, defeatedwild_dog, player_total_health

# Room 6 function - NOt the final room ( Final Room is room5 function)
def room6(currentRoom, goldAmount, visited_room, player_health, player_dmg, gameOver, defeatedwild_dog, player_total_health):
    gold = 50
    monster_health=4
    monster_dmg=1
    if visited_room == False:
        print("the room is ahead of you and your approaching the room next to south!")
        player_health, monster_health, player_dmg, monster_dmg, currentRoom, gameOver, defeatedwild_dog, player_total_health= combat(player_health, monster_health, player_dmg, monster_dmg, currentRoom,gameOver, defeatedwild_dog, player_total_health)
        if gameOver== True:
            return currentRoom, goldAmount, visited_room, player_health, player_dmg, gameOver, defeatedwild_dog, player_total_health
        if currentRoom !=6:
            return currentRoom, goldAmount, visited_room, player_health, player_dmg, gameOver, defeatedwild_dog, player_total_health
        else:
            print()
            print("The room has", gold, "gold pieces in it.")
            goldAmount += gold
            print("After taking the gold, you currently have", goldAmount, "gold pieces in your bag.")
            print()
        visited_room= True
    else:
        print()
        print("You have already visited this room before.")
        print()
    entershop=input("Enter shop? (y),(n)")
    if entershop=="y":
        goldAmount, player_health, player_dmg, player_total_health= shop(goldAmount, player_health, player_dmg, player_total_health)
    print("where do you want to go?")
    print("Hint : Select N to visit the final room! ")
    print("You are time travelling !")
    direction = input("[N],[S]?: ")
    while direction != "N" and direction != "S":
        print("Invalid input.")
        direction = input("[N],[S]?: ")
 
    if direction=="N":
        currentRoom=5
    else:
        currentRoom=3
    print("--------------------------------------------------------------------------------------------------------------------------------------------------")
    return currentRoom, goldAmount, visited_room, player_health, player_dmg, gameOver, defeatedwild_dog, player_total_health

def main():
    gameOver = False

    START_GOLD = 0 
    goldAmount = START_GOLD
    currentRoom = START_ROOM
    visited_room1 = False
    visited_room2 = False
    visited_room3 = False
    visited_room4 = False
    visited_room5 = False
    visited_room6 = False
    defeatedwild_dog = False
    player_total_health = 10
    player_health = 10
    player_dmg = 1
    

    print("Welcome to Dungeon Crawl.")
    print()
    print("By:Neha Tirunagiri")
    print("[COM S 127 A]")
    print()

    while True:
        choice = input("MAIN MENU: [p]lay, [i]nstructions,[q]uit?: ")
        print()
        if choice == "p":
            print("The hunt for riches has led you to the dungeon of doom. What will be your fate in the rooms beyond?")
            while gameOver==False:
                if currentRoom == 1:
                    goldAmount, visited_room1, currentRoom = room1(goldAmount, visited_room1, currentRoom)
                elif currentRoom == 2:
                        currentRoom, goldAmount, visited_room2, player_health, player_dmg, gameOver, defeatedwild_dog, player_total_health = room2(currentRoom, goldAmount, visited_room2, player_health, player_dmg, gameOver, defeatedwild_dog, player_total_health)
                elif currentRoom == 3:
                    currentRoom, goldAmount, visited_room3, player_health, player_dmg, gameOver, defeatedwild_dog, player_total_health= room3(currentRoom, goldAmount, visited_room3,  player_health, player_dmg, gameOver, defeatedwild_dog, player_total_health)
                elif currentRoom == 4:
                    currentRoom, goldAmount, visited_room4, player_health, player_dmg, gameOver, defeatedwild_dog, player_total_health = room4(currentRoom, goldAmount, visited_room4,  player_health, player_dmg, gameOver, defeatedwild_dog, player_total_health)
                elif currentRoom == 5:
                    currentRoom, goldAmount, visited_room5, player_health, player_dmg, gameOver, defeatedwild_dog, player_total_health = room5(currentRoom, goldAmount, visited_room5,  player_health, player_dmg, gameOver, defeatedwild_dog, player_total_health)
                elif currentRoom == 6:
                    currentRoom, goldAmount, visited_room5, player_health, player_dmg, gameOver, defeatedwild_dog, player_total_health = room6(currentRoom, goldAmount, visited_room5,  player_health, player_dmg, gameOver, defeatedwild_dog, player_total_health)


                elif currentRoom == FINAL_ROOM:
                    print()
                    print("You have escaped with", goldAmount, "gold from the dungeon!")
                    print()
                    gameOver=True
                    exit()
                else:
                    print("Error - currentRoom number", currentRoom, "does not correspond with available rooms")
                    sys.exit()
                
           

            goldAmount = START_GOLD
            currentRoom = START_ROOM
            visited_room1 = False
            visited_room2 = False
            visited_room3 = False
            visited_room4 = False
            visited_room5 = False
            visited_room6 = False
            defeatedwild_dog = False
            player_total_health = 10
            player_health = 10
            player_dmg = 1
            gameOver=False
        elif choice == "i":
            print("travers the dangerous dungeon and collect all the gold ")
            
            pass
        elif choice == "q":
            game_over=True
            print("see you later") 
        else:
            print()
            print("Please enter [p], [i], or [q]...")
            print()
if __name__ == "__main__":
    main()
       