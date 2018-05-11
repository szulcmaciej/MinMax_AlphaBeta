from stratego_game import Game
from players.human_player import HumanPlayer
from players.ai_players import MinMaxPlayer, AlphaBetaPlayer, HeuristicAlphaBetaPlayer, AlphaBetaPlayerWithCentr
from players.random_player import RandomPlayer

import math
import numpy as np
import cProfile

def analyse_results(results):
    averages = np.average(np.array(results), axis=0)
    print('Player 1 avg points: ', averages[0])
    print('Player 2 avg points: ', averages[1])

    points = [(result[0], result[1]) for result in results]
    p1_wins = [p1 > p2 for p1, p2 in points]
    p2_wins = [p2 > p1 for p1, p2 in points]
    draws = [p1 == p2 for p1, p2 in points]

    print()
    print('P1 wins: ', np.count_nonzero(p1_wins))
    print('P2 wins: ', np.count_nonzero(p2_wins))
    print('Draws: ', np.count_nonzero(draws))

    print('Avg P1 move time: ', averages[2])
    print('Avg P2 move time: ', averages[3])


p1 = AlphaBetaPlayer('alfabeta1', 4)
p2 = RandomPlayer('alfabeta1')

game = Game(8, p1, p2)

results = []
for i in range(1):
    print('game ', i)
    results.append(game.play())

print()
analyse_results(results)



# cProfile.run('game.play()', sort='tottime')





# results = [(15, 30), (20, 25), (25, 20), (20, 20), (35, 20)]
# analyse_results(results)
# # print(np.array(results))
