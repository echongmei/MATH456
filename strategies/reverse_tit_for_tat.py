class Reverse_tit_for_tat:
    def __init__(self, player_id):
        self.history = []
        self.name = "reverse_tit_for_tat"
        self.round = 0
        self.player_id = player_id
    
    def strategy(self, opponent):
        """
            0 = cooperate
            1 = defect
        """
        #first move will always be defect
        if len(self.history) == 0:
            return 1
        #plays the opposite of opponent's last move
        if opponent.history[-1] == 0:
            return 1
        return 0