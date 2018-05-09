import time

from players.player import Player
import numpy as np
import math
import stratego_game


class MinMaxPlayer(Player):
    def __init__(self, name):
        Player.__init__(self, name)

    def play(self, board):


        return x, y

    @staticmethod
    def get_possible_moves(board):
        moves = []

        zeros_true = board == 0
        coords = np.nonzero(zeros_true)

        for i in range(len(coords[0])):
            moves.append((coords[0][i], coords[1][i]))

        return moves

    def minmax(self, board, eval_function, maximize=True, levels_remaining=100, alpha=-math.inf, beta=math.inf):

        possible_moves = self.get_possible_moves(board)
        move_to_return = possible_moves[0]
        return_fun_value = -math.inf
        for move in possible_moves:
            if maximize:
                value = eval_function(board, move)
                if value > return_fun_value:
                    return_fun_value = value
                    board[move] = 1
            else:
                

        if levels_remaining > 0:


        if levels_remaining == 0:
            # leaf



        return move, value

    def alphabeta(self, board, maximize=True, levels_remaining=100, alpha=-math.inf, beta=math.inf):
        pass


def eval_function_points(board, move):
    return stratego_game.calculate_points(board, move)