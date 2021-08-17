from .base_solver import BaseSolver
from sudoku import Sudoku


class NaiveSolver(BaseSolver):
    def __init__(self, sudoku: Sudoku):
        super().__init__(sudoku=sudoku)
