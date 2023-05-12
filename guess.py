from collections import Counter


#will guess the strategy by looking at its own history (blind) and player_2's 
def guess(player1, player2):
    guess = []
        
    p2history = player2
    p1history = player1
    
    #Player2 played all cooperates 
    if sum(p2history) == 0:
        #could be grim trigger, nice, or tit for tat
        if sum(p1history) == 0 or (sum(p1history) == 1 and p1history[-1] == 1):
            #for Grim Trigger and Tit_for_tat to play all 0s, player1 must have played all 0s OR all 0s except the last round
            guess.append('Grim_trigger')
            guess.append('Tit_for_tat')
        guess.append('Nice')
     
    #Player 2 played all defects
    elif sum(p2history) == len(p2history):
        #could be mean, reverse tit for tat, or hard majority
        if sum(p1history) == 0 or (sum(p1history) == 1 and p1history[-1] == 1):
            #for Reverse_tit_for tat to play all 1s, player1 must have played all 0s OR all 0s except the last round
            guess.append('Reverse_tit_for_tat')
        else:
            #for Hard_majority to play all 1s, player1 must have more 1s than (or equal to) 0s for each round i
            flag = True
            for i in range(len(p1history)):
                c1 = Counter(p1history[:i])
                if c1[1] < c1[0]:
                    flag = False
            if flag == True:
                guess.append("Hard_majority")
        guess.append("Mean")
     
    #Player 2 played an arbituary number of 0s and 1s
    else:   
        if p2history[0] == 0:
            #could be tit for tat, or grim trigger (nice is already handled above)
            grim_trigger_flag = True
            tit_for_tat_flag = True
            for i in range(1, len(p2history)):
                if p2history[i] == 1 and sum(p1history[:i-1]) > 0:
                    grim_trigger_flag = False
                if p2history[i] != p1history[i-1]:
                    tit_for_tat_flag = False
            if tit_for_tat_flag == True:
                guess.append("Tit_for_tat")
            if grim_trigger_flag == True:
                guess.append("Grim_trigger")
        else:
            #could be reverse tit for tat, or hard majority (mean is already handled above)
            hard_majority_flag = True
            reverse_tit_for_tat_flag = True
            for i in range(1, len(p2history)):
                c = Counter(p1history[:i-1])
                if (p2history[i] != 1 and c[1] >= c[0]) or (p2history[i] != 0 and c[1] < c[0]):
                    hard_majority_flag = False
                if p2history[i] == p1history[i-1]:
                    reverse_tit_for_tat_flag = False
            if reverse_tit_for_tat_flag == True:
                guess.append("Reverse_tit_for_tat")
            if hard_majority_flag == True:
                guess.append("Hard_majority")
    return guess
