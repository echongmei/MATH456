class Grim_trigger():
    """
    The agent always cooperates until the other agent defects, 
    after which the agent only defects.
    """
    def __init__(self, player_id):
        self.history = []
        self.name = "grim_trigger"
        self.round = 0
        self.player_id = player_id
    
    def strategy(self, opponent):
        """
            0 = cooperate
            1 = defect
        """
        #first move will always be cooperate
        if len(self.history) == 0:
            return 0
        #always defect the other agent defects
        if sum(opponent.history) > 0:
            return 1
        return 0
    