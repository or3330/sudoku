from .base_solver import BaseSolver
from sudoku import Sudoku
from collections import defaultdict


class WiseSolver(BaseSolver):
    def __init__(self, sudoku: Sudoku):
        super().__init__(sudoku=sudoku)
        self._possible_values = defaultdict(lambda: [i + 1 for i in range(len(self._sudoku))])
        self._current_pos = (0, 0)

    def run(self) -> bool:
        """
        solves the sudoko board using wise algorithm
        """
        empty_pos = self._find_next_empty_pos()
        while empty_pos:
            if not self._update_possible_values(empty_pos):
                return False
            empty_pos = self._find_next_empty_pos()

        return True

    def _update_possible_values(self, pos: tuple) -> bool:
        """
        Updates possible values for the position, if only one sets the value
        :param pos:
        :return bool - if update succeeded or not
        """
        possible_values = [i for i in self._possible_values[pos] if self._sudoku.is_valid(pos=pos, value=i)]
        if len(possible_values) == 0:
            return False

        if len(possible_values) == 1:
            self._sudoku.set_value(pos=pos, value=possible_values[0])
            del self._possible_values[pos]
        else:
            self._possible_values[pos] = possible_values
        return True

    def _get_next_pos(self):
        sudoku_len = len(self._sudoku)
        x, y = self._current_pos
        y = (y + 1) % sudoku_len
        if y == 0:
            x = (x + 1) % sudoku_len
        self._current_pos = (x, y)
        return self._current_pos

    def _find_next_empty_pos(self):
        """
        finds the next empty position in the matrix and returns it if exist
        """
        old_pos = self._current_pos
        pos = self._get_next_pos()
        while self._sudoku.get_value(pos) > 0:
            if pos == old_pos:
                return None
            pos = self._get_next_pos()
        return pos
