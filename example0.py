####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####
import random
team_name = 'Mr.Feldman'
strategy_name = 'Dominating Math'
strategy_description = 'Be more aggressive when betrayed.'
    
def move(my_history, their_history, my_score, their_score):
    count=0
    if len(their_history)>2:
        for i in range(3):
            if their_history[i] == 'b':
                count+=1
        if count > 1:
            return random.choice('bbbbc')
        elif count ==1:
            return random.choice('bbc')
        else:
            return random.choice('bc')
    else:
        return 'c'
    