from sudoku_solver.find_possible_values import solve_grid
from sudoku_solver.validate_puzzle import validate


class Sudoku:
    def __init__(self, grid):
        self.grid = grid

    def is_valid(self):
        return validate(self.grid)

    def solve(self):
        return solve_grid(self.grid)

    def __str__(self):
        grid_representation = "~~~~~~~~~~~~~~~~~~~~~\n"
        for i, val in enumerate(self.grid):
            grid_representation += str(val)
            if i % 3 == 2:
                grid_representation += "|"
            if i % 9 == 8:
                grid_representation += "\n"
        return grid_representation
