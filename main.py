import sys
import random

from defined_agents import *
from blind_agent import *

# https://towardsdatascience.com/a-beginners-guide-to-q-learning-c3e2a30a653c


# population_size = 1 # How many AIs in the population
opponents = 6 # How many instances of each defined strategy there are
# episode_length =  # How many turns to play
# ε = 0.1 # the probability that we make moves based on past knowledge or just make random moves --> we want it to approach 0 as more rounds are played
training_games = 100  # How long to train in seconds per agent
turns = 3
games = 10 # How many episodes to play during the testing phase



payoff_matrix = [[2, 2], # Both players cooperate
                [0, 3],  # Player 1 cooperates, player 2 defects
                [3, 0],  # Player 1 defects, player 2 cooperates
                [1, 1]]  # Both players defect


def train_player(blind_player, training_games: int, turns: int):
   ties = 0
   defined_players = [Grim_Trigger(1), Hard_Majority(2), Mean(3), Nice(4), Reverse_Tit_For_Tat(5), Tit_For_Tat(6)]
   player_1 = blind_player
   for player in defined_players[:1]:
      player_2 = player
      for i in range(training_games):
         # print(player_2.name)
         payoff_1 = []
         payoff_2 = []
         # print(i*turns)
         # player_1.round = i*turns
         print('line 39', player_1.Q)
         for j in range(turns):
            
            # print(payoff_1, payoff_2)
            action_1 = player_1.choose_action(player_2)
            action_2 = player_2.choose_action(player_1)
            player_1.history.append(action_1)
            player_2.history.append(action_2)
            # print(player_1.history, player_2.history)
            # print(j, player_1.Q)
            
            # player_1.round = (i*turns) + (j + 1)
            # player_2.round = (i*turns) + (j + 1)
            # print(j, player_1.Q, player_1.history, player_2.history[-len(player_1.history):])
         # print(player_2.name, player_1.history, player_2.history[-len(player_1.history):])
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
            # player_1.action_payoff(round, action_1, payoff_1[-1])
         # print(player_1.Q)
         # print(payoff_1, len(payoff_1), sum(payoff_1), sum(payoff_2))
         total_player1_payoff = sum(payoff_1)
         total_player2_payoff = sum(payoff_2)
         # print(sum(payoff_1), sum(payoff_2))
         if total_player1_payoff > total_player2_payoff:
            # print(sum(payoff_1,payoff_2))
            avg_action_payoff = float(total_player1_payoff/turns)
            for j in range(turns):
               # round = j + (i*turns)
               action_1 = player_1.history[j]
               player_1.action_payoff(round, action_1, avg_action_payoff)
               
               player_1.update_wins()
               player_2.update_losses()
         if total_player1_payoff < total_player2_payoff:
            
            for j in range(turns):
               player_2.update_wins()
               player_1.update_losses()
            print(player_1.analyze_outcome(player_2), player_2.wins)
         if total_player1_payoff == total_player2_payoff:
            for j in range(turns):
               player_2.update_ties()
               player_1.update_ties()
         # # break
         # print(len(payoff_1))
         # player_1.round -= 1
         # player_2.round -= 1
         # print(player_1.wins)
        
         # player_1.reset()
         
         print(player_1.history)
         print(player_2.history)
         player_2.wins = 0
         
         player_2.losses = 0
         player_1.wins = 0
         player_1.ties = 0
         
         player_1.losses = 0
         player_2.ties = 0
         player_2.history = []
         player_1.history = []
      # print(player_1.Q)
      # break
      # print(player_1.Q)
   # print(player_1.wins)
   return player_1
   
# train_player(Blind(0),training_games, turns)

def play_games(blind_player, games, turns):
   player_1_wins = 0
   player_2_wins = 0
   ties = 0
   defined_players = [Grim_Trigger(1), Hard_Majority(2), Mean(3), Nice(4), Reverse_Tit_For_Tat(5), Tit_For_Tat(6)]
   player_1 = blind_player
   for player in defined_players[-1:]:
      player_2 = player
      for i in range(games):
         payoff_1 = []
         payoff_2 = []
         # player_1.round = i*turns
         for j in range(turns):
            # print(payoff_1, payoff_2)
            action_1 = player_1.choose_action(player_2)
            action_2 = player_2.choose_action(player_1)
            player_1.history.append(action_1)
            player_2.history.append(action_2)
            # print(player_1.round, player_1.history, )
            # print(j, player_1.Q)
            
            # player_1.round = (i*turns) + (j + 1)
            # player_2.round = (i*turns) + (j + 1)
            # print(j, player_1.Q, player_1.history, player_2.history[-len(player_1.history):])
         # print(player_1.history)

         # print(player_2.name, player_1.history, player_2.history[-len(player_1.history):])
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
            player_1.action_payoff(round, action_1, payoff_1[-1])
      
         total_player1_payoff = sum(payoff_1)
         total_player2_payoff = sum(payoff_2)
         # print(total_player1_payoff, total_player2_payoff)
         if total_player1_payoff > total_player2_payoff:
            player_1_wins += 1
            # print(player_1_wins)
         elif total_player1_payoff < total_player2_payoff:
            player_2_wins += 1
         else:
            ties += 1
      # break
   return player_1_wins, player_2_wins, ties


blind_player = train_player(Blind(0),training_games, turns)
# print(play_games(blind_player.reset(), games, turns))
# print(play_games(blind_player, games, turns))