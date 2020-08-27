import copy
from sudoku_solver.print_format import grid_as_string
from sudoku_solver.find_possible_values import find_possible_values
from sudoku_solver.updater import update

class Sudoku:

    def __init__(self, grid):
        self.grid = grid


    def empty_grid(self):
        self.grid = [[0 for j in range(9)] for k in range(9)]
        return self.grid

    def solve(self):
        sudoku_position_possibilities = find_possible_values(self.grid)

        updated_sudoku = update(sudoku_position_possibilities, self.grid)
        iterations = [updated_sudoku]
        prev = 0

        while prev != updated_sudoku:
            prev = copy.deepcopy(updated_sudoku)
            sudoku_position_possibilities = find_possible_values(updated_sudoku)
            updated_sudoku = update(sudoku_position_possibilities, updated_sudoku)
            iterations.append(updated_sudoku)

        return iterations[0]

    def display_to_terminal(self):
        grid_as_string(self.grid)