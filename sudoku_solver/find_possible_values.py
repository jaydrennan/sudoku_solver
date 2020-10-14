import math


def solve_grid(sudoku_puzzle):
    """returns 3d array, the third array listing all possible values for given position"""
    # creates empty 9x9 grid that will store a list of possible answers for each position.

    while 0 in sudoku_puzzle:
        sudoku_puzzle = fill_grid(sudoku_puzzle)
    # solution = []
    # start = 0
    #
    # for x in range(9):
    #     solution.append(sudoku_puzzle[start : start + 9])
    #     start += 9
    return sudoku_puzzle


def fill_grid(all_values):
    for i, val in enumerate(all_values):
        if val == 0:
            possible_vals = set()
            for poss_val in range(1, 10):
                if (
                    check_row(poss_val, i, all_values) == False
                    and check_column(poss_val, i, all_values) == False
                    and check_quadrant(poss_val, i, all_values) == False
                ):
                    possible_vals.add(poss_val)
            if len(possible_vals) == 1:
                all_values[i] = possible_vals.pop()
    return all_values


def check_column(poss_val, i, vals):
    col_index = i % 9
    for _ in range(9):
        if vals[col_index] == poss_val:
            return True
        col_index += 9
    return False


def check_row(poss_val, i, vals):
    end = i + (9 - (i % 9))
    start = i - (i % 9)
    if poss_val in vals[start:end]:
        return True
    return False


def check_quadrant(x, i, vals):
    horizontal_adjustment = i % 3
    vertical_adjustment = i - (i % 27) + (i % 9)
    start = vertical_adjustment - horizontal_adjustment
    for _ in range(3):
        if x in vals[start : start + 3]:
            return True
        start += 9
    return False
