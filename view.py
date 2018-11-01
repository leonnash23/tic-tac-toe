from abc import ABCMeta, abstractmethod


class GameData:
    def __init__(self, board):
        self.board = board
        self.board_size = len(board)


class View:
    __metaclass__ = ABCMeta

    @abstractmethod
    def paint(self, game: GameData):
        pass


class ConsoleView(View):
    def paint(self, game: GameData):
        for i in range(game.board_size):
            for j in range(game.board_size):
                print(game.board[i][j] + " ", end="")
            print()
