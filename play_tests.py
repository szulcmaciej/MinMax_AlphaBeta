from stratego_game import Game
from players.human_player import HumanPlayer
from players.ai_players import MinMaxPlayer, AlphaBetaPlayer, HeuristicAlphaBetaPlayer
from players.random_player import RandomPlayer

import cProfile


# p1 = MinMaxPlayer('MinMax', 3)
# p2 = MinMaxPlayer('Human', 3)

# p1 = AlphaBetaPlayer('p1', 3)
# p2 = AlphaBetaPlayer('p2', 3)

p1 = HeuristicAlphaBetaPlayer('alfabeta1', 3)
p2 = HeuristicAlphaBetaPlayer('alphabeta2', 3)

game = Game(5, p1, p2)
# game.play()

cProfile.run('game.play()', sort='tottime')
