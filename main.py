from sudoku import Sudoku
import numpy as np
from solvers import NaiveSolver
from loaders import CsvLoader

board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


if __name__ == '__main__':
    sudoku, solved_sudoku = CsvLoader().load()
    sudoku.print_board()
    naive_solver = NaiveSolver(sudoku=sudoku)
    naive_solver.run()
    print("\n---------------------------------------------------------------------------------\n")
    sudoku.print_board()
    print("\n---------------------------------------------------------------------------------\n")
