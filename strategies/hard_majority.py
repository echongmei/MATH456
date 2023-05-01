class Hard_majority():
    """
    The agent defects on its first move, and will continue to defect if the
    number of defections of the opponent is greater than or equal to the number of times it
    has cooperated, otherwise the agent cooperates.
    """
    
    def __init__(self, player_id):
        self.history = []
        self.name = "hard_majority"
        self.round = 0
        self.player_id = player_id
    
    def strategy(self, opponent):
        """
            0 = cooperate
            1 = defect
        """
        #first move will always be defect
        if len(self.history) == 1:
            return 1
        #always defect if the number of defections of the opponent is 
        # greater than or equal to the number of times it has cooperated
        num_defected = sum(opponent.history)
        num_cooperated = len(opponent.history) - num_defected
        if num_defected >= num_cooperated:
            return 1
        return 0
    