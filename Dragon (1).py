
import Entity
import random

#Initializing Dragon class, inherit from Entity 
class Dragon(Entity.Entity):

  def basic_attack(self, hero):
    '''Hero takes random attack damage 3-7 from tail attack.
    Returns a description of tail attack.
    '''
    #Deal random 3-7 damage to hero
    damage = random.randint(3,7)
    hero.take_damage(damage)
    #Description
    return self.name + " smashes you with its tail for " + str(damage) + " damage!"
    
  def special_attack(self, hero):
    '''Hero takes random attack damage 4-8 from claw attack.
    Returns a description of claw attack.
    '''
    #Deal random 4-8 damage to hero
    damage = random.randint(4,8)
    hero.take_damage(damage)
    #Description 
    return self.name + " sharply claws you for " + str(damage) + " damage!"

 