
class Environment():
    """
    Environment class that manages all temporary stat changes.
    """
    def __init__(self, character_list):
        """
        Values:
            character_list: a list of Ally objects
            enemy_list: a list of Enemy objects
        """
        self.character_list = []
        self.enemy_list = []