class Match():
    """condicts matches between two players"""
    
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

    def play(self):
        """
        Plays one round of the match
        """
        return
    
    def winner(self):
        """
        Returns the winner of the match
        """
        return
    
    def scores(self):
        """
        Returns the scores of the Match
        """
        return