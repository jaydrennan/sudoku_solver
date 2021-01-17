from sudoku_solver.sudoku_grid import Sudoku


def test_sudoku_grid(original_sudoku_single):

    grid_b = [
        0,
        0,
        7,
        0,
        1,
        0,
        0,
        0,
        8,
        0,
        0,
        0,
        6,
        8,
        0,
        3,
        0,
        2,
        0,
        0,
        0,
        2,
        0,
        4,
        0,
        9,
        7,
        0,
        3,
        2,
        4,
        7,
        9,
        6,
        8,
        5,
        0,
        0,
        0,
        1,
        6,
        0,
        0,
        0,
        4,
        0,
        6,
        0,
        0,
        0,
        0,
        0,
        1,
        9,
        0,
        7,
        0,
        0,
        4,
        0,
        0,
        0,
        0,
        3,
        0,
        9,
        0,
        2,
        0,
        8,
        5,
        1,
        0,
        5,
        6,
        8,
        0,
        1,
        0,
        7,
        0,
    ]

    sudoku_a = Sudoku(original_sudoku_single)
    sudoku_b = Sudoku(grid_b)

    assert sudoku_a != sudoku_b
    assert sudoku_a.solve() != sudoku_b.solve()


def test_solver(original_sudoku_single, solution_single):

    grid = Sudoku(original_sudoku_single)

    solution = grid.solve()
    assert solution == solution_single
    assert len(solution) == 81
    assert 0 not in solution
    assert solution != []


def test_str(original_sudoku_single):
    grid = Sudoku(original_sudoku_single)
    formatted_grid = "~~~~~~~~~~~~~~~~~~~~~\n469|750|300|\n000|230|095|\n500|000|000|\n708|093|006|\n000|000|000|\n200|170|804|\n000|000|002|\n970|021|000|\n001|046|973|\n"

    assert str(grid) == formatted_grid
