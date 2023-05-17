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
        self.player_id = player_id
        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.Q = {"Grim Trigger": {}, "Hard Majority": {}, 'Mean': {}, 'Nice': {}, "Reverse Tit For Tat": {}, "Tit For Tat": {} }
        self.ε = 1  #the probability that we make moves based on past knowledge or just make random moves --> we want it to approach 0 as more rounds are played
        self.guess_memory = {}
        self.analysis = {"Grim Trigger": {}, "Hard Majority": {}, 'Mean': {}, 'Nice': {}, "Reverse Tit For Tat": {}, "Tit For Tat": {} }
        
    
    def get_quality(self, opponent):
        quality_1 = self.Q[opponent.name][str(self.history)][0]
        quality_2 = self.Q[opponent.name][str(self.history)][1]
        return quality_1, quality_2
    
    def set_quality(self, opponent, quality_1, quality_2):
        self.Q[opponent.name][str(self.history)][0] = quality_1
        self.Q[opponent.name][str(self.history)][1] = quality_2
      
    def maximize_quality(self, opponent):
       quality_1, quality_2 = self.get_quality(opponent)
       if (quality_1 == quality_2) or (random.random() < (1 / self.ε)):
           return random.randint(0, 1)
       elif (quality_1 > quality_2):
           return 0
       else: return 1

    def choose_action(self, opponent):
        self.ε += float(0.25)
        if str(self.history) not in self.Q[opponent.name]:
            self.Q[opponent.name][str(self.history)] = [0.0, 0.0]
        return self.maximize_quality(opponent)

    def action_payoff(self, opponent, round, action, payoff):
        current_Q = self.Q[opponent.name][str(self.history[:round])][action]
        normalized_value = max(self.Q[opponent.name][str(self.history[:round])][0], self.Q[opponent.name][str(self.history[:round])][1])
        self.Q[opponent.name][str(self.history[:round])][action] = float(current_Q + 0.1*(payoff + (0.95*(normalized_value) - current_Q)))
        

    def update_wins(self):
        self.wins += 1
   
    def update_losses(self):
        self.losses += 1

    def update_ties(self):
        self.ties += 1
   
    def analyze_outcome(self, opponent):
        percent_won = 0
      
        if self.wins > 0:
            percent_won = float(self.wins / len(self.history))
        cooperations = 0
        defections = 0
        for i in range(0, len(self.history)):
            action = self.history[i]
            if action == 0:
                cooperations += 1
            else:
                defections += 1
        percent_cooperated = 0
        if cooperations > 0:
            percent_cooperated = float(cooperations / len(self.history))
        if str(self.history) not in self.analysis[opponent.name]:
            self.analysis[opponent.name][str(self.history)] = [self.wins, percent_won, percent_cooperated]
        else:
            if max(self.analysis[opponent.name][str(self.history)][0], self.wins) == self.wins:                   
               self.analysis[opponent.name][str(self.history)][0] = self.wins
               self.analysis[opponent.name][str(self.history)][1] = percent_won
               self.analysis[opponent.name][str(self.history)][2] = percent_cooperated
            else:
               self.analysis[opponent.name][str(self.history)][0] = float((self.analysis[opponent.name][str(self.history)][0] + self.wins)/2)
               self.analysis[opponent.name][str(self.history)][1] = float((self.analysis[opponent.name][str(self.history)][1] + percent_won)/2)
               self.analysis[opponent.name][str(self.history)][2] = float((self.analysis[opponent.name][str(self.history)][2] + percent_cooperated)/2)
        
        return self.wins, percent_won, percent_cooperated

    def reset(self):
        self.wins = 0
        self.ties = 0
        self.losses = 0
        self.history = []        
        return self