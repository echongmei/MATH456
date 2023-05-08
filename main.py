import sys
import random

from defined_agents import *
from blind_agent import *

# 1. create blind agent
# 2. create adversary agents 
# 3. define training rounds
# 4. use a while loop to perform training rounds

#    4a. 

payoff_matrix = [[2, 2], # Both players cooperate
                [0, 3], # Player 1 cooperates, player 2 defects
                [3, 0], # Player 1 defects, player 2 cooperates
                [1, 1]] # Both players defect
def check_for_win(player_1, player_2, action_payoffs):
   if action_payoffs['player 1'] > action_payoffs['player 1']:
      player_1.action_payoff(player_2, player_1.history[-1], action_payoffs['player 1'][-1]) #CHECK FOR DVE
      player_1.update_wins()
      player_2.update_losses()


def train_blind_agent(blind_agent, training_rounds):
    adversary_agents = []
    for i in range(3, 4): #creates one agent for each of the definied strategies
        if i == 1:
           adversary_agents.append(Grim_Trigger(i))
        if i == 2:
           adversary_agents.append(Hard_Majority(i))
        if i == 3:
            adversary_agents.append(Mean(i))
        if i == 4:
            adversary_agents.append(Nice(i))
        if i == 5:
            adversary_agents.append(Reverse_Tit_For_Tat(i))
        if i == 6:
           adversary_agents.append(Tit_For_Tat(i))
    
    
    for j in range(len(adversary_agents)):
        remaining_rounds = training_rounds
        win_condition = False
        player_1 = blind_agent
        player_2 = adversary_agents[j]
        action_payoffs = {'player 1': [], 'player 2': []}
        while remaining_rounds > 0:
            print('round', remaining_rounds)
            # while not win_condition: #if player 1 wins and if they guess strategy correctly
            
            player_1.history.append(player_1.choose_action(player_2))
            player_2.history.append(player_2.choose_action(player_1))
            print(player_1.history, player_2.history)
            
            if player_1.history[-1] == 0:
                if player_2.history[-1] == player_1.history[-1]:
                  action_payoffs['player 1'].append(payoff_matrix[0][0])
                  action_payoffs['player 2'].append(payoff_matrix[0][1])
                if player_2.history[-1] != player_1.history[-1]:
                  action_payoffs['player 1'].append(payoff_matrix[1][0])
                  action_payoffs['player 2'].append(payoff_matrix[1][1])
            if player_1.history[-1] == 1:
                if player_2.history[-1] == player_1.history[-1]:
                  action_payoffs['player 1'].append(payoff_matrix[3][0])
                  action_payoffs['player 2'].append(payoff_matrix[3][1])
                if player_2.history[-1] != player_1.history[-1]:
                  action_payoffs['player 1'].append(payoff_matrix[2][0])
                  action_payoffs['player 2'].append(payoff_matrix[2][1])
            player_1.action_payoff(player_2, player_1.history[-1], action_payoffs['player 1'][-1]) #CHECK FOR DVE
            
            # player_2.action_payoff(player_1, player_2.history[-1], action_payoffs['player 2'][-1]) #CHECK FOR DVE

            
            player_1.round += 1
            player_2.round += 1
            # print(player_1)
            # print(action_payoffs)
            # break
            remaining_rounds -= 1

      #   print(ac)
        print(action_payoffs)
        
        
      #   while remaining_rounds > 0:
            
        print(player_1.Q)


   #  print(adversary_agents)
    return blind_agent



training_rounds = 10 # rounds to play per adversary agent types
adversary_agents = []
train_blind_agent(Blind(0), training_rounds)