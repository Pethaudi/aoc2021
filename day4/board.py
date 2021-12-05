import numpy as np

class Board:
    def __init__(self, board: list[int]):
        self.board = list(
            map(
                lambda num: [num, False],
                board
            )
        )
        self.stack = []
        self.won = False

    def selectNumber(self, number: int) -> bool:
        for field in self.board:
            if not field[1] and field[0] == number:
                self.stack.append(number)
                field[1] = True
                return self.hasWon()

        return False

    def hasWon(self) -> bool:
        if self.won:
            return True

        npBoard = np.array(list(
            map(
                lambda field: field[1],
                self.board
            )
        )).reshape([5,5])

        for line in np.sum(npBoard, axis=0):
            if line == 5:
                self.won = True
                return True

        for line in np.sum(npBoard, axis=1):
            if line == 5:
                self.won = True
                return True

        return False

    def sumOfUnselected(self) -> int:
        summation = 0
        for field in self.board:
            if not field[1]:
                summation += field[0]
        return summation