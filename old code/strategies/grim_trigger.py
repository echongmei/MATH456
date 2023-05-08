class Grim_trigger():
    """
    The agent always cooperates until the other agent defects, 
    after which the agent only defects.
    """
    def __init__(self, player_id: int) -> None:
        self.history = []
        self.name = "Grim Trigger"
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
        #first move will always be cooperate
        if len(self.history) == 0:
            return 0
        #always defect if the other agent defected before
        if sum(opponent.history) > 0:
            return 1
        return 0
    