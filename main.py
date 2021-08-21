from solvers import NaiveSolver, WiseSolver
from loaders import CsvLoader
from copy import deepcopy




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
