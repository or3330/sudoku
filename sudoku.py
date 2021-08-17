import numpy as np


class Sudoku:
    def __init__(self, board: np.array):
        self._board = board

    def set_value(self, pos: tuple, value: int) -> bool:
        if not self._is_valid(pos=pos, value=value):
            return False
        self._board[pos] = value
        return True

    def get_value(self, pos: tuple) -> int:
        return self._board[pos]

    def _is_valid(self, pos: tuple, value: int) -> bool:
        """
        this function checks the Constrains on every number that we try in the way to the solution
        :param self._board:
        :param value:
        :param pos:
        :return:
        """
        for i in range(len(self._board[0])):
            if self._board[pos[0]][i] == value and pos[1] != i:
                return False

        # check COL
        for i in range(len(self._board)):
            if self._board[i][pos[1]] == value and pos[0] != i:
                return False

        # check BOX (the 3*3 must contain all integer's from 1-9 no duplicates)
        box_x = pos[1] // 3
        box_y = pos[0] // 3

        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if self._board[i][j] == value and (i, j) != pos:
                    return False

        return True
