import random
import math

class Character:
    """
    Character class to hold and react to the simulated world around them
    """
    def __init__(self, name, level, experience, health, gold):
        """
        Values:
            name: str name for the character
            health: integer value for maximum health
            c_health: integer value for current health
            player_c: boolean value for whether character is a player character or not
            dead: whether or not the current character is dead
            knockout: whether or not the current character is knocked out
            defending: whether or not the current character has their defenses raised
        """
        self.name = name
        self.health = health
        self.c_health = health
        self.dead = False
        self.knockout = False
        self.defending = False
        #self.speed = speed
        #self.strength = strength
        self.experience = experience
        self.level = level
        self.gold = gold

        #self.backpack = []

        #self.weapon = None
        #self.shield = None
        #self.r_weapon = None

        #self.helmet = None
        #self.torso = None
        #self.leggings = None
        #self.boots = None

    def __str__(self):
        return self.name

    def information(self): # FIXME: Add more information, change to print statements
        """
        Returns all values of the character
        Returns:
            character_dict: a dictionary of all of the character's traits and equipment
        """
        character_dict = {"Name": self.name, "Current Health": self.c_health, 
            "Max Health": self.health, "Knocked Out" : self.knockout, "Gold" : self.gold}
        return character_dict

    def next_level(self):
        """
        NOTE: level formula from http://howtomakeanrpg.com/a/how-to-make-an-rpg-levels.html
        Used by gain_xp to determine whether a character has leveled up
        Returns:
            n_level: int value of the next level
        """
        exponent = 1.5
        n_level = math.floor(1000 * (self.level ** exponent))
        return n_level

    def gain_xp(self, value):
        """
        Adds experience to player's pool.
        Args:
            value: int by which to increase experience
        Effects:
            1. If player gained experience > required experience for the next level, gain a level
            2. Else, simply add value to experience pool
        """
        self.experience += value
        print("\n{} gained {} experience!".format(self.name, value))

        # check if level gain
        if self.experience > self.next_level():
            self.level += 1
            print("\n{} gained a level!".format(self.name))
        return

    def damage(self, value):
        """
        Three cases:
            1. Decreases current health by value
            2. If value is greater than current health, knockout character
            3. If value is greater than two times current health, kill character
        Args:
            value: amount of damage dealt to character
        """
        if self.defending == False:
            if value >= self.c_health:
                if value >= self.health * 2:
                    return self.death()
                else:
                    return self.ko()
            else:
                self.c_health = self.c_health - value
                print("{} took {} damage!".format(self.name, value))
        else:
            self.defending = False
            print("{}'s defenses were lowered!".format(self.name))
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
                print("{} was healed to full health.".format(self.name))
                return
            else:
                if self.c_health + value >= self.health:
                    self.knockout = False
                    self.c_health = self.health
                    print("{} was healed to full health.".format(self.name))
                    return
                else:
                    self.c_health = self.c_health + value
                    self.knockout = False
                    print("{} was healed by {} points.".format(self.name, self.value))
                    return
        else:
            print("{} has died and cannot be healed!".format(self.name))
            return

    def ko(self):
        """
        Handles if a character's current health drops to 0.
        """
        self.c_health = 0
        self.knockout = True
        print("{} has been knocked out!".format(self.name))
        return

    def death(self):
        """
        Handles if a character's current health drops to 0 
        ...and the damage done is more than double the character's maximum health.
        """
        self.c_health = 0
        self.dead = True
        print("{} died!".format(self.name))
        return

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
            print("{} was revived for {} health!".format(self.name, value))
            return
        else:
            print("Revival of {} failed!".format(self.name))
            return

    def normal_attack(self, other):
        """
        The current character attacks another character with a normal attack.
        ADD: Modifiers for different weapons/armor/stats/strength
        Args:
            other: another character whom is attacked
        Effects:
            Other character has their current health decreased by a random amount from 1 to 10, unless it is
            ...a critical hit, which does 20.
        """
        crit_chance = random.randint(1, 20)
        if (crit_chance == 20):
            print("A critical hit! {} did {} damage to {}".format(self.name, 20, other.name))
            other.damage(20) # FIXME: change based on diff weapons/armor/strength, etc.
            return

        if self.c_health == 0:
            print("{} cannot attack.".format(self.name))
        else:
            dmg = random.randint(1, 10)
            print("{} did {} damage to {}".format(self.name, dmg, other.name))
            other.damage(dmg)
        return

    def defend(self):
        """
        The current character defends against a single damaging attack
        """
        print("{} is defending!".format(self.name))
        self.defending = True
        return

class Enemy(Character):
    """
    An Enemy is a character that is not player controlled and dies when its HP runs out instead of being knocked out.
    """
    def __init__(self, name, level, experience, health, gold):
        """
        Values:
            * See Character for description of inherited variables *
        """
        super().__init__(name, level, experience, health, gold)

    def damage(self, value):
        """
        Decreases current health by value
        If c_health is < value, then Enemy dies
        Args:
            value: amount of damage dealt to self
        """
        if self.defending == False:
            if value >= self.c_health:
                return self.death()
            else:
                self.c_health = self.c_health - value
        else:
            self.defending = False
            print("{}'s defenses were lowered!".format(self.name))
        return

    def normal_attack(self, other):
        """
        The current character attacks another character with a normal attack.
        ADD: Modifiers for different weapons/armor/stats/strength
        Args:
            other: another character whom is attacked
        Effects:
            Other character has their current health decreased by a random amount from 1 to 4 or 10 if critical hit
        """
        crit_chance = random.randint(1, 10)
        if (crit_chance == 10):
            other.damage(10) # FIXME: may want to change based on diff weapons/armor, etc.
            print("A critical hit! {} did {} damage to {}".format(self.name, 10, other.name))
            return
        else:
            dmg = random.randint(1, 4)
            print("{} did {} damage to {}".format(self.name, dmg, other.name))
            other.damage(dmg)
        return


