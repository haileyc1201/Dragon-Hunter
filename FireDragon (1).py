import Dragon
import random
import Entity

class FireDragon(Dragon.Dragon):

  def __init__(self, name, max_hp, f_shots):
    '''Initializes the name, max_hp, and fire shots of the dragon'''
    super().__init__(name, max_hp)
    self.f_shots = f_shots

  def special_attack(self, hero):
    '''Dragon uses fire shot to deal 5-9 damage points to the hero'''
    if self.f_shots > 0: #If there are fire shots left
      damage = random.randint(5, 9) #Deal random amount of damage from 5 to 9
      self.f_shots -= 1 #Decrement fire shots remaining
      hero.take_damage(damage) #Deal that damage to the hero
      return "Your hero has been hit! " + self.name + " used a fire shot to deal "+ str(damage) + " damage!"

    else: #If there are no fire shots left
      fail = random.randint(1, 5) #Select a random statement to give the user and user takes no damage 
      if fail == 1:
        return (
            "The fire dragon tripped on his tail and missed his attack! You're safe... for now. No damage was dealt"
        )

      elif fail == 2:
        return (
            "The fire dragon needs a nap. He attempts a fire attack but a yawn interrupts him! You're safe... for now. No damage was dealt"
        )

      elif fail == 3:
        return (
            "The fire dragon was too busy thinking about his next move. He misses his attack! You're safe... for now. No damage was dealt"
        )

      elif fail == 4:
        return (
            "The fire dragon got performance anxiety. He coughs out a spark. You're safe... for now. No damage was dealt"
        )

      else:
        return (
            "The fire dragon rears up to attack AND..... had to pause to cough up a fireball. You're safe... for now. No damage was dealt"
        )

  def __str__(self):
    '''Returns the name, hp, and fire shots of the dragon'''
    return (super().__str__() + "\nFire Shots Remaining: " + str(self.f_shots))
