# Imports
import random
import os
from turtle import clear
import time
import sys 
import json

class Player:
    def __init__(self, name, shield, health, damage, heal):
        self.name = name
        self.shield = shield
        self.health = health
        self.damage = damage
        self.heal = heal

class Opponent: 
    def __init__(self, name, shield, health, damage, heal):
        self.name = name
        self.shield = shield
        self.health = health
        self.damage = damage
        self.heal = heal

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.15)

def battle(Player, Opponent):

    os.system('cls')

    while Player.health and Opponent.health > 0:
        
        time.sleep(0.5)
        print(f"\nYour health: {Player.health} \nOpponent health: {Opponent.health} \nPlayer Shield: {Player.shield} \nOpponent Shield: {Opponent.shield}")
            
        enemy_move = random.randint(1,2)
        round_attack = int(input("\nPick your move, \n 1 = Punch \n 2 = Heal \n-> "))

        if Player.shield >= 150:
            Player.shield = 150

            if round_attack == 1:
                if enemy_move == 1:

                    time.sleep(0.5)
                    print("You chose punch \nOpponent chose punch ")

                    # Opponent chose punch
                    if Player.shield - opponent.damage < 0:
                        
                        a = Player.shield - opponent.damage
                        b = a * -1

                        Player.shield = 0
                        Player.health -= b

                    elif Player.shield - opponent.damage > 0: 
                        Player.shield -= opponent.damage

                    else:
                        Player.health -= opponent.damage

                    #You chose punch
                    Opponent.health -= player.damage

                elif enemy_move == 2:

                    time.sleep(0.5)
                    print("You chose punch \n Opponent chose heal ")

                    # Opponent chose healing
                    Opponent.health += opponent.heal

                    # You chose punch
                    Opponent.health -= player.damage


            elif round_attack == 2:
                while round_attack == 2:
                    print("You can't pick this move, please pick another one")
                    inner_round_attack = int(input("Pick your move, \n 1 = Punch \n 2 = Heal \n-> "))

                    if inner_round_attack == 1:
                        break

 
        else:
            if round_attack == 1:
                if enemy_move == 1:

                    time.sleep(0.5)
                    print("You chose punch \nOpponent chose punch ")
                    
                    # Opponent chose punch
                    if Player.shield - opponent.damage < 0:
                        
                        a = Player.shield - opponent.damage
                        b = a * -1

                        Player.shield = 0
                        Player.health -= b
    
                    elif Player.shield - opponent.damage > 0: 
                        Player.shield -= opponent.damage

                    else:
                        Player.health -= opponent.damage

                    # You chose punch
                    Opponent.health -= player.damage

                elif enemy_move == 2: 

                    time.sleep(0.5)
                    print("You chose punch \nOpponent chose heal")

                    # Opponent chose heal
                    Opponent.health += opponent.heal

                    # You chose punch
                    Opponent.health -= player.damage

            
            elif round_attack == 2:
                if enemy_move == 1:

                    time.sleep(0.5)
                    print("You chose healing \nOppponent chose punch ")

                    # Player chose healing
                    if Player.health + player.heal > 100:

                        a = Player.health + player.heal
                        b = a - 100
                        Player.health == 100
                        Player.shield += b
                    
                    elif Player.health + player.heal < 100:
                        Player.health += player.heal

                    else:
                        Player.shield += Player.heal

                    # Opponent chose punch
                    if Player.shield - opponent.damage < 0:
                        
                        a = Player.shield - opponent.damage
                        b = a * -1

                        Player.shield = 0
                        Player.health -= b

                    elif Player.shield - opponent.damage > 0: 
                        Player.shield -= opponent.damage

                    else:
                        Player.health -= opponent.damage

                
                elif enemy_move == 2:
                    
                    time.sleep(0.5)
                    print("You chose healing \nOpponent chose healing")
                    if Player.health + player.heal > 100:

                        a = Player.health + player.heal
                        b = a - 100
                        Player.health == 100
                        Player.shield += b

                    elif Player.health + player.heal < 100:
                        Player.health += player.heal

                    else:
                        Player.shield += Player.heal
                    
                    Opponent.health += opponent.heal
            
    else: 

        # Player defeated

        if Player.health <= 0:
            print("You have been defeated, the game is over")

            Player.health = 0

            with open("database.json", "r") as f:
                data = json.load(f)
            
            data[profile][1] = Player.health

            with open("database.json", "w") as f:
                json.dump(data, f, indent=4)

        
        # Opponent defeated

        elif Opponent.health <= 0:
            print("You have won the match, moving on...")

            
            with open("database.json", "r") as f:
                data = json.load(f)
            
            data[profile][1] = Player.health

            with open("database.json", "w") as f:
                json.dump(data, f, indent=4)
            


        # Both defeated (Draw)

        elif Opponent.health and Player.health <= 0:

            print("It's a draw, you have been defeated, the game is over")

            Player.health = 0

            with open("database.json", "r") as f:
                data = json.load(f)
            
            data[profile][1] = Player.health

            with open("database.json", "w") as f:
                json.dump(data, f, indent=4)



    

# ---- Beginning of the game ----
os.system('cls')
print("Welcome to 'The Adventure'! \n")
time.sleep(1)

# Opening an account, reaching an existing account
has_account = input("\nDo you have an account? \n -> ")

while has_account.upper() not in ("YES", "NO", "Y", "N"):

    print("Unidentified Answer, Options Are:\n yes or y\n no or n \n")

    has_account = input("\nDo you have an account? \n -> ")



