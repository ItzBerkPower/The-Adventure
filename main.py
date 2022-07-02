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

    while Player.health and Opponent.health > 0:
        
        print(f"\nYour health: {Player.health} \nOpponent health: {Opponent.health} \nPlayer Shield: {Player.shield} \nOpponent Shield: {Opponent.shield}")
            
        enemy_move = random.randint(1,2)
        round_attack = int(input("\nPick your move, \n 1 = Punch \n 2 = Heal \n-> "))

        if Player.shield >= 150:
            Player.shield = 150

            if round_attack == 1:
                if enemy_move == 1:
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
                    print("You chose punch \nOpponent chose heal")

                    # Opponent chose heal
                    Opponent.health += opponent.heal

                    # You chose punch
                    Opponent.health -= player.damage

            
            elif round_attack == 2:
                if enemy_move == 1:
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
        if Player.health <= 0:
            print("You have been defeated, the game is over")
        
        elif Opponent.health <= 0:
            print("You have won the match, moving on...")

            f = open("database.txt", "a")
            f.write("")
        
        elif Opponent.health and Player.health <= 0:
            print("It's a draw, you have been defeated, the game is over")




    
    





    
#Beginning of the game
os.system('cls')
print("Welcome to 'The Adventure'! \n")
time.sleep(1)

#Choosing Character -- 

character = random.randint(1,3)

if character == 1:
    player = Player("Jack", 0, 100, 10, 10)
    print("You have landed with Jack, he specialises in damage \n")
    
elif character == 2:
    player = Player("Billy", 0, 100, 10, 15)
    print("You have landed with Billy, he specialises in shields \n")

elif character == 3:
    player = Player("Wizas", 0, 100, 10, 20)
    print("You have landed with Wizas, he is an all-rounder \n")


#Choosing Enemy --

opponent = Opponent("Monster", 0, 100, 20, 10)


delay_print("You enter the forest \n")
firstDir = int(input("Do you want to take a left, or right, or go straight down the middle? \n 1 = Left, \n 2 = Right, \n 3 = Middle \n-> "))

if firstDir == 1:
    print("\nYou turn towards the left, and see a monster in the corner of your eye")
    print("\nIt runs towards you")

    battle(player, opponent)


elif firstDir == 2:
    print("\nYou turn towards the right, and are greeted by a monster standing right infront of you")

    battle(player, opponent)

elif firstDir == 2:
    print("\nYou go down the center")
    print("You walk over the bridge and continue on")


















