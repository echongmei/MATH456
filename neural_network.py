import sys
from strategies.blind import Blind
from strategies.grim_trigger import Grim_trigger
from strategies.hard_majority import Hard_majority
from strategies.mean import Mean
from strategies.nice import Nice
from strategies.tit_for_tat import Tit_for_tat
from strategies.reverse_tit_for_tat import Reverse_tit_for_tat

import random 

# COME BACK AND FIX THIS AFTER YOU ADD GETS TO EACH STRATEGY
def generate_players(N : int) -> dict:
    if N <= 1:
        return '⊥' #error detected
    players = dict()   #players = {i: [class instance(i), attributes for this player]}
    players[0] = Blind(0) # the single blind player -> will always be created
   #  print(players[0].history)
    for i in range(1, N):
        strategy_val = random.randint(1, 6) 
        if strategy_val == 1: # grim trigger
            players[i] = Grim_trigger(i)
        if strategy_val == 2: # hard majority 
            players[i] = Hard_majority(i)
        if strategy_val == 3: # mean 
            players[i] = Mean(i)
        if strategy_val == 4: # nice
            players[i] = Nice(i)
        if strategy_val == 5: # tit-for-tat
            players[i] = Tit_for_tat(i)
        if strategy_val == 6: # reverse tit-for-tat
            players[i] = Reverse_tit_for_tat(i)
   
    return players

def re_eval(round_moves, previous_moves, memory):
    
    pass
def correctness(guess, players, N):
    number_correct = 0
    for i in list(guess.keys()):
        if guess[i] == players[i].name:
            number_correct += 1
    return round(float(number_correct/N), 5)

def check_for_win(player, players, N):
   #  print(N)
    guess = {}
    round_moves = {}
    previous_moves = {}
    for i in list(player.round_memory.keys()):
      round_moves[i] = player.round_memory[i][-1]
      previous_moves[i] = player.round_memory[i][:-1]
      
   #  print(round_moves)
   #  print(previous_moves)
    if player.round == 1:
        for j in list(round_moves.keys()):
            if round_moves[j] == 1:
                options = ['Hard Majority', 'Mean', 'Reverse Tit for Tat']
            elif round_moves[j] == 0:
                options = ['Grim Trigger', 'Nice', 'Reverse Tit for Tat']

            guess[j] = options[random.randint(0, len(options)-1)]
   #  elif player.round > 1:
   #      for k in list(round_moves.keys()):
   #          guess[k] = re_eval(round_moves[k], previous_moves[k], player.guess_memory)
#             print(i)
#             player.round_mem
    percent_correct = correctness(guess, players, N)
    guess['percent'] = percent_correct
    player.guess_memory[player.round] = guess
    print(player.guess_memory)
    if percent_correct == round(float(1.0),5):
        return True
    else:
        return False

   #  players[0].guess_memory[players[0].round] = guess


# player_id: the id of the player that needs to make the move, 
# players: all players in game
def player_move(player, players: dict): 
    N = len(players)
    possible_moves = []
    for id in range(0, N):
        if id != player.player_id:
            possible_moves.append(player.strategy(players[id]))
            if id == 0:
               #  print(players[0].round_memory[players[0].round], player.player_id)
                if player.player_id not in list(players[0].round_memory.keys()):
                    players[0].round_memory[player.player_id] = [possible_moves[-1]]
                  #   print(players[0].round_memory)
                else:
                    players[0].round_memory[player.player_id].append(possible_moves[-1])
    defects = len(list(filter(lambda x: x % 2 != 0, possible_moves)))
    cooperates = len(list(filter(lambda x: x % 2 == 0, possible_moves)))
    if defects > cooperates:
        player.history.append(1)
    elif defects < cooperates:
        player.history.append(0)
    else:
        player.history.append(random.randint(0,1))
    player.round += 1
    print(player.player_id, possible_moves)
    return player
   #  pass 

def play_game(N: int):
    players = generate_players(N)
    print(players)
    win_condition = False
    while not win_condition:
        for i in range(0, N):
            # if i == 0:
               #  players[0].round_memory[players[0].round + 1] = {}
            players[i] = player_move(players[i], players)
        
      #   win_condition = check_for_win(players[0], N)
        if players[0].round >= 1:
            print(check_for_win(players[0], players, N))
            win_condition = True
   #  print(players[0].round_memory)
   #  print(list(players[0].round_memory[1].keys())[1], list(players[0].round_memory[1].values())[1])
    return players
# [print('\t {} \n'.format(vars(players[i]))) for i in range(0, N)]


# print(generate_players(20))


print(play_game(5))
# print(list([0]))
# print(list([0])[:-1])

