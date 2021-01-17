def is_valid_sudoku_grid(grid):
    return (
        rows_valid(grid)
        and columns_valid(grid)
        and quadrants_valid(grid)
        and correct_range(grid)
    )


def rows_valid(grid):
    for start in range(0, 83, 9):
        end = start + 9
        for i in range(1, 10):
            row = grid[start:end]
            count = row.count(i)
            if count > 1:
                return False
    return True


def columns_valid(grid):
    for column_starting_index in range(9):
        column = []
        for _ in range(9):
            column.append(grid[column_starting_index])
            column_starting_index += 9
        for i in range(1, 10):
            if column.count(i) > 1:
                return False
    return True


def quadrants_valid(grid):
    starting_points = [0, 3, 6, 27, 30, 33, 54, 57, 60]
    for starting_point in starting_points:
        quadrant = (
            grid[starting_point : starting_point + 3]
            + grid[starting_point + 9 : starting_point + 12]
            + grid[starting_point + 18 : starting_point + 21]
        )

        for i in range(1, 10):
            if quadrant.count(i) > 1:
                return False
    return True


def correct_range(grid):
    for val in grid:
        if val < 0 or val > 9:
            return False
    return True
