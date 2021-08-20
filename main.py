from solvers import NaiveSolver
from loaders import CsvLoader




if __name__ == '__main__':
    sudoku, solved_sudoku = CsvLoader().load()
    sudoku.print_board()
    naive_solver = NaiveSolver(sudoku=sudoku)
    naive_solver.run()
    print("\n---------------------------------------------------------------------------------\n")
    sudoku.print_board()
    print("\n---------------------------------------------------------------------------------\n")
