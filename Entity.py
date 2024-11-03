
#Initializing entity class
class Entity:

  #Setting initial values
  def __init__(self, name, max_hp):
    self._name = name #Name of entity
    self._max_hp = max_hp #Max health of entity
    self._hp = max_hp #Current health of entity (initialized at maximum)

  @property
  def name(self):
    '''Returns name of entity'''
    return self._name

  @property
  def hp(self):
    '''Returns current health of entity'''
    return self._hp

  def __str__(self): 
    '''Returns name of entity and current health out of max health'''
    return self._name + ": " + str(self.hp) + "/" + str(self._max_hp) + " hp"

  def take_damage(self, dmg):
    '''Subtracts damage from current health'''
    self._hp = self._hp - dmg
    if self._hp < 0:
      self._hp = 0