from sudoku_solver.find_possible_values import solve_grid


class Sudoku:
    def __init__(self, grid):
        self.grid = grid

    def solve(self):
        return solve_grid(self.grid)

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
