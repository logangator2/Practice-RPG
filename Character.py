import random

class Character:
    """
    Character class to hold and react to the simulated world around them
    """
    def __init__(self, name, health):
        """
        Values:
            name: str name for the character
            health: integer value for maximum health
            c_health: integer value for current health
            dead: whether or not the current character is dead
            knockout: whether or not the current character is knocked out

        """
        self.name = name
        self.health = health
        self.c_health = health
        self.dead = False
        self.knockout = False
        self.defend = False
        #self.speed = speed

        #self.item1 = None
        #self.item2 = None
        #self.item3 = None

        #self.helmet = None
        #self.torso = None
        #self.leggings = None
        #self.boots = None

    def __str__(self):
        return self.name

    def information(self): # ADD: Add more information
        """
        Returns all values of the character
        """
        character_dict = {"Name": self.name, "Current Health": self.c_health, 
            "Max Health": self.health, "Dead" : self.dead}
        return character_dict

    def damage(self, value):
        """
        Three cases:
            1. Decreases current health by value
            2. If value is greater than current health, knockout character
            3. If value is greater than two times current health, kill character
        Args:
            value: amount of damage dealt to character
        """
        if self.defend == False:
            if value >= self.c_health:
                if value >= self.health * 2:
                    return self.death()
                else:
                    return self.knockout()
            else:
                self.c_health = self.c_health - value
        else:
            self.defend = False
        return

    def healing(self, value):
        """
        Handles when a character regains health.
        Args:
            value: number the character is healed by
        Effects:
            The character regains health up to their maximum by the value given.
        """
        if self.dead == False:
            if value >= self.health:
                self.knockout = False
                self.c_health = self.health
                return "{} was healed to full health.".format(self.name)
            else:
                if self.c_health + value >= self.health:
                    self.knockout = False
                    self.c_health = self.health
                    return "{} was healed to full health.".format(self.name)
                else:
                    self.c_health = self.c_health + value
                    self.knockout = False
                    return "{} was healed by {} points.".format(self.name, self.value)
        else:
            return "{} has died and cannot be healed!".format(self.name)

    def knockout(self):
        """
        Handles if a character's current health drops to 0.
        """
        self.c_health = 0
        self.knockout = True
        return "{} has been knocked out!".format(self.name)

    def death(self):
        """
        Handles if a character's current health drops to 0 
        ...and the damage done is more than double the character's maximum health.
        """
        self.c_health = 0
        self.dead = True
        return "{} died!".format(self.name)

    def dead(self):
        return self.dead

    def revive(self, value):
        """
        Handles if a character is revived.
        Args:
            value: number the character is healed by
        Effects:
            The character is brought back to life and regains health up to their maximum.
        """
        if value > 0:
            if value >= self.health:
                self.c_health = self.health
            else:
                self.c_health = value
            self.dead = False
            return "{} was revived!".format(self.name)
        else:
            return "ERROR REVIVING {}".format(self.name)

    def normal_attack(self, other):
        """
        The current character attacks another character with a normal attack.
        ADD: Modifiers for different weapons/armor/stats
        Args:
            other: another character whom is attacked
        Effects:
            Other character has their temporary health decreased by a random amount from 1 to 10
        """
        if self.c_health == 0:
            print("{} cannot attack.".format(self.name))
        else:
            dmg = random.randint(1, 10)
            other.damage(dmg)
            print("{} did {} damage to {}".format(self.name, dmg, other.name))
        return

    def defend(self):
        """
        The current character defends against a single damaging attack
        """
        self.defend = True
        return


