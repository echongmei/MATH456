import sys



class Grim_Trigger():
    def __init__(self, player_id: int) -> None:
      self.history = []
      self.name = "Grim Trigger"
      self.round = 0
      self.player_id = player_id
      self.wins = 0
      self.losses = 0
      
    def choose_action(self, opponent): #this is the players strategy
       if (len(self.history)  == 0) or (self.round == 0):
          return 0
       elif sum(opponent.history) > 0:
          return 1
       else:
          return 0
       
    def update_wins(self):
        self.wins += 1
   
    def update_losses(self):
        self.losses += 1
 
    def analyze_outcome(self):
      percent_won = 0
      if self.wins > 0:
         percent_won = float(self.wins / (self.wins + self.losses))
      elif self.losses > 0:
        percent_won = 1 - float(self.losses / (self.wins + self.losses))
         
        return self.wins, percent_won
      


class Hard_Majority():
    def __init__(self, player_id: int) -> None:
      self.history = []
      self.name = "Hard Majority"
      self.round = 0
      self.player_id = player_id
      self.wins = 0
      self.losses = 0
      
    def choose_action(self, opponent): #this is the players strategy
       opponent_cooperations = len(list(filter(lambda move: move == 0, opponent.history)))
       opponent_defections = len(opponent.history) - opponent_cooperations
       if (len(self.history)  == 0) or (self.round == 0):
          return 1
       elif opponent_defections >= opponent_cooperations:
          return 1
       else:
          return 0
       
    def update_wins(self):
        self.wins += 1
   
    def update_losses(self):
        self.losses += 1
 
    def analyze_outcome(self):
      percent_won = 0
      if self.wins > 0:
         percent_won = float(self.wins / (self.wins + self.losses))
      elif self.losses > 0:
        percent_won = 1 - float(self.losses / (self.wins + self.losses))
         
        return self.wins, percent_won


class Mean():
    def __init__(self, player_id: int) -> None:
      self.history = []
      self.name = "Mean"
      self.round = 0
      self.player_id = player_id
      self.wins = 0
      self.losses = 0
      
    def choose_action(self, opponent): #this is the players strategy
          return 1
       
    def update_wins(self):
        self.wins += 1
   
    def update_losses(self):
        self.losses += 1
 
    def analyze_outcome(self):
      percent_won = 0
      if self.wins > 0:
         percent_won = float(self.wins / (self.wins + self.losses))
      elif self.losses > 0:
        percent_won = 1 - float(self.losses / (self.wins + self.losses))
         
        return self.wins, percent_won
      


class Nice():
    def __init__(self, player_id: int) -> None:
      self.history = []
      self.name = "Nice"
      self.round = 0
      self.player_id = player_id
      self.wins = 0
      self.losses = 0
      
    def choose_action(self, opponent): #this is the players strategy
          return 0
       
    def update_wins(self):
        self.wins += 1
   
    def update_losses(self):
        self.losses += 1
 
    def analyze_outcome(self):
      percent_won = 0
      if self.wins > 0:
         percent_won = float(self.wins / (self.wins + self.losses))
      elif self.losses > 0:
        percent_won = 1 - float(self.losses / (self.wins + self.losses))
         
        return self.wins, percent_won
      


class Reverse_Tit_For_Tat():
    def __init__(self, player_id: int) -> None:
      self.history = []
      self.name = "Reverse Tit For Tat"
      self.round = 0
      self.player_id = player_id
      self.wins = 0
      self.losses = 0
      
    def choose_action(self, opponent): #this is the players strategy
       if (len(self.history)  == 0) or (self.round == 0):
          return 1
       elif opponent.history[-1] == 0:
          return 1
       else:
          return 0
       
    def update_wins(self):
        self.wins += 1
   
    def update_losses(self):
        self.losses += 1
 
    def analyze_outcome(self):
      percent_won = 0
      if self.wins > 0:
         percent_won = float(self.wins / (self.wins + self.losses))
      elif self.losses > 0:
        percent_won = 1 - float(self.losses / (self.wins + self.losses))
         
        return self.wins, percent_won
      

class Tit_For_Tat():
    def __init__(self, player_id: int) -> None:
      self.history = []
      self.name = "Tit For Tat"
      self.round = 0
      self.player_id = player_id
      self.wins = 0
      self.losses = 0
      
    def choose_action(self, opponent): #this is the players strategy
       if (len(self.history)  == 0) or (self.round == 0):
          return 0
       elif opponent.history[-1] == 1:
          return 1
       else:
          return 0
       
    def update_wins(self):
        self.wins += 1
   
    def update_losses(self):
        self.losses += 1
 
    def analyze_outcome(self):
      percent_won = 0
      if self.wins > 0:
         percent_won = float(self.wins / (self.wins + self.losses))
      elif self.losses > 0:
        percent_won = 1 - float(self.losses / (self.wins + self.losses))
         
        return self.wins, percent_won