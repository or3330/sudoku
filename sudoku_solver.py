from typing import Optional

# define a matrix of 9*9 with which will represent our Sudoku Board
# in Constraint satisfaction Problem POV:
# VARIABLES = each 0 represents a empty space on the sudoku board
# Constrains = each number that !=0 is a given Constrains - according to the rules of the game

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


def solve(matrix: list) -> bool:
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


# printing Function prints the Sudoku board to the terminal
def print_matrix(matrix: list):
    for i in range(len(matrix)):

        # after every 3 rows it will draw horizontal line
        if (i % 3 == 0) and i != 0:
            print("- - - - - - - - - - - - - - - -")

        for j in range(len(matrix[0])):

            # after every 3 Columns it will draw a diagonal line
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(matrix[i][j])
            else:
                print(str(matrix[i][j]) + " ", end="")


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


def valid(matrix: list, num: int, pos: tuple):
    """
    this function checks the Constrains on every number that we try in the way to the solution
    :param matrix:
    :param num:
    :param pos:
    :return:
    """

    for i in range(len(matrix[0])):
        if matrix[pos[0]][i] == num and pos[1] != i:
            return False

    # check COL
    for i in range(len(matrix)):
        if matrix[i][pos[1]] == num and pos[0] != i:
            return False

    # check BOX (the 3*3 must contain all integer's from 1-9 no duplicates)
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if matrix[i][j] == num and (i, j) != pos:
                return False

    return True


# main
def main():
    print_matrix(board)
    solve(board)
    print("\n---------------------------------------------------------------------------------\n")
    print_matrix(board)


main()
