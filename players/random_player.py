from players.player import Player
import numpy as np

class RandomPlayer(Player):
    def __init__(self, name):
        Player.__init__(self, name)

    def play(self, board):
        [x, y] = np.random.random_integers(0, np.shape(board)[0] - 1, 2)

        while board[x, y] > 0:
            [x, y] = np.random.random_integers(0, np.shape(board)[0] - 1, 2)

        return x, y