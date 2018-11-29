import random
import math

import Item

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
            defending: whether or not the current character has their defenses raised
        """
        self.name = name
        self.health = health
        self.c_health = health
        self.dead = False
        self.defending = False
        #self.speed = speed

    def __str__(self):
        return self.name

    def information(self):
        """
        Prints information about a character
        """
        print("Name: {}, Health: {}/{}".format(self.name, self.c_health, self.health))
        return

    def damage(self, value):
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
                self.c_health = self.health
                print("{} was healed to full health.".format(self.name))
                return
            else:
                if self.c_health + value >= self.health:
                    self.c_health = self.health
                    print("{} was healed to full health.".format(self.name))
                    return
                else:
                    self.c_health = self.c_health + value
                    print("{} was healed by {} points.".format(self.name, value))
                    return
        else:
            print("{} has died and cannot be healed!".format(self.name))
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
            print("\n{} did {} damage to {}".format(self.name, dmg, other.name))
            other.damage(dmg)
        return

    def defend(self):
        """
        The current character defends against a single damaging attack
        """
        print("{} is defending!".format(self.name))
        self.defending = True
        return

class Ally(Character):
    """
    An Ally is a character that is player controlled.
    """
    def __init__(self, name, health, level, experience, strength, defense, gold):
        """
        Values:
            * See Character for description of inherited variables *
            knockout: boolean to tell whether character is conscious
            experience: (int) metric for determining level
            level: int for general power level
            gold: int for how much money a character has
        """
        super().__init__(name, health)
        self.knockout = False
        self.strength = strength
        self.defense = defense
        self.experience = experience
        self.level = level
        self.gold = gold

        self.backpack = [] # FIXME: maybe a dict?

        self.mod_defense = defense

        #self.weapon = None
        #self.shield = None
        #self.r_weapon = None

        self.helmet = None
        self.torso = None
        self.leggings = None
        self.boots = None

    def information(self):
        print("\n\nName: {}".format(self.name))
        print("Health: {}/{}".format(self.c_health, self.health))
        print("Level: {}, Progress to Next Level: {}/{}".format(self.level, self.experience, self.next_level()))
        print("Strength: {}".format(self.strength))
        print("Defense: {}".format(self.mod_defense))
        print("Knocked Out: {}".format(self.knockout))
        print("Gold: {}".format(self.gold))
        print("Backpack: ")
        for item in self.backpack:
            print("-{}".format(item.name))
        return

    def next_level(self):
        """
        NOTE: level formula from http://howtomakeanrpg.com/a/how-to-make-an-rpg-levels.html
        Used by gain_xp to determine whether a character has leveled up
        Returns:
            n_level: int exp value of the next level
        """
        exponent = 1.5
        n_level = math.floor(100 * (self.level ** exponent))
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
        while (True):
            if self.experience >= self.next_level():
                self.experience = self.experience - self.next_level()
                # FIXME: add in stat gains here - based on level?
                self.health += 5
                self.strength += random.randint(1, 2)
                self.defense += random.randint(1, 2)

                self.c_health = self.health
                self.level += 1
                print("\n{} gained a level!".format(self.name))
                print("{} was healed to full health!".format(self.name))
            else:
                break
        return

    def equip(self, item):
        """
        Equips specific item to appropriate slot
        Args:
            item: Item object
        Effects:
            sets item to appropriate slot, then modifies appropriate stat
        """
        # check instance
        if isinstance(item, Item.Armor):
            # FIXME: generic way
            #if self.(item.a_type) != None:
            #    self.mod_defense = self.mod_defense - self.item.a_type.stat

            # FIXME: make more generic
            if item.a_type == "helmet":
                # NOTE: check if armor already equipped in slot, same for each armor type slot
                if self.helmet != None:
                    self.mod_defense = self.mod_defense - self.helmet.stat
                self.helmet = item
            elif item.a_type == "torso":
                if self.torso != None:
                    self.mod_defense = self.mod_defense - self.torso.stat
                self.torso = item
            elif item.a_type == "leggings":
                if self.leggings != None:
                    self.mod_defense = self.mod_defense - self.leggings.stat
                self.leggings = item
            elif item.a_type == "boots":
                if self.boots != None:
                    self.mod_defense = self.mod_defense - self.boots.stat
                self.boots = item
            # NOTE: doesn't need to catch inaccurate input because item wouldn't create

            self.mod_defense = self.mod_defense + item.stat
            print("\nYou equipped {}".format(item.name))
        else:
            print("This item can't be equipped!")
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
                    print("{} was healed by {} points.".format(self.name, value))
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

    def normal_attack(self, other):
        """
        The current character attacks another character with a normal attack.
        Args:
            other: another character whom is attacked
        Effects:
            Other character has their current health decreased, unless critical hit
        """
        crit_chance = random.randint(1, 20)
        if (crit_chance == 20):
            print("A critical hit! {} did {} damage to {}".format(self.name, 20 + self.strength, other.name))
            other.damage(20 + self.strength) # FIXME: change based on diff weapons/armor/strength, etc.
            return

        if self.c_health == 0:
            print("{} cannot attack.".format(self.name))
        else:
            dmg = random.randint(1, 10) + self.strength
            print("\n{} did {} damage to {}".format(self.name, dmg, other.name))
            other.damage(dmg)
        return

class Enemy(Character):
    """
    An Enemy is a character that is not player controlled and dies when its HP runs out instead of being knocked out.
    """
    def __init__(self, name, health, tier):
        """
        Values:
            * See Character for description of inherited variables *
        """
        super().__init__(name, health)
        tiers = {"weak" : 0.25, "annoying" : 0.75, "average" : 1, "strong" : 1.25, "boss" : 2}
        self.tier = tiers[tier]

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
        The current enemy attacks another character with a normal attack.
        Args:
            other: another character whom is attacked
        Effects:
            Other character has their current health decreased by a random amount, dependent on enemy tier
        """
        if not other.defending:
            crit_chance = random.randint(1, 20)
            if (crit_chance == 20):
                dmg = int(self.tier * 20 * (other.level / 2) - other.mod_defense)
                if dmg < 0:
                    dmg = random.randint(0, 1)
                print("A critical hit! {} did {} damage to {}".format(self.name, dmg, other.name))
                other.damage(dmg)
                return
            else:
                dmg = int(self.tier * random.randint(1, int(10 * (other.level / 2))) - other.mod_defense)
                if dmg <= 0:
                    dmg = random.randint(0, 1)
                print("{} did {} damage to {}".format(self.name, dmg, other.name))
                other.damage(dmg)
        else:
            print("{} made {}'s defenses lower.".format(self.name, other.name))
            other.damage(1)
        return

    def calc_experience(self, player_team):
        """
        Calculate experience of enemy based on their level and Enemy difficulty
        Args:
            player_team: list of player objects, used to find avg player level
        Returns:
            value: int for experience gained by players
        """
        levels = 0

        for p in player_team:
            levels += p.level
        avg_level = math.ceil(levels/len(player_team))

        # calculate xp value
        value = (50 * avg_level) * self.tier # FIXME: on higher levels this generates too much xp
        return value


