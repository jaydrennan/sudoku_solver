import math


def find_possible_values_original(sudoku_puzzle):
    """returns 3d array, the third array listing all possible values for given position"""
    # creates empty 9x9 grid that will store a list of possible answers for each position.
    possible_solutions = [[0 for _ in range(9)] for _ in range(9)]
    for y_coordinate, row in enumerate(sudoku_puzzle):
        for x_coordinate, x_value in enumerate(row):
            position_possibilities = []
            if sudoku_puzzle[y_coordinate][x_coordinate] == 0:
                for i in range(1, 10):
                    if is_valid(i, row, x_coordinate, y_coordinate, sudoku_puzzle):
                        position_possibilities.append(i)
            possible_solutions[y_coordinate][x_coordinate] = position_possibilities
    return possible_solutions


def is_valid(i, row, x_coordinate, y_coordinate, sudoku_puzzle):
    return (
        check_row(i, row)
        and check_column(i, x_coordinate, sudoku_puzzle)
        and check_box(x_coordinate, y_coordinate, i, sudoku_puzzle)
    )


def check_row(i, row):
    return i not in row


def check_column(i, x_coordinate, sudoku_puzzle):
    for row in sudoku_puzzle:
        if i == row[x_coordinate]:
            return False
    return True


def check_box(x, y, i, sudoku_puzzle):

    x_coordinate = math.floor(x / 3) * 3
    y_coordinate = math.floor(y / 3) * 3

    return check_area(x_coordinate, y_coordinate, i, sudoku_puzzle)


def check_area(x, y, i, sudoku_puzzle):
    """checks to see if i already exists in the same quadrant"""

    for col in range(x, x + 3):
        for row in range(y, y + 3):
            if sudoku_puzzle[row][col] == i:
                return False
    return True