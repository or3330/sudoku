from .base_solver import BaseSolver
from sudoku import Sudoku
from typing import Optional


class NaiveSolver(BaseSolver):
    def __init__(self, sudoku: Sudoku):
        super().__init__(sudoku=sudoku)

    def run(self) -> bool:
        """
        solves the suduko board using backtracking
        """
        empty_pos = self._find_next_empty_pos()
        if not empty_pos:
            return True

        # adding new element and checking if its valid
        for i in range(1, 10):
            if not self._sudoku.set_value(pos=empty_pos, value=i):
                continue

            # recursive call for solve with the new board
            if self.run():
                return True

        self._sudoku.set_value(pos=empty_pos, value=0)
        return False

    def _find_next_empty_pos(self) -> Optional[tuple]:
        """
        finds the next empty position in the matrix and returns it if exist
        """
        sudoku_len = len(self._sudoku)
        for i in range(sudoku_len):
            for j in range(sudoku_len):
                if self._sudoku.get_value((i, j)) == 0:
                    return i, j  # returning the row and col from this function
        return None
