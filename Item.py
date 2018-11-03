
import Character

class Item():
    """
    NOTE: small amount of init code from 
    ... https://letstalkdata.com/2014/08/how-to-write-a-text-adventure-in-python-part-1-items-and-enemies/

    General Item class
    """
    def __init__(self, name, description, value):
        """
        Values:
            name: (str) 
            description: (str) 
            value: (int) how much gold the item is worth
        """
        self.name = name
        self.description = description
        self.value = value

class Potion(Item):
    """
    
    """
    def __init__(self, name, description, value, amount):
        super().__init__(name, description, value)
        self.amount = amount

    # def heal(self, other):
    #     Character.healing(10) # work?

class Armor(Item):
    """

    """
    def __init__(self, name, description, value, defense):
        super().__init__(name, description, value)
        self.defense = defense

class Weapon(Item):
    """

    """
    def __init__(self, name, description, value, strength):
        super().__init__(name, description, value)
        self.strength = strength
        
        
        
