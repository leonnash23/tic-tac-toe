from view import View, GameData


class Game:
    NO_ONE = "_"

    def __init__(self, view: View):
        self._board_size = 3
        self._board = [[]]
        self._p1_move = True
        self._init_board()
        self._view = view

    def paint(self):
        self._view.paint(GameData(self._board))

    def _init_board(self):
        self._board = ["_"] * self._board_size
        for i in range(self._board_size):
            self._board[i] = ["_"] * self._board_size

    def makeMove(self, n):
        k = 0
        for i in range(self._board_size):
            for j in range(self._board_size):
                if k == int(n) - 1:
                    self._board[i][j] = self.getPlayerMove()
                    self._switchPlayer()
                    return
                else:
                    k += 1

    def _switchPlayer(self):
        self._p1_move = not self._p1_move

    def checkWin(self):
        for i in range(self._board_size):
            h = self._checkH(i)
            if h != self.NO_ONE:
                return h
            v = self._checkV(i)
            if v != self.NO_ONE:
                return v
        d = self._checkD1()
        if d != self.NO_ONE:
            return d
        return self._checkD2()

    def _checkH(self, i):
        temp = self._board[i][0]
        for j in range(self._board_size):
            if self._board[i][j] != temp:
                return self.NO_ONE
        return temp

    def _checkV(self, i):
        temp = self._board[0][i]
        for j in range(self._board_size):
            if self._board[j][i] != temp:
                return self.NO_ONE
        return temp

    def _checkD1(self):
        temp = self._board[0][0]
        for i in range(self._board_size):
            if self._board[i][i] != temp:
                return self.NO_ONE
        return temp

    def _checkD2(self):
        temp = self._board[0][0]
        for i in range(self._board_size - 1, -1, -1):
            if self._board[i][i] != temp:
                return self.NO_ONE
        return temp

    def getPlayerMove(self):
        if self._p1_move:
            return "x"
        else:
            return "o"
