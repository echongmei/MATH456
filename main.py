import sys
import random

from defined_agents import *
from blind_agent import *

training_games = 50000  # How many training games are played 
turns = 20 # How many turns each training/testing game consists of 
games = 100 # How many testing games to play to

payoff_matrix = [[2, 2], # Both players cooperate
                [0, 3],  # Player 1 cooperates, player 2 defects
                [3, 0],  # Player 1 defects, player 2 cooperates
                [1, 1]]  # Both players defect


def create_table(table, i, player_1, player_2, Q_values): #collects all of the Q-values after every training game
   if i not in table[player_2.name]: # the table of all Q-values for every opponent strategy
      table[player_2.name][i] = {}
   for key in Q_values[player_2.name]:
      table[player_2.name][i][key] = [float(Q_values[player_2.name][key][0]), float(Q_values[player_2.name][key][1])]
   return table

   # if (i < 2) or (i == 25000-1): # only the games that appear in the 'snapshot' q-value table
   #    if i not in table[player_2.name]:
   #       table[player_2.name][i] = {}
   #    for key in Q_values[player_2.name]:
   #       table[player_2.name][i][key] = [float(Q_values[player_2.name][key][0]), float(Q_values[player_2.name][key][1])]
   # return table



def train_player(blind_player, training_games: int, turns: int): # traing the blind player
   table = {"Grim Trigger": {}, "Hard Majority": {}, 'Mean': {}, 'Nice': {}, "Reverse Tit For Tat": {}, "Tit For Tat": {} }
   defined_players = [Grim_Trigger(1), Hard_Majority(2), Mean(3), Nice(4), Reverse_Tit_For_Tat(5), Tit_For_Tat(6)]
   player_1 = blind_player
   for player in defined_players:
      
      player_2 = player
      for i in range(training_games):
         payoff_1 = []
         payoff_2 = []
         for j in range(turns):
            action_1 = player_1.choose_action(player_2)
            action_2 = player_2.choose_action(player_1)
            player_1.history.append(action_1)
            player_2.history.append(action_2)
         for j in range(turns):
            action_1 = player_1.history[j]
            action_2 = player_2.history[j]
            if action_1 == 0 and action_2 == 0: # Both players cooperate
               payoff_1.append(payoff_matrix[0][0])
               payoff_2.append(payoff_matrix[0][1])
            elif action_1 == 0 and action_2 == 1: # Only player 2 defects
               payoff_1.append(payoff_matrix[1][0])
               payoff_2.append(payoff_matrix[1][1])
            elif action_1 == 1 and action_2 == 0: # Only player 1 defects
               payoff_1.append(payoff_matrix[2][0])
               payoff_2.append(payoff_matrix[2][1])
            elif action_1 == 1 and action_2 == 1: # Both players defect
               payoff_1.append(payoff_matrix[3][0])
               payoff_2.append(payoff_matrix[3][1])
            round = j
            player_1.action_payoff(player_2, round, action_1, payoff_1[-1])

         # UNCOMMENT IF YOU WANT TO COLLECT Q-VALUES
         values = player_1.Q.copy()
         table = create_table(table, i, player_1, player_2, values)

         total_player1_payoff = sum(payoff_1)
         total_player2_payoff = sum(payoff_2)
         if total_player1_payoff > total_player2_payoff:
            avg_action_payoff = float(total_player1_payoff/turns)
            for j in range(turns):
               action_1 = player_1.history[j]
               player_1.action_payoff(player_2, round, action_1,  avg_action_payoff)
               
               player_1.update_wins()
               player_2.update_losses()
         if total_player1_payoff < total_player2_payoff:
            for j in range(turns):
               player_2.update_wins()
               player_1.update_losses()
         if total_player1_payoff == total_player2_payoff:
            for j in range(turns):
               player_2.update_ties()
               player_1.update_ties()
         player_1.analyze_outcome(player_2)
         
         player_1.reset()
         player_2.reset()

   return player_1, table # UNCOMMENT IF YOU WANT TO COLLECT Q-VALUES
   # return player_1
   

def play_games(blind_player, games, turns): # these are the testing games
   game_outcomes = {"Grim Trigger": {'wins': 0, 'losses': 0, 'ties': 0, 'percent cooporate': 0, 'percent defect': 0}, 
                    "Hard Majority": {'wins': 0, 'losses': 0, 'ties': 0, 'percent cooporate': 0, 'percent defect': 0}, 
                    'Mean': {'wins': 0, 'losses': 0, 'ties': 0, 'percent cooporate': 0, 'percent defect': 0}, 
                    'Nice': {'wins': 0, 'losses': 0, 'ties': 0, 'percent cooporate': 0, 'percent defect': 0}, 
                    "Reverse Tit For Tat": {'wins': 0, 'losses': 0, 'ties': 0, 'percent cooporate': 0, 'percent defect': 0}, 
                    "Tit For Tat": {'wins': 0, 'losses': 0, 'ties': 0, 'percent cooporate': 0, 'percent defect': 0} }

   defined_players = [Grim_Trigger(1), Hard_Majority(2), Mean(3), Nice(4), Reverse_Tit_For_Tat(5), Tit_For_Tat(6)]
   player_1 = blind_player
   for player in defined_players:

      player_1_wins = 0
      player_2_wins = 0
      ties = 0
      history = []
      player_2 = player
      for i in range(games):
         payoff_1 = []
         payoff_2 = []
         for j in range(turns):
            action_1 = player_1.choose_action(player_2)
            action_2 = player_2.choose_action(player_1)
            player_1.history.append(action_1)
            player_2.history.append(action_2)

         for j in range(turns):
            action_1 = player_1.history[j]
            action_2 = player_2.history[j]
            if action_1 == 0 and action_2 == 0: # Both players cooperate
               payoff_1.append(payoff_matrix[0][0])
               payoff_2.append(payoff_matrix[0][1])
            elif action_1 == 0 and action_2 == 1: # Only player 2 defects
               payoff_1.append(payoff_matrix[1][0])
               payoff_2.append(payoff_matrix[1][1])
            elif action_1 == 1 and action_2 == 0: # Only player 1 defects
               payoff_1.append(payoff_matrix[2][0])
               payoff_2.append(payoff_matrix[2][1])
            elif action_1 == 1 and action_2 == 1: # Both players defect
               payoff_1.append(payoff_matrix[3][0])
               payoff_2.append(payoff_matrix[3][1])
            round = j 
      
         total_player1_payoff = sum(payoff_1)
         total_player2_payoff = sum(payoff_2)

         if total_player1_payoff > total_player2_payoff:
            player_1_wins += 1
         elif total_player1_payoff < total_player2_payoff:
            player_2_wins += 1
         else:
            ties += 1

         history += player_1.history
         player_1.reset()
         player_2.reset()

      game_outcomes[player_2.name]['wins'] = player_1_wins
      game_outcomes[player_2.name]['losses'] = player_2_wins
      game_outcomes[player_2.name]['ties'] = ties
      game_outcomes[player_2.name]['percent cooporate'] = float(len(list(filter(lambda move: move == 0, history)))/len(history))
      game_outcomes[player_2.name]['percent defect'] = float(len(list(filter(lambda move: move == 1, history)))/len(history))

   return game_outcomes

# blind_player: the trained blind player, 
# table: the table of Q-values
# game_outcomes: the game_outcomes of the testing games

# blind_player = train_player(Blind(0), training_games, turns)
# # UNCOMMENT IF YOU WANT TO COLLECT Q-VALUES
blind_player, table = train_player(Blind(0),training_games, turns) 

game_outcomes = play_games(blind_player.reset(), games, turns)
print(game_outcomes)
