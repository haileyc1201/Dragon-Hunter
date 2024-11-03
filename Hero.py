
import Entity
import random

#Initializing Hero class, inherit from Entity 
class Hero(Entity.Entity):

  def sword_attack(self, dragon):
    '''Dragon takes random 2d6 damage from sword attack. 
    Returns sword attack description.'''
    #Randomize damage of 2d6 by rolling 1d6 twice.
    damage = random.randint(1,6) + random.randint(1,6)
    #Dragon takes damage
    dragon.take_damage(damage)
    #Description 
    return "You slash the " + dragon.name + " with your sword for " + str(damage) + " damage!"

  def arrow_attack(self, dragon):
    '''Dragon takes random 1d12 damage from arrow attack.
    Returns arrow attack description.'''
    #Randomize 1d12 damage 
    damage = random.randint(1,12)
    #Dragon takes damage 
    dragon.take_damage(damage)
    #Description
    return "You shoot an arrow at the " + dragon.name + " with your bow for " + str(damage) + " damage!"

