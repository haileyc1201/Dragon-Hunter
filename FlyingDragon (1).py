import Dragon
import random

#Initializing FlyingDragon class
class FlyingDragon(Dragon.Dragon):

  def __init__(self, name, max_hp, swoops):
    '''Initializes the name, max_hp, and swoops of the dragon'''
    super().__init__(name, max_hp)
    self.swoops = swoops

  
  def special_attack(self, hero):
    '''Dragon uses swoop to deal 5-8 damage points to the hero'''
    if self.swoops > 0: #If there are swoops left
      damage = random.randint(5, 8) #Deal random amount of damage from 5 to 8
      self.swoops -= 1 #Decrement swoops remaining
      hero.take_damage(damage) #Deal that damage to the hero
      return "Your hero has been hit! " + self.name + " used a swoop to knock you down and deal " + str(damage) + " damage!"

    else: #If there are no swoops left
      fail = random.randint(1, 5) #Pick a random response and user takes no damage
      if fail == 1:
        return (
            "The flying dragon tripped on his tail and missed his attack! You're safe... for now. No damage was dealt"
        )

      elif fail == 2:
        return (
            "The flying dragon needs a nap. He attempts a swoop attack but the altitude made him more sleepy! You're safe... for now. No damage was dealt"
        )

      elif fail == 3:
        return (
            "The flying dragon was too busy thinking about his next move. He misses his attack! You're safe... for now. No damage was dealt"
        )

      elif fail == 4:
        return (
            "The flying dragon got performance anxiety. He gives his wings a small flap and gets embarrassed. You're safe... for now. No damage was dealt"
        )

      else:
        return (
            "The flying dragon rears up to attack AND..... realizes he forgot to call his mom. He says he'll make it quick. You're safe... for now. No damage was dealt"
        )

  
  def __str__(self):
    '''Returns the name, hp, and swoops of the dragon'''
    return (super().__str__() + "\nSwoop attacks Remaining: " + str(self.swoops))
