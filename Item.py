
import Character

class Item():
    """
    NOTE: small amount of init code from 
    ... https://letstalkdata.com/2014/08/how-to-write-a-text-adventure-in-python-part-1-items-and-enemies/

    General Item class
    """
    def __init__(self, name, description):
        """
        Values:
            name: (str) 
            description: (str)
        """
        self.name = name
        self.description = description

    def use(self):
        pass

class Potion(Item):
    """
    
    """
    def __init__(self, name, description):
        super().__init__(name, description)

    def use(self):
        pass

class Healing_Potion(Potion):
    """
    
    """
    def __init__(self, name, description, tier):
        super().__init__(name, description)
        tiers = {"Minor" : 0.5, "Normal" : 1, "Major": 2}

        self.tier = tiers[tier]

    def use(self, character):
        """
        Heals selected character. Potion power based on tier.
        Args:
            character: Player object
        Effects:
            character object is healed by certain amount.
        """
        value = int(character.level * self.tier * 5)
        character.healing(value)
        return

class Armor(Item):
    """

    """
    def __init__(self, name, description):
        super().__init__(name, description)
        tiers = {"Leather" : 0.5, "Normal" : 1, "Major": 2}
        types = ["helmet", "torso", "leggings", "boots"]
        self.defense = 1

    def use(self):
        self.equip()
        return
    
    def equip(self):
        return

class Weapon(Item):
    """

    """
    def __init__(self, name, description):
        super().__init__(name, description,)
        self.strength = 1

    def use(self):
        self.equip()
        return
    
    def equip(self):
        return
        
        
        
