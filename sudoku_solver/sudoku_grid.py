import copy
from sudoku_solver.find_possible_values import find_possible_values
from sudoku_solver.updater import update


class Sudoku:
    def __init__(self, grid):
        self.grid = grid

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

    def __str__(self):
        grid_representation = "~~~~~~~~~~~~~~~~~~~~~\n"
        for row_count, row in enumerate(self.grid):
            for count_column, column in enumerate(row):
                grid_representation += str(column) + " "
                if count_column % 3 == 2 and count_column % 9 < 8:
                    grid_representation += "|"
                elif count_column % 9 == 8:
                    grid_representation += "\n"
            if row_count % 3 == 2 and row_count % 9 < 8:
                grid_representation += "---------------------\n"
            elif row_count == 8:
                grid_representation += "~~~~~~~~~~~~~~~~~~~~~\n"
        return grid_representation
