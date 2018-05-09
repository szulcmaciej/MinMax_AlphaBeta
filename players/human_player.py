from players.player import Player


class HumanPlayer(Player):
    def __init__(self, name):
        Player.__init__(self, name)

    def play(self, board):
        print()
        print(self.name)
        print(board)
        x = int(input('X: '))
        y = int(input('Y: '))

        while (x < 0 or x > board.shape[0] - 1) or (y < 0 or y > board.shape[0]):
            print()
            print('Bad input!')
            print(self.name)
            print(board)
            x = int(input('X: '))
            y = int(input('Y: '))

        return x, y