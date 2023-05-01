class Tit_for_tat():
    
    def __init__(self, player_id):
        self.history = []
        self.name = "tit_for_tat"
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
        #copies opponent's last move
        if opponent.history[-1] == 1:
            return 1
        return 0