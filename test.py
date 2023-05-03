import unittest
from subprocess import run

import sys
from strategies.blind import Blind
from strategies.grim_trigger import Grim_trigger
from strategies.hard_majority import Hard_majority
from strategies.mean import Mean
from strategies.nice import Nice
from strategies.reverse_tit_for_tat import Reverse_tit_for_tat
from strategies.tit_for_tat import Tit_for_tat

import random
# import neural_network

def generate_random_player(player_id: int):
    options = [Grim_trigger(player_id), Hard_majority(player_id), Mean(player_id), Nice(player_id), Reverse_tit_for_tat(player_id), Tit_for_tat(player_id)]
    random_player = options[random.randrange(0,len(options))]
    random_player.history = [random.randint(0, 1) for i in range(0, random.randint(1, 20))]
    random_player.round = len(random_player.history)
   #  print(range(0,len(options)))
   #  print(random_player.history)
   #  print(vars(random_player))
    return random_player

class Test_Strategy_Initialization(unittest.TestCase):
    
    def test_initialize_blind(self):
        player = Blind(0)
        expected_attributes = {'history': [], 'name': 'Blind', 'round': 0, 'player_id': 0, 'total_score': 0, 'memory': {}}
        actual_attributes = vars(player)
        self.assertEqual(actual_attributes, expected_attributes)

    def test_initialize_grim_trigger(self):
        player = Grim_trigger(0)
        expected_attributes = {'history': [], 'name': 'Grim Trigger', 'round': 0, 'player_id': 0, 'total_score': 0}
        actual_attributes = vars(player)
        self.assertEqual(actual_attributes, expected_attributes)
    
    def test_initialize_hard_majority(self):
        player = Hard_majority(0)
        expected_attributes = {'history': [], 'name': 'Hard Majority', 'round': 0, 'player_id': 0, 'total_score': 0}
        actual_attributes = vars(player)
        self.assertEqual(actual_attributes, expected_attributes)
    
    def test_initialize_mean(self):
        player = Mean(0)
        expected_attributes = {'history': [], 'name': 'Mean', 'round': 0, 'player_id': 0, 'total_score': 0}
        actual_attributes = vars(player)
        self.assertEqual(actual_attributes, expected_attributes)
    
    def test_initialize_nice(self):
        player = Nice(0)
        expected_attributes = {'history': [], 'name': 'Nice', 'round': 0, 'player_id': 0, 'total_score': 0}
        actual_attributes = vars(player)
        self.assertEqual(actual_attributes, expected_attributes)
    
    def test_initialize_reverse_tit_for_tat(self):
        player = Reverse_tit_for_tat(0)
        expected_attributes = {'history': [], 'name': 'Reverse Tit for Tat', 'round': 0, 'player_id': 0, 'total_score': 0}
        actual_attributes = vars(player)
        self.assertEqual(actual_attributes, expected_attributes)
    
    def test_initialize_tit_for_tat(self):
        player = Tit_for_tat(0)
        expected_attributes = {'history': [], 'name': 'Tit for Tat', 'round': 0, 'player_id': 0, 'total_score': 0}
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