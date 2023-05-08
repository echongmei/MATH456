import unittest
from subprocess import run

import sys
# from strategies.blind import Blind
# from strategies.grim_trigger import Grim_trigger
# from strategies.hard_majority import Hard_majority
# from strategies.mean import Mean
# from strategies.nice import Nice
# from strategies.reverse_tit_for_tat import Reverse_tit_for_tat
# from strategies.tit_for_tat import Tit_for_tat
from defined_agents import *
from blind_agent import *
import random
# import neural_network


payoff_matrix = [[2, 2], # Both players cooperate
                [0, 3], # Player 1 cooperates, player 2 defects
                [3, 0], # Player 1 defects, player 2 cooperates
                [1, 1]] # Both players defect

def generate_random_player(player_id: int):
    options = [Grim_Trigger(player_id), Hard_Majority(player_id), Mean(player_id), Nice(player_id), Reverse_Tit_For_Tat(player_id), Tit_For_Tat(player_id)]
    random_player = options[random.randrange(0,len(options))]
    random_player.history = [random.randint(0, 1) for i in range(0, random.randint(1, 20))]
    random_player.round = len(random_player.history)
   #  for i in range(len(random_player.history)):
   #      opponenet_move = random.randint(0,1)
   #      if random_player.history[i] == 0:
   #          if random_player.history[i] == opponenet_move:
   #             if payoff_matrix[0][0] > payoff_matrix[0][1]:
   #                 random_player.update_wins
   #             else:
   #                 random_player.

   
   #  print(range(0,len(options)))
   #  print(random_player.history)
   #  print(vars(random_player))
    return random_player

class Test_Strategy_Initialization(unittest.TestCase):
    
    def test_initialize_blind(self):
        player = Blind(0)
        expected_attributes = {'history': [], 'name': 'Blind', 'round': 0, 'player_id': 0, 'wins': 0, 'losses': 0, 'Q': {}, 'epsilon_count': float(1), 'round_memory': 0, 'guess_memory': {}}
        actual_attributes = vars(player)
        self.assertEqual(actual_attributes, expected_attributes)

    def test_initialize_grim_trigger(self):
        player = Grim_Trigger(0)
        expected_attributes = {'history': [], 'name': 'Grim Trigger', 'round': 0, 'player_id': 0, 'wins': 0, 'losses': 0}
        actual_attributes = vars(player)
        self.assertEqual(actual_attributes, expected_attributes)
    
    def test_initialize_hard_majority(self):
        player = Hard_Majority(0)
        expected_attributes = {'history': [], 'name': 'Hard Majority', 'round': 0, 'player_id': 0, 'wins': 0, 'losses': 0}
        actual_attributes = vars(player)
        self.assertEqual(actual_attributes, expected_attributes)
    
    def test_initialize_mean(self):
        player = Mean(0)
        expected_attributes = {'history': [], 'name': 'Mean', 'round': 0, 'player_id': 0, 'wins': 0, 'losses': 0}
        actual_attributes = vars(player)
        self.assertEqual(actual_attributes, expected_attributes)
    
    def test_initialize_nice(self):
        player = Nice(0)
        expected_attributes = {'history': [], 'name': 'Nice', 'round': 0, 'player_id': 0, 'wins': 0, 'losses': 0}
        actual_attributes = vars(player)
        self.assertEqual(actual_attributes, expected_attributes)
    
    def test_initialize_reverse_tit_for_tat(self):
        player = Reverse_Tit_For_Tat(0)
        expected_attributes = {'history': [], 'name': 'Reverse Tit For Tat', 'round': 0, 'player_id': 0, 'wins': 0, 'losses': 0}
        actual_attributes = vars(player)
        self.assertEqual(actual_attributes, expected_attributes)
    
    def test_initialize_tit_for_tat(self):
        player = Tit_For_Tat(0)
        expected_attributes = {'history': [], 'name': 'Tit For Tat', 'round': 0, 'player_id': 0, 'wins': 0, 'losses': 0}
        actual_attributes = vars(player)
        self.assertEqual(actual_attributes, expected_attributes)
    


# IGNORE THIS FOR NOW -> wait until we have a play game


# class Test_Strategy_Action(unittest.TestCase):
     
   #   def test_strategy_blind(self):
   #       player = Blind(0)
   #       with not self.assertRaises(Test_Strategy_Initialization.test_initialize_blind()):
   #           print('hi')

   #   def test_strategy_grim_trigger(self):
   #       player = Grim_trigger(0)
   #       opponenet = generate_random_player(1) # specify which player you want this to be
   #       temp_opponent = opponenet
   #       print(vars(opponenet))
   #       for i in range(1, len(opponenet.history)):
   #           print(vars(opponenet))
   #           temp_opponent = opponenet
   #           temp_opponent.history = opponenet.history[:i]
   #           temp_opponent.round = i
   #           temp_opponent = temp_opponent
   #          #  print(i, vars(temp_opponent))
   #          #  if player.round == 0 and len(player.history) == 0:
   #          #    expected = 0
   #          #  else:
   #          #       if sum(opponenet.history[:i]) > 0:
   #          #           expected = 1
   #          #       else: 
   #          #           expected = 0
   #          #  if self.assertEqual(expected, player.strategy(temp_opponent)):
   #          #      player.history.append(expected)
   #          #      player.round += 1
   #          #      co
                 
            #  print(opponenet.history[:i])

   #   def test_strategy_hard_majority(self):

   #   def test_strategy_mean(self):
         

   #   def test_strategy_nice(self):
   #       opponenet = generate_random_player()
   #       print(vars(opponenet))
   #       for i in range(0, len(opponenet.history)):
   #           print(opponenet.history[:i])
         
         
   
   #   def test_strategy_reverse_tit_for_tat(self):


   #   def test_strategy_tit_for_tat(self):
          


# class Test_Player_Initialization(unittest.TestCase):
   # figure out how to deal with the random numsber issue



if __name__ == "__main__":
    unittest.main()
   #  Test_Strategy_Action(unittest.TestCase)