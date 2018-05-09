import time

from players.player import Player
import numpy as np
import math
import stratego_game


class MinMaxPlayer(Player):
    def __init__(self, name, levels=3):
        Player.__init__(self, name)
        self.levels = levels

    def play(self, board):
        move, value = self.minmax(board, eval_function_points, True, self.levels - 1, 0)
        x = move[0]
        y = move[1]
        return x, y

    @staticmethod
    def get_possible_moves(board):
        moves = []

        zeros_true = board == 0
        coords = np.nonzero(zeros_true)

        for i in range(len(coords[0])):
            moves.append((coords[0][i], coords[1][i]))

        return moves

    def minmax(self, board, eval_function, maximize=True, levels_remaining=3, points_for_previous_moves=0):

        possible_moves = self.get_possible_moves(board)
        if len(possible_moves) < levels_remaining + 1:
            levels_remaining = len(possible_moves) - 1

        best_move = None
        if maximize:
            best_value = -math.inf
        else:
            best_value = math.inf

        if levels_remaining == 0:
            if maximize:
                best_value = -math.inf
            else:
                best_value = math.inf
            for move in possible_moves:
                value = eval_function(board.copy(), move, is_player=maximize)
                if maximize:
                    if value > best_value:
                        best_value = value
                        best_move = move
                else:
                    if value < best_value:
                        best_value = value
                        best_move = move
            best_value += points_for_previous_moves

        if levels_remaining > 0:
            if maximize:
                best_value = -math.inf
            else:
                best_value = math.inf
            for move in possible_moves:
                points = eval_function(board.copy(), move, is_player=maximize)
                board_copy = np.copy(board)
                board_copy[move] = 1
                next_move, value = self.minmax(board_copy, eval_function, not maximize, levels_remaining - 1, points_for_previous_moves + points)
                if maximize and value > best_value:
                    best_value = value
                    best_move = move
                if not maximize and value < best_value:
                    best_value = value
                    best_move = move

        # TODO może się przydać przy heurystykach
        # if levels_remaining > 0:
        #     if maximize:
        #         best_value = -math.inf
        #     else:
        #         best_value = math.inf
        #     for move in possible_moves:
        #         value = eval_function(board, move, is_player=maximize)
        #         if maximize and value > best_value:
        #             best_value = value
        #             board_copy = np.copy(board)
        #             board_copy[move] = 1
        #             # go deeper
        #         if not maximize and value < best_value:
        #             best_value = value
        #             board_copy = np.copy(board)
        #             board_copy[move] = 1

        return best_move, best_value


class AlphaBetaPlayer(Player):
    def __init__(self, name, levels=3):
        Player.__init__(self, name)
        self.levels = levels

    def play(self, board):
        move, value = self.alphabeta(board, eval_function_points, True, self.levels - 1, 0)
        x = move[0]
        y = move[1]
        return x, y

    @staticmethod
    def get_possible_moves(board):
        moves = []

        zeros_true = board == 0
        coords = np.nonzero(zeros_true)

        for i in range(len(coords[0])):
            moves.append((coords[0][i], coords[1][i]))

        return moves

    def alphabeta(self, board, eval_function, maximize=True, levels_remaining=3, points_for_previous_moves=0, alpha=-math.inf, beta=math.inf):

        possible_moves = self.get_possible_moves(board)
        if len(possible_moves) < levels_remaining + 1:
            levels_remaining = len(possible_moves) - 1

        best_move = None
        if maximize:
            best_value = -math.inf
        else:
            best_value = math.inf

        if levels_remaining == 0:
            if maximize:
                best_value = -math.inf
            else:
                best_value = math.inf
            for move in possible_moves:
                value = eval_function(board.copy(), move, is_player=maximize)
                if maximize:
                    if value > best_value:
                        best_value = value
                        best_move = move
                        if value > alpha:
                            alpha = value
                else:
                    if value < best_value:
                        best_value = value
                        best_move = move
                        if value < beta:
                            beta = value

                if alpha >= beta:
                    best_value += points_for_previous_moves
                    return best_move, best_value

            best_value += points_for_previous_moves

        if levels_remaining > 0:
            if maximize:
                best_value = -math.inf
            else:
                best_value = math.inf
            for move in possible_moves:
                points = eval_function(board.copy(), move, is_player=maximize)
                board_copy = np.copy(board)
                board_copy[move] = 1
                next_move, value = self.alphabeta(board_copy, eval_function, not maximize, levels_remaining - 1,
                                               points_for_previous_moves + points, alpha, beta)
                if maximize and value > best_value:
                    best_value = value
                    best_move = move
                    if value > alpha:
                        alpha = value
                if not maximize and value < best_value:
                    best_value = value
                    best_move = move
                    if value < beta:
                        beta = value

                if alpha >= beta:
                    return best_move, best_value

        return best_move, best_value


class HeuristicAlphaBetaPlayer(Player):
    def __init__(self, name, levels=3):
        Player.__init__(self, name)
        self.levels = levels

    def play(self, board):
        move, value = self.alphabeta(board, eval_function_points, True, self.levels - 1, 0)
        x = move[0]
        y = move[1]
        return x, y

    @staticmethod
    def get_possible_moves(board):
        moves = []

        zeros_true = board == 0
        coords = np.nonzero(zeros_true)

        for i in range(len(coords[0])):
            moves.append((coords[0][i], coords[1][i]))

        return moves

    def alphabeta(self, board, eval_function, maximize=True, levels_remaining=3, points_for_previous_moves=0,
                  alpha=-math.inf, beta=math.inf):

        possible_moves = self.get_possible_moves(board)
        if len(possible_moves) < levels_remaining + 1:
            levels_remaining = len(possible_moves) - 1

        # heuristics
        # possible_moves.sort(key=lambda move: eval_function_points(board, move, maximize))


        best_move = None
        if maximize:
            best_value = -math.inf
        else:
            best_value = math.inf

        if levels_remaining == 0:
            if maximize:
                best_value = -math.inf
            else:
                best_value = math.inf
            for move in possible_moves:
                value = eval_function(board.copy(), move, is_player=maximize)
                if maximize:
                    if value > best_value:
                        best_value = value
                        best_move = move
                        if value > alpha:
                            alpha = value
                else:
                    if value < best_value:
                        best_value = value
                        best_move = move
                        if value < beta:
                            beta = value

                if alpha >= beta:
                    best_value += points_for_previous_moves
                    return best_move, best_value

            best_value += points_for_previous_moves

        if levels_remaining > 0:
            if maximize:
                best_value = -math.inf
            else:
                best_value = math.inf
            for move in possible_moves:
                points = eval_function(board.copy(), move, is_player=maximize)
                board_copy = np.copy(board)
                board_copy[move] = 1
                next_move, value = self.alphabeta(board_copy, eval_function, not maximize, levels_remaining - 1,
                                                  points_for_previous_moves + points, alpha, beta)
                if maximize and value > best_value:
                    best_value = value
                    best_move = move
                    if value > alpha:
                        alpha = value
                if not maximize and value < best_value:
                    best_value = value
                    best_move = move
                    if value < beta:
                        beta = value

                if alpha >= beta:
                    return best_move, best_value

        return best_move, best_value


def eval_function_points(board, move, is_player):
    if is_player:
        return stratego_game.calculate_points(board, move)
    else:
        return -stratego_game.calculate_points(board, move)
