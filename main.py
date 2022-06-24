import random
import os
from turtle import clear
import time

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

#def delay_print(s):
#    for c in s:
#        sys.stdout.write(c)
#        sys.stdout.flush()
#        time.sleep(0.15)

def battle(Player, Opponent):

    while Player.health and Opponent.health > 0:

        print(f"Your health: {Player.health} \n Opponent health: {Opponent.health} \n Player Shield: {Player.shield}")
            
        enemy_move = random.randint(1,2)
        round_attack = int(input("Pick your move, \n 1 = Punch \n 2 = Heal \n-> "))

        if Player.shield >= 150:

            if round_attack == 1:
                if enemy_move == 1:
                    print("You chose punch \nOpponent chose punch ")
                    if Player.shield - opponent.damage < 0:
                        
                        a = Player.shield - opponent.damage
                        b = a * -1
                        c = opponent.damage - b
                        Player.health -= c

                    elif Player.shield - opponent.damage > 0: 
                        Player.shield -= opponent.damage

                    else: Player.health -= opponent.damage

                    Opponent.health -= player.damage

                elif enemy_move == 2:
                    print("You chose punch \n Opponent chose punch ")
                    while Player.shield > 0:
                        Player.shield -= opponent.damage
                    else:
                        Player.health -= opponent.damage
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
                    if Player.shield - opponent.damage < 0:
                        
                        a = Player.shield - opponent.damage
                        b = a * -1
                        c = opponent.damage - b
                        Player.health -= c

                    elif Player.shield - opponent.damage > 0: 
                        Player.shield -= opponent.damage

                    else: 
                        Player.health -= opponent.damage

                    


                elif enemy_move == 2: 
                    print("You chose punch \nOpponent chose heal")
                    Opponent.health += opponent.heal
                    Opponent.health -= player.damage

            
            elif round_attack == 2:
                if enemy_move == 1:
                    print("You chose healing \nOppponent chose punch ")
                    while Player.health <= 100:
                        Player.health += player.heal
                    else:
                        Player.shield += player.heal
                    
                    while Player.shield > 0:
                        Player.shield -= opponent.damage
                    else: 
                        Player.health -= opponent.damage
                    Player.health -= opponent.damage
                
                elif enemy_move == 2:
                    print("You chose healing \nOpponent chose healing")
                    while Player.health <= 100:
                        Player.health += player.heal
                    else:
                        Player.shield += player.heal
                    Opponent.health += opponent.heal
            
    else: 
        if Player.health <= 0:
            print("You have been defeated, the game is over")
        
        elif Opponent.health <= 0:
            print("You have won the match, moving on...")
        
        elif Opponent.health and Player.health <= 0:
            print("It's a draw, you have been defeated, the game is over")


    
    
#Beginning of the game 

print("Welcome to 'The Adventure'! \n")


#Choosing Character -- 

character = random.randint(1,3)

if character == 1:
    player = Player("Jack", 0, 100, 10, 10)
    print("You have landed with Jack, he specialises in damage")
    
elif character == 2:
    player = Player("Billy", 0, 100, 10, 15)
    print("You have landed with Billy, he specialises in shields")

elif character == 3:
    player = Player("Wizas", 0, 100, 10, 20)
    print("You have landed with Wizas, he is an all-rounder")


#Choosing Enemy --

opponent = Opponent("Monster", 0, 100, 20, 10)

print("You enter the forest")
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




