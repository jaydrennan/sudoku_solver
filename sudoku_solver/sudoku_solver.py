import copy

from sudoku_solver.find_possible_values import find_possible_values
from sudoku_solver.updater import update


def get_solution(original_sudoku):

    sudoku_position_possibilities = find_possible_values(original_sudoku)

    updated_sudoku = update(sudoku_position_possibilities, original_sudoku)
    iterations = [updated_sudoku]
    prev = 0

    while prev != updated_sudoku:
        prev = copy.deepcopy(updated_sudoku)
        sudoku_position_possibilities = find_possible_values(updated_sudoku)
        updated_sudoku = update(sudoku_position_possibilities, updated_sudoku)
        iterations.append(updated_sudoku)

    return iterations[0]
