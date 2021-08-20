from solvers import NaiveSolver, WiseSolver
from loaders import CsvLoader
from copy import deepcopy

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
    saved_sudoku = deepcopy(sudoku)
    sudoku.print_board()
    naive_solver = NaiveSolver(sudoku=sudoku)
    naive_time = naive_solver.run_with_time_analysis()
    print("\n---------------------------------------------------------------------------------\n")
    sudoku.print_board()
    print("\n---------------------------------------------------------------------------------\n")

    sudoku = saved_sudoku
    sudoku.print_board()
    wise_solver = WiseSolver(sudoku=sudoku)
    wise_time = wise_solver.run_with_time_analysis()
    print("\n---------------------------------------------------------------------------------\n")
    sudoku.print_board()
    print("\n---------------------------------------------------------------------------------\n")

    print(f'Wise solver time: {wise_time} seconds')
    print(f'Naive solver time: {naive_time} seconds')

