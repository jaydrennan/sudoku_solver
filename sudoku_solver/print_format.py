def print_to_terminal(sudoku_grid):
    print(grid_as_string(sudoku_grid))


def grid_as_string(sudoku_grid):
    grid_representation = "~~~~~~~~~~~~~~~~~~~~~\n"
    for row_count, row in enumerate(sudoku_grid):
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
