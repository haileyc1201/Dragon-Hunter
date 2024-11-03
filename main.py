# Hailey Clark and Lexi Nguyen Group 8
# Date: 3/5/2024
# Description: This program is a game where the user plays as a hero and must defeat 3 dragons
import Entity
import check_input
import Hero
import Dragon
import FireDragon
import FlyingDragon
import random

def main():

  # Getting user input for name
  user_name = input("What is your name challenger?\n")

  #Initialliing hero
  player = Hero.Hero(user_name, 50)
  print("Welcome to dragon training, " + player.name + ". You must defeat 3 dragons.")

  #Initializing dragons in a list. Radomizes HP and special attack uses to scale difficulty. 
  first_dragon = Dragon.Dragon("The Armed Dragon", random.randint(15,30))
  second_dragon = FireDragon.FireDragon("The Red Archfiend", random.randint(10,25), random.randint(2, 3)) 
  third_dragon = FlyingDragon.FlyingDragon("The Blue Eyes White Dragon", random.randint(10,25), random.randint(2, 4))
  dragons = [first_dragon, second_dragon, third_dragon]
  #Initialzing random_dragon for losing game over statement. 
  random_dragon = dragons[1]

  #While loop to keep game running until all dragons are defeated or hero hp reaches 0
  while player.hp != 0:
    print()

    #Prints player name and hp
    print(player)

    #Prints dragon names, hp, and special attacks remaining
    for i in range(1,len(dragons)+1):
      print(str(i), ". ", dragons[i-1])

    #Getting user input for which dragon to attack
    dragon_choice = check_input.get_int_range("\nChoose a dragon to attack: ", 1, len(dragons))

    #Getting user input for which attack to use
    attack_choice = check_input.get_int_range("\nAttack with: \n1. Arrow (1D12) \n2. Sword (2D6)\nEnter Weapon: ", 1, 2)
    print()

    #If statement to determine attack is used
    if attack_choice == 1:
      print(player.arrow_attack(dragons[dragon_choice-1]))
    else:
      print(player.sword_attack(dragons[dragon_choice-1]))

    #For each dragon
    for dragon in dragons:
      #If dragon is dead, announce death and remove from list
      if dragon.hp == 0:
        print("You slain " + dragon.name + "!")
        dragons.remove(dragon)

    #If there are dragons left, a random dragon attacks the player
    if len(dragons) != 0:    
      random_dragon = dragons[random.randint(0, len(dragons)-1)]
      #Choosing a random attack 
      random_dragon_attack = random.randint(1,2)
      if random_dragon_attack == 1:
        print(random_dragon.basic_attack(player))
      else:
        print(random_dragon.special_attack(player))

    #If there are no dragons alive, break from the while loop
    else:
      break

  
  print()

  #If the player survived, print victory statement
  if player.hp != 0:
    print("You have felled all the beasts. Congrats! You have passed the trial.")

  #If the player died, print game over statement which includes the dragon that slain the player. 
  else:
    print("You have been slain by " + random_dragon.name + "! Womp Womp.")
  
main()