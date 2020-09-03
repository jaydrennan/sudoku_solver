def update(possible_values, known_sudoku_values):

    new_coordinates = []
    for y, row in enumerate(possible_values):
        for x, column in enumerate(row):

            if (
                isinstance(possible_values[y][x], list)
                and len(possible_values[y][x]) == 1
            ):
                known_sudoku_values[y][x] = possible_values[y][x][0]
                new_coordinates.append([y, x])
    return known_sudoku_values
