import sys
import random

class Blind():
    """
      The agent tries to figure out what another agent’s strategy is, then plays what’s
      best against that.
    """
    
    def __init__(self, player_id: int) -> None:
        self.history = []
        self.name = "Blind"
        self.round = 0
        self.player_id = player_id
        self.wins = 0
        self.losses = 0
        self.Q = {}
        self.epsilon_count = float(1)
        self.round_memory = 0
        self.guess_memory = {}
    
    def get_quality(self, opponent):
      #   quality_1 = self.Q[str(opponent.history[-self.round_memory:])][0]
      #   quality_2 = self.Q[str(opponent.history[-self.round_memory:])][1]
      #   print(self.Q[str(opponent.history[-self.round_memory:])][0])
      #   print(str(opponent.history[-self.round_memory:]), self.round_memory)

        quality_1 = self.Q[self.round][0]
        quality_2 = self.Q[self.round][1]
      #   print(quality_1, quality_2)
        return quality_1, quality_2
    
    def set_quality(self, opponent, quality_1, quality_2):
      #   self.Q[str(opponent.history[-self.round_memory:])][0] = quality_1
      #   self.Q[str(opponent.history[-self.round_memory:])][1] = quality_2
        self.Q[self.round][0] = quality_1
        self.Q[self.round][1] = quality_2
        print(self.Q[self.round])

    def nomalize_quality(self, opponent):
        quality_1, quality_2 = self.get_quality(opponent)
        γ = 0.95
        norm_value = min(quality_1, quality_2)
        self.set_quality(opponent, ((quality_1 - norm_value) * γ), ((quality_2 - norm_value) * γ))

    def maximize_quality(self, opponent):
       quality_1, quality_2 = self.get_quality(opponent)
       if (quality_1 == quality_2) or (random.random() < (1 / self.epsilon_count)):
           return random.randint(0, 1)
       elif (quality_1 > quality_2):
           return 0
       else: return 1

    def choose_action(self, opponent):
        self.epsilon_count += float(0.5)
      #   if str(opponent.history[-self.round_memory:]) not in self.Q:
      #       self.Q[str(opponent.history[-self.round_memory:])] = [0, 0]
      #   return self.maximize_quality(opponent)
        
        if (self.round) not in self.Q:
            self.Q[self.round] = [0, 0]
        return self.maximize_quality(opponent)

    def action_payoff(self, opponent, action, payoff):
      #   self.Q[str(opponent.history[-self.round_memory:])][action] += payoff
      #   print(self.Q)
        self.Q[self.round][action] += payoff
      #   print(self.Q[self.round][action], self.Q[self.round])
        self.nomalize_quality(opponent)

    def update_wins(self):
        self.wins += 1
   
    def update_losses(self):
        self.losses += 1
   
    def analyze_outcome(self):
        percent_won = 0
        if self.wins > 0:
            percent_won = float(self.wins / (self.wins + self.losses))
        cooperations = 0
        defections = 0
        for state in self.Q:
            action = self.maximize_quality(eval(state))
            if action == 0:
                cooperations += 1
            else:
                defections += 1
        percent_cooperated = 0
        if cooperations > 0:
            percent_cooperated = float(cooperations / len(self.Q))
        return self.wins, percent_won, percent_cooperated

    def reset_outcome_analysis(self):
        self.wins = 0
        self.losses = 0