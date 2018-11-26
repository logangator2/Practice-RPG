
import math
import time

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
        self.description = "\n" + description

    def print_desc(self):
        """
        Prints description of the object
        """
        print(self.description)
        return

    def use(self):
        pass

class Potion(Item):
    """
    Generic potion item.
    Values:
        name: item name
        description: short description of item use
    """
    def __init__(self, name, description):
        super().__init__(name, description)

class Healing_Potion(Potion):
    """
    Healing Potion Item.
    Values:
        tier: a dict entry that determines strength of potion.
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

class Equipment(Item):
    """
    Generic Equipment Item class for weapons and armor
    Values:
        tiers: dict of possible tiers
        tier: dict selection
        stat: stat to be increased/decreased
    """
    def __init__(self, name, description, tier):
        super().__init__(name, description)
        self.tiers = {}

        self.tier = None
        self.stat = 0

    def scale(self, player_team):
        """
        Scales equipment power level to player_team avg_level
        Args:
            player_team: list of Ally objects
        Returns:
            value: stat value
        """
        levels = 0

        for p in player_team:
            levels += p.level
        avg_level = math.ceil(levels/len(player_team))

        # calculate scaling
        value = int(int(1 * avg_level) * self.tier)
        return value

class Armor(Equipment):
    """
    Armor class that increases Ally defense.
    Args:
        player_team: needs player team to scale power level
    Values:
        a_type: armor type, a dictionary selection that determines which slot it uses on a player when equipped
    """
    def __init__(self, name, description, tier, a_type, player_team):
        super().__init__(name, description, tier)
        tiers = {"Leather" : 1, "Chain" : 2, "Plate": 3, "Dragon" : 5}
        a_types = {"helmet" : "helmet", "torso" : "torso", "leggings" : "leggings", "boots" : "boots"}

        self.a_type = a_types[a_type]
        self.tier = tiers[tier]
        self.stat = self.scale(player_team)

class Weapon(Equipment):
    """
    Weapon class that increases Ally strength
    Args:
        player_team: needs player team to scale power level
    Values:
        w_type: a dictionary selection that determines which weapon the item is
    """
    def __init__(self, name, description, tier, w_type, player_team):
        super().__init__(name, description)
        tiers = {"Wood" : 0.25, "Stone" : 0.5, "Bronze" : 0.75, "Iron" : 1, "Steel" : 1.5}
        # w_types = {"Dagger" : , "Shortsword" : ,"Longsword" : , "Axe" : , "Katana" : ,
        #  "Trident" : , "Katana" : , "" : }
        w_types = []

        self.w_type = w_types[w_type]
        self.tier = tiers[tier]
        self.stat = self.scale(player_team)

        
        #self.name = "{} {} {}".format(coolness, self.tier, self.w_type)
        
def manage(player):
    """
    Separates item menu for code clarity.
    Args:
        player: Ally object with items in backpack list
    Effects:
        Manages items according to player commands.
    """
    while (True):
        print() # formatting
        for item in player.backpack:
            print(item.name)

        answer = input("\nWhich item would you like to look at? Press 'q' to leave item menu. ")
        if (answer.lower() == "quit") or (answer.lower() == "q"):
            break

        for item in player.backpack:
            if (answer.lower() == item.name.lower()):
                print("You can 'use', 'equip', 'toss' or 'view' an item description. You can use the first key of each command.")
                answer = input("What would you like to do with this item? ")

                # view desc
                if (answer.lower() == "view") or (answer.lower() == "v"):
                    print("\n{}: {}".format(item.name, item.description))

                # toss item
                elif (answer.lower() == "toss") or (answer.lower() == "t"):
                    player.backpack.remove(item)
                    print("\nYou tossed out {} and littered on the road!".format(item.name))

                # use if potion
                elif (answer.lower() == "use") or (answer.lower() == "u"):
                    if isinstance(item, Potion):
                        item.use(player)
                        time.sleep(1.5)
                    elif isinstance(item, Armor):
                        print("\nThis item cannot be used!")

                # equip if armor
                elif (answer.lower() == "equip") or (answer.lower() == "e"):
                    if isinstance(item, Potion):
                        print("\nThis item cannot be equipped!")
                    elif isinstance(item, Armor):
                        player.equip(item)
                        time.sleep(1.5)  

                else:
                    print("\nInvalid command!")
                    time.sleep(1.5)

            else:
                if (item == player.backpack[-1]):
                    print("That item isn't in your backpack!")
                    time.sleep(1.5)
    return      
        
