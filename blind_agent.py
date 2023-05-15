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
        self.ties = 0
        self.Q = {"Grim Trigger": {}, "Hard Majority": {}, 'Mean': {}, 'Nice': {}, "Reverse Tit For Tat": {}, "Tit For Tat": {} }
        self.ε = 1  #the probability that we make moves based on past knowledge or just make random moves --> we want it to approach 0 as more rounds are played
        self.guess_memory = {}
        self.analysis = {"Grim Trigger": {}, "Hard Majority": {}, 'Mean': {}, 'Nice': {}, "Reverse Tit For Tat": {}, "Tit For Tat": {} }
    
    def get_quality(self, opponent):
      #   quality_1 = self.Q[str(opponent.history[-self.history_memory:])][0]
      #   quality_2 = self.Q[str(opponent.history[-self.history_memory:])][1]
      #   print(self.Q[str(opponent.history[-self.history_memory:])][0])
      #   print(str(opponent.history[-self.history_memory:]), self.history_memory)

        quality_1 = self.Q[opponent.name][str(self.history)][0]
        quality_2 = self.Q[opponent.name][str(self.history)][1]
      #   print(quality_1, quality_2)
        return quality_1, quality_2
    
    def set_quality(self, opponent, quality_1, quality_2):
      #   self.Q[str(opponent.history[-self.history_memory:])][0] = quality_1
      #   self.Q[str(opponent.history[-self.history_memory:])][1] = quality_2
        self.Q[opponent.name][str(self.history)][0] = quality_1
        self.Q[opponent.name][str(self.history)][1] = quality_2
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
         #   print('random')
           return random.randint(0, 1)
       elif (quality_1 > quality_2):
         #   print('q1 > q2')
           return 0
       else: return 1

    def choose_action(self, opponent):
        self.ε += float(0.25)
      #   if str(opponent.history[-self.history_memory:]) not in self.Q:
      #       self.Q[str(opponent.history[-self.history_memory:])] = [0, 0]
      #   return self.maximize_quality(opponent)
      #   print(self.Q)
        if str(self.history) not in self.Q[opponent.name]:
            # print('hi', self.history)
            self.Q[opponent.name][str(self.history)] = [0.0, 0.0]
        max = self.maximize_quality(opponent)
      #   print(max)
      #   print('MAX', max)
        return max
      #   return self.maximize_quality(opponent)

    def action_payoff(self, opponent, round, action, payoff):
      #   self.Q[str(opponent.history[-self.history_memory:])][action] += payoff
      #   print(self.Q, self.history)
      #   self.Q[str(self.history)][action] += payoff
      #   print(self.Q[str(self.history)][action], self.Q[str(self.history)])
      #   self.normalize_quality(opponent)
         
      #   current_state = self.history
        current_Q = self.Q[opponent.name][str(self.history[:round])][action]
        
      #   temp_history = self.history
      #   self.history = temp_history[:round]
      #   print(opponent.history[:round], self.history)
      #   opponent_next_move = opponent.choose_action(self)
      #   print(opponent_next_move)
      #   print(opponent.history[:round], self.history)
      #   self.history = temp_history
      #   print(self.Q[str(self.history[:round])])
        normalized_value = max(self.Q[opponent.name][str(self.history[:round])][0], self.Q[opponent.name][str(self.history[:round])][1])
        self.Q[opponent.name][str(self.history[:round])][action] = float(current_Q + 0.1*(payoff + (0.95*(normalized_value) - current_Q)))
        

    def update_wins(self):
        self.wins += 1
   
    def update_losses(self):
        self.losses += 1

    def update_ties(self):
        self.ties += 1
   
    def analyze_outcome(self, opponent):
      #   print(len(list(filter(lambda move: move == 0, self.history))))
      #   print(self.history, opponent.history)
      #   print(self.Q)
        percent_won = 0
      
        if self.wins > 0:
            percent_won = float(self.wins / len(self.history))
            # if percent_won >= 1.0:
            #    #   print('wins', self.history, self.wins, self.losses, self.ties, percent_won)
            #    #  return   

        
         # return 'ERROR'
        cooperations = 0
        defections = 0
        for i in range(0, len(self.history)):
            # print(str(self.history[:i]))

            action = self.history[i]
            # print(action)
            if action == 0:
                cooperations += 1
            else:
                defections += 1
        percent_cooperated = 0
        if cooperations > 0:
            percent_cooperated = float(cooperations / len(self.history))
      #   print(cooperations, defections)
      #   print('hi', self.wins, percent_won, percent_cooperated)
      #   print(self.analysis)
        if str(self.history) not in self.analysis[opponent.name]:
            self.analysis[opponent.name][str(self.history)] = [self.wins, percent_won, percent_cooperated]
            # print(self.analysis[opponent.name])
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
        
      #   print(self.wins, self.losses, self.history, self.history)
        return self