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
      #   self.history = 0
        self.player_id = player_id
        self.wins = 0
        self.losses = 0
        self.Q = {}
        self.ε = 1  #the probability that we make moves based on past knowledge or just make random moves --> we want it to approach 0 as more rounds are played
        self.guess_memory = {}
        self.opponent_analysis = {}
    
    def get_quality(self, opponent):
      #   quality_1 = self.Q[str(opponent.history[-self.history_memory:])][0]
      #   quality_2 = self.Q[str(opponent.history[-self.history_memory:])][1]
      #   print(self.Q[str(opponent.history[-self.history_memory:])][0])
      #   print(str(opponent.history[-self.history_memory:]), self.history_memory)

        quality_1 = self.Q[str(self.history)][0]
        quality_2 = self.Q[str(self.history)][1]
      #   print(quality_1, quality_2)
        return quality_1, quality_2
    
    def set_quality(self, opponent, quality_1, quality_2):
      #   self.Q[str(opponent.history[-self.history_memory:])][0] = quality_1
      #   self.Q[str(opponent.history[-self.history_memory:])][1] = quality_2
        self.Q[str(self.history)][0] = quality_1
        self.Q[str(self.history)][1] = quality_2
      #   print(self.Q[str(self.history)])

   #  def normalize_quality(self, opponent):
   #      quality_1, quality_2 = self.get_quality(opponent)
   #      γ = 0.95
   #      norm_value = min(quality_1, quality_2)
   #    #   print(quality_1, quality_2, norm_value)
   #      self.set_quality(opponent, ((quality_1 - norm_value) * γ), ((quality_2 - norm_value) * γ))

    def maximize_quality(self, opponent):
       quality_1, quality_2 = self.get_quality(opponent)
       if (quality_1 == quality_2) or (random.random() < (1 / self.ε)):
           return random.randint(0, 1)
       elif (quality_1 > quality_2):
           return 0
       else: return 1

    def choose_action(self, opponent):
        self.ε += float(0.25)
      #   if str(opponent.history[-self.history_memory:]) not in self.Q:
      #       self.Q[str(opponent.history[-self.history_memory:])] = [0, 0]
      #   return self.maximize_quality(opponent)
      #   print(self.Q)
        if str(self.history) not in self.Q:
            self.Q[str(self.history)] = [0.0, 0.0]
        return self.maximize_quality(opponent)

    def action_payoff(self, round, action, payoff):
      #   self.Q[str(opponent.history[-self.history_memory:])][action] += payoff
      #   print(self.Q, self.history)
      #   self.Q[str(self.history)][action] += payoff
      #   print(self.Q[str(self.history)][action], self.Q[str(self.history)])
      #   self.normalize_quality(opponent)
         
      #   current_state = self.history
        current_Q = self.Q[str(self.history[:round])][action]
      #   print(self.Q[str(self.history[:round])])
        normalized_value = max(self.Q[str(self.history[:round])][0], self.Q[str(self.history[:round])][1])
        self.Q[str(self.history[:round])][action] = float(current_Q + 0.1*(payoff + (0.95*(normalized_value) - current_Q)))
        

    def update_wins(self):
        self.wins += 1
   
    def update_losses(self):
        self.losses += 1
   
    def analyze_outcome(self, opponent):
      #   print(len(list(filter(lambda move: move == 0, self.history))))
      #   print(self.history, opponent.history)
      #   print(self.Q)
        percent_won = 0
        if self.wins > 0:
            percent_won = float(self.wins / (self.wins + self.losses))
        cooperations = 0
        defections = 0
        for i in range(0, len(self.history)):
            action = self.maximize_quality(eval(str(self.history[i])))
            # print(action)
            if action == 0:
                cooperations += 1
            else:
                defections += 1
        percent_cooperated = 0
        if cooperations > 0:
            percent_cooperated = float(cooperations / len(self.Q))
      #   print(cooperations, defections)
      #   print('hi', self.wins, percent_won, percent_cooperated)
        return self.wins, percent_won, percent_cooperated

    def reset(self):
        self.wins = 0
        self.losses = 0
        
        self.history = []
      #   print(self.wins, self.losses, self.history, self.history)
        return self