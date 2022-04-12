import random
from time import sleep
games = []
prov_list = []
number_of_games = int(input("What's the number of games to be generated? "))

for i in range(0, number_of_games):
    prov_list.append(sorted(random.sample(range(1, 60), 6)))
    games.append(prov_list[:])
    prov_list.clear()

for i in range(0, number_of_games):
    print(f'GAME {i+1}: {games[i]}')
    sleep(1)
print('Good luck!')
