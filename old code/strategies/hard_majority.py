class Hard_majority():
    """
    The agent defects on its first move, and will continue to defect if the
    number of defections of the opponent is greater than or equal to the number of times it
    has cooperated, otherwise the agent cooperates.
    """
    
    def __init__(self, player_id: int) -> None:
        self.history = []
        self.name = "Hard Majority"
        self.round = 0
        self.player_id = player_id
        self.total_score = 0
    
    
   #  def get_history(self) -> list:
   #      return self.history
   #  def get_name(self) -> str:
   #      return self.name
   #  def get_round(self) -> int:
   #      return self.round
   #  def get_playerID(self) -> int:
   #      return self.player_id
   #  def get_totalScore(self) -> int:
   #      return self.total_score
    

    
    def strategy(self, opponent) -> int:
        """
            0 = cooperate
            1 = defect
        """
        #first move will always be defect
        if len(self.history) == 0:
            return 1
        #always defect if the number of defections of the opponent is 
        # greater than or equal to the number of times it has cooperated
        print(opponent.history)
        num_cooperated = len(list(filter(lambda move: move == 0, opponent.history)))
      #   print(num_cooperated)
        num_defected = len(opponent.history) - num_cooperated
        print(num_cooperated, num_defected)
        if num_defected >= num_cooperated:
            return 1
        return 0
    