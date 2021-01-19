from sudoku_solver.validate_puzzle import is_valid_sudoku_grid


class InvalidSudokuValueError(Exception):
    """Raised if there is a value outside of 0-9 or when there are repeat values in a row, column, or quadrant"""


def solve_grid(sudoku_puzzle):
    """
    Receives unsolved Sudoku puzzle in the form of a single list. Returns a completed list.

    Expects a list with all given values and 0's in place of unknown values.
    The list parameter and return list are the sudoku puzzle's rows combined into a single list,
    from top to bottom.
    """

    empty_count = sudoku_puzzle.count(0)

    if not is_valid_sudoku_grid(sudoku_puzzle):
        raise InvalidSudokuValueError(
            "Either repeat values in row, column, or quadrant. Or value out of range."
        )

    while 0 in sudoku_puzzle:
        sudoku_puzzle = fill_grid(sudoku_puzzle)
        if empty_count == sudoku_puzzle.count(0):
            return sudoku_puzzle
        empty_count = sudoku_puzzle.count(0)
    return sudoku_puzzle


def fill_grid(all_values):
    needed_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    starting_points = [0, 3, 6, 27, 30, 33, 54, 57, 60]
    for starting_point in starting_points:
        quadrant = (
            all_values[starting_point : starting_point + 3]
            + all_values[starting_point + 9 : starting_point + 12]
            + all_values[starting_point + 18 : starting_point + 21]
        )

        if 0 in quadrant:
            empty_indexes = []
            for i, val in enumerate(quadrant):
                if val == 0:
                    empty_indexes.append(i)
            missing_values = list(set(needed_values) - set(quadrant))
            index_possible_solutions = {}
            for i in empty_indexes:
                possible_values = []
                row_start = int(
                    starting_point - (starting_point % 9) + (((i - (i % 3)) / 3) * 9)
                )
                col_start = starting_point + (i % 3) - ((starting_point // 9) * 9)
                for val in missing_values:
                    if (
                        row(row_start, val, all_values) is False
                        and column(col_start, val, all_values) is False
                    ):
                        possible_values.append(val)
                if len(possible_values) == 1:
                    quadrant[i] = possible_values[0]
                    missing_values.remove(possible_values[0])
                else:
                    index_possible_solutions[i] = possible_values

            all_possible_values = compile_all_possible_values(index_possible_solutions)
            for val in missing_values:
                if all_possible_values.count(val) == 1:
                    for key in index_possible_solutions:
                        if val in index_possible_solutions[key]:
                            quadrant[key] = val

            all_values[starting_point : starting_point + 3] = quadrant[0:3]
            all_values[starting_point + 9 : starting_point + 12] = quadrant[3:6]
            all_values[starting_point + 18 : starting_point + 21] = quadrant[6:10]
    return all_values


def compile_all_possible_values(index_possible_solutions):
    all_possible_values = []
    for vals in index_possible_solutions.values():
        all_possible_values += vals
    return all_possible_values


def row(row_start, val, all_values):
    start = row_start
    end = start + 9
    if val in all_values[start:end]:
        return True
    return False


def column(col_start, val, all_values):
    for _ in range(9):
        if all_values[col_start] == val:
            return True
        col_start += 9
    return False
