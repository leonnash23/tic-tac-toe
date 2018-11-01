from controller import Game
from view import ConsoleView

c = Game(ConsoleView())

while True:
    c.paint()
    m = input()
    c.makeMove(m)
    win = c.checkWin()
    if c.checkWin() != c.NO_ONE:
        print("WINNER:" + win)
        break
