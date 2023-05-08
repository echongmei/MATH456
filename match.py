class Match():
    """conducts matches between two players"""
    
    def __init__(self, players = None, turns=None):
        """ 
        Parameters
        ----------
        players : tuple
            A pair of Player objects
        turns : integer
            The number of turns per match
        
        """
        
        self.players = players
        self.turns = turns
        self.payoff_matrix = [[[-1,-1], [-6,0]], [[0,-6],[-4,-4]]]
        
    # def play(self):
    #     """
    #     Plays one round of the match
    #     """
    #     return
    
    def winner(self, players):
        """
        Returns the winner of the match
        """
        max_score = -10000
        winner_player_id = -1
        for p in players:
            if max_score < p.total_score:
                max_score = p.total_score
                winner_player_id = p.player_id
        if winner_player_id == -1:
            raise ValueError("Failed to find winner")
        return winner_player_id
    
    def scores(self):
        """
        Returns the scores of the Match
        """
        return
