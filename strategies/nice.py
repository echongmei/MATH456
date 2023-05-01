import random

class Nice():
    """
    Player always cooperates
    """
    
    def __init__(self, player_id):
        self.history = []
        self.name = "nice"
        self.round = 0
        self.player_id = player_id
    
    def strategy(self):
        """
            0 = cooperate
            1 = defect
        """
        return 0