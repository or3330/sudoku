import numpy as np


class Sudoku:
    def __init__(self, board: np.array):
        self._board = board

    def set_value(self, pos: tuple, value: int):
        self._board[pos] = value

    def get_value(self, pos: tuple):
        return self._board[pos]

    def is_valid(self) -> bool:
        # TODO: need to implement
        raise NotImplemented("is_valid not implemented")
