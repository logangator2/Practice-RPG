
import Character
import random

class Enemy(Character.Character):
    """
    An Enemy is a character that is not player controlled and dies when its HP runs out.
    """
    def __init__(self, name, health):
        """
        Values:
            * See Character for inherited variables *
        """
        super().__init__(name, health)

    def damage(self, value):
        """
        Decreases current health by value
        If c_health is < value, then Enemy dies
        Args:
            value: amount of damage dealt to character
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
        ADD: Modifiers for different weapons/armor/stats
        Args:
            other: another character whom is attacked
        Effects:
            Other character has their current health decreased by a random amount from 1 to 10
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

