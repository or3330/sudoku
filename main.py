import csv
import random

from sudoku import Sudoku
import numpy as np
from solvers import NaiveSolver
import random
from numpy import genfromtxt

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



def load_board():
    csv_file = np.genfromtxt('input/sudoku.csv', delimiter=",")
    first_col = csv_file[:, 0]
    second_col = csv_file[:, 1]
    random_row = random.randint(0, 10000)
    single_board = np.array(first_col[random_row])

    print("\n---------------------------------------------------------------------------------\n")
    print(first_col)
    print("\n---------------------------------------------------------------------------------\n")
    print(second_col)
    print("\n---------------------------------------------------------------------------------\n")
    print(random_row)
    print("\n---------------------------------------------------------------------------------\n")


    return single_board


def main():
    sudoku = Sudoku(board=np.array(board))
    sudoku.print_board()
    naive_solver = NaiveSolver(sudoku=sudoku)
    naive_solver.run()
    print("\n---------------------------------------------------------------------------------\n")
    sudoku.print_board()
    print("\n---------------------------------------------------------------------------------\n")
    load_board()



main()
