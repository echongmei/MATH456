import random

class Blind():
    """
    The agent tries to figure out what another agent’s strategy is, then plays what’s
    best against that.
    """
    
    
    def __init__(self, player_id):
        self.history = []
        self.name = "blind"
        self.round = 0
        self.player_id = player_id
        self.total_score = 0
    
    def strategy(self, opponent):
        """
            0 = cooperate
            1 = defect
        """
        #first move will always be cooperate
        if len(self.history) == 0:
            return 0
        #always defect if the other agent defected before
        if sum(opponent.history) > 0:
            return 1
        return 0
    