
import Character

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
        if self.defend == False:
            if value >= self.c_health:
                return self.death()
            else:
                self.c_health = self.c_health - value
        else:
            self.defend = False
        return