if has_account.upper() in ("YES", "NO", "Y", "N"):

    if has_account.upper() == "NO" or has_account.upper == "N":

        print("\nLets open you an account.")
        time.sleep(0.75)

        user_name = input("\nWhat is your name? \n -> ")

        with open("database.json", "r") as f:
            data = json.load(f)

        for i in data:
            while i[0] == user_name:
                print("You already have an account with that name")

            if i[0] != user_name:
                break
            
        data.append([user_name, 0, 0, 0, 0, 0, 0])

        for i, e in list(enumerate(data)): 
            if data[i][0] == user_name:
                profile = int(i)
                break

        with open("database.json", "w") as f:
            json.dump(data, f, indent=4)
        
        time.sleep(1)


    elif has_account.upper() == "YES" or has_account.upper() == "Y":

        with open("database.json", "r") as f:
                data = json.load(f)

        user_name = input("\nWhat is your name? \n -> ")

        while not any(user_name == stuff[0] for stuff in data):
            print("\nAccount not found, please try again \n ")

            user_name = input("\nWhat is your name? \n -> ")

        if any(user_name == stuff[0] for stuff in data):
            
            use_account = input("\nFound your account, would you like to use it? \n -> ")

        

            while use_account.upper() not in ("YES", "Y", "NO", "N"):
                print("\nUnidentified answer, Options are: \nyes, y \nno, n")

                use_account = input("\nFound your account, would you like to use it? \n -> ")


            
            if use_account.upper() in ("YES", "Y", "NO", "N"):
            
                if use_account.upper() == "YES" or use_account.upper() == "Y":
                    print("\nPerfect")
                        
                    for i, e in list(enumerate(data)):
                        if data[i][0] == user_name:
                            profile = int(i)
                            break

                    time.sleep(2)


                elif use_account.upper() == "NO" or use_account.upper() == "N":
                    print("Lets make you a new account then.\n")

                    user_name = input("\nWhat is your name? \n -> ")

                    with open("database.json", "r") as f:
                        data = json.load(f)

                    for i in data:
                        while i[0] == user_name:
                            print("You already have an account with that name")
                            user_name = input("\nWhat is your name? \n -> ")

                        else:
                            break
                            
                    data.append([user_name, 0, 0, 0, 0, 0, 0])

                    for i, e in list(enumerate(data)):
                        if data[i][0] == user_name:
                            profile = int(i)
                            break
                                            
                    with open("database.json", "w") as f:
                        json.dump(data, f, indent=4)




os.system('cls')

with open("database.json", "r") as f:
        data = json.load(f)

if data[profile][3] == 0:

    print("Since you opened a new account, lets make your player \n")
    time.sleep(1)

    name = random.randint(1,3)

    if name == 1:
        print("Your player name is Wizas")
        #player = Player("Wizas", 100, 20, 10)

        data[profile][1] = 100
        data[profile][4] = 20
        data[profile][5] = 10
        data[profile].append("Wizas")

        data[profile][3] += 1

        time.sleep(5)

        with open("database.json", "w") as f:
            json.dump(data, f, indent=4)

    elif name == 2:
        #player = Player("Jack", 100, 20, 10)
        print("Your player name is Jack")

        data[profile][1] = 100
        data[profile][4] = 20
        data[profile][5] = 10
        data[profile].append("Jack")
    
        data[profile][3] += 1

        time.sleep(5)

        with open("database.json", "w") as f:
            json.dump(data, f, indent=4)

    elif name == 3:
        #player = Player("Billy", 100, 20, 10)
        print("Your player name is Billy")

        data[profile][1] = 100
        data[profile][4] = 20
        data[profile][5] = 10
        data[profile].append("Billy")

        data[profile][3] += 1

        time.sleep(5)

        with open("database.json", "w") as f:
            json.dump(data, f, indent=4)


#---------------------------------------------------------------------------------------------------------------------------------------------------------


#Choosing Enemy --

opponent = Opponent("Monster", 0, 100, 20, 10)

os.system('cls')

delay_print("Starting game...")
time.sleep(3)

os.system('cls')

delay_print("You enter the forest \n")
time.sleep(1)

firstDir = int(input("\nDo you want to take a left, or right, or go straight down the middle? \n 1 = Left, \n 2 = Right, \n 3 = Middle \n-> "))

if firstDir == 1:
    time.sleep(2)
    print("\nYou turn towards the left, and see a monster in the corner of your eye\n")

    time.sleep(1)
    delay_print("\nIt runs towards you... \n \n")

    time.sleep(2)

    with open("database.json", "r") as f:
        data = json.load(f)

    if data[profile][7] == "Wizas":
        player = Player("Wizas", data[profile][6], data[profile][1], data[profile][4], data[profile][5])

    elif data[profile][7] == "Jack":
        player = Player("Jack", data[profile][6], data[profile][1], data[profile][4], data[profile][5])
    
    elif data[profile][7] == "Billy":
        player = Player("Billy", data[profile][6], data[profile][1], data[profile][4], data[profile][5])

    battle(player, opponent)

    if data[profile][1] > 0:

        print("\nYou've earned 50 coins \nYou've earned 5 xp!")
    
        with open("database.json", "r") as f:
            data = json.load(f)

        data[profile][2] += 50
        data[profile][3] += 5

        with open("database.json", "w") as f:
            json.dump(data, f, indent=4)


elif firstDir == 2:
    print("\nYou turn towards the right, and are greeted by a monster standing right infront of you, but you dodge it")

    battle(player, opponent)

elif firstDir == 3:
    print("\nYou go down the center")
    print("You walk over the bridge and continue on")
    

# data[profile][0] = Username
# data[profile][1] = health
# data[profile][2] = coins
# data[profile][3] = exp
# data[profile][4] = damage
# data[profile][5] = heal
# data[profile][6] = shield
# data[profile][7] = Player username






