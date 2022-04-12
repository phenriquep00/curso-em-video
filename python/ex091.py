# import random
#
# roll = {'player1': random.randint(1, 6),
#         'player2': random.randint(1, 6),
#         'player3': random.randint(1, 6),
#         'player4': random.randint(1, 6)
#         }
# roll_copy = roll.copy()
# order = sorted(roll.values())
# first = str
# for k, v in roll.items():
#     if v == order[-1]:
#         first = k
#         order.pop()
#         del roll[k]
#         break
# second = str
# for k, v in roll.items():
#     if v == order[-1]:
#         second = k
#         order.pop()
#         del roll[k]
#         break
# third = str
# for k, v in roll.items():
#     if v == order[-1]:
#         third = k
#         order.pop()
#         del roll[k]
#         break
# forth = str
# for k, v in roll.items():
#     if v == order[0]:
#         forth = k
#         order.pop()
#         del roll[k]
#         break
#
# print(roll_copy)
# print('¬' * 30)
# print(f'The winner was {first}')
# print(f'Second place goes to {second}')
# print(f'Third place won by {third}')
# print(f'The last one was {forth}')

from random import randint
from time import sleep
from operator import itemgetter
game = {'player1': randint(1, 6),
        'player2': randint(1, 6),
        'player3': randint(1, 6),
        'player4': randint(1, 6)}
ranking = list(sorted(game.items(), key=itemgetter(1), reverse=True))
for k, v in game.items():
    print(f'{k} got {v}')
    sleep(.5)

for i, v in enumerate(ranking):
    print(f'{i+1}° place: {v}')
    sleep(.5)
