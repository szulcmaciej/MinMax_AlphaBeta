import numpy as np
import time

import sys

from players.human_player import HumanPlayer
from players.random_player import RandomPlayer


class Game:
    def __init__(self, board_size=8, player1=None, player2=None):
        self.BOARD_SIZE = board_size
        self.board = np.zeros((board_size, board_size))
        self.p1 = player1
        self.p2 = player2
        # if p1 == None (p1 is human)

        self.game_over = False
        self.player_one_moving = True
        self.p1_points = 0
        self.p2_points = 0

    def play(self, player_one_staring=True):
        self.board = np.zeros((self.BOARD_SIZE, self.BOARD_SIZE))
        self.game_over = False
        self.player_one_moving = player_one_staring
        self.p1_points = 0
        self.p2_points = 0

        while not self.game_over:
            # one loop for one move of one player
            self.game_loop()
            # print points
            # print('p1 points: ', str(self.p1_points))
            # print('p2 points: ', str(self.p2_points))

        # print('Game over')

        return self.p1_points > self.p2_points

    def move(self, player_id, x, y):
        if self.board[x, y] == 0:
            self.board[x, y] = player_id
            self.add_points(x, y)
            return True
        else:
            # bad move
            return False

    def add_points(self, x, y):
        points = 0
        # row
        if np.all(self.board[x, :]):
            points += self.BOARD_SIZE

        # column
        if np.all(self.board[:, y]):
            points += self.BOARD_SIZE

        # 1st diagonal
        k = y - x
        diagonal = np.diag(self.board, k)
        if np.all(diagonal) and len(diagonal) > 1:
            points += len(diagonal)

        # 2nd diagonal
        new_y = (self.BOARD_SIZE - 1) - y
        k = new_y - x
        diagonal = np.diag(np.fliplr(self.board), k)
        if np.all(diagonal) and len(diagonal) > 1:
            points += len(diagonal)

        if self.player_one_moving:
            self.p1_points += points
        else:
            self.p2_points += points

    def display_board(self):
        print(self.board)

    def game_loop(self):
        x = 0
        y = 0

        player_moved = False

        while not player_moved:
            if self.player_one_moving:
                if self.p1 is not None:
                    # p1 is not human
                    x, y = self.p1.play(self.board)
                else:
                    # p1 is human
                    # x, y = ...
                    pass
                player_moved = self.move(1, x, y)
            else:
                # p2 is moving
                if self.p2 is not None:
                    x, y = self.p2.play(self.board)
                else:
                    pass
                player_moved = self.move(2, x, y)

        self.player_one_moving = not self.player_one_moving

        # check if game over
        self.game_over = np.all(np.all(self.board))



#
# # p1 = HumanPlayer('p1')
# p1 = RandomPlayer('p1')
# p2 = RandomPlayer('p2')
# g = Game(8, p1, p2)
#
# player1_wins = []
# # print(0, end='')
# for i in range(1000):
#     # print('\r', (i+1)/1000, end='')
#     player1_wins.append(g.play())
#     # time.sleep(0.1)
#     sys.stdout.write("\r%d%%" % (i / 1000 * 100))
#     sys.stdout.flush()
#
# print()
# print(sum(player1_wins) / len(player1_wins) * 100, '%')
#


for j in range(2,21):
    # p1 = HumanPlayer('p1')
    p1 = RandomPlayer('p1')
    p2 = RandomPlayer('p2')
    g = Game(j, p1, p2)

    player1_wins = []
    # print(0, end='')
    for i in range(1000):
        player1_wins.append(g.play())

        # sys.stdout.write("\r%d%%" % (i / 10 * 100))
        # sys.stdout.flush()

    print('board: ', j)
    print(sum(player1_wins) / len(player1_wins) * 100, '%')