from .base_solver import BaseSolver
from sudoku import Sudoku


class NaiveSolver(BaseSolver):
    def __init__(self, sudoku: Sudoku):
        super().__init__(sudoku=sudoku)

    def run(self):
        """
        solves the suduko board using backtracking
        :param matrix: sudoku board
        :return: bool
        """
        # returns the next empty block by its row and col as (i,j)
        empty_pos = find_empty_block(matrix=matrix)

        # if we don't have a next empty its means we have a solution for the sudoku board
        # recursion ending condition
        if not empty_pos:
            return True
        else:
            row, col = empty_pos

        # adding new element and checking if its valid
        for i in range(1, 10):
            if valid(matrix, i, (row, col)):
                matrix[row][col] = i
            else:
                continue

            # recursive call for solve with the new board
            if solve(matrix):
                return True

        matrix[row][col] = 0
        return False

    def find_empty_block(matrix: list) -> Optional[tuple]:
        """
        finds the next empty position in the matrix and returns it if exist
        :param matrix:
        :return:
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    return i, j  # returning the row and col from this function
        return None