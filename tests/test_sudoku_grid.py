from sudoku_solver.sudoku_grid import Sudoku


def test_sudoku_grid():

    grid_a = [
        [4, 6, 9, 7, 5, 0, 3, 0, 0],
        [0, 0, 0, 2, 3, 0, 0, 9, 5],
        [5, 0, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 8, 0, 9, 3, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 1, 7, 0, 8, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
        [9, 7, 0, 0, 2, 1, 0, 0, 0],
        [0, 0, 1, 0, 4, 6, 9, 7, 3],
    ]

    grid_b = [
        [6, 4, 0, 7, 5, 0, 3, 0, 0],
        [0, 0, 0, 2, 3, 0, 0, 9, 5],
        [5, 0, 9, 0, 0, 0, 0, 0, 0],
        [7, 0, 8, 0, 9, 3, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 1, 7, 0, 8, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 2],
        [9, 7, 0, 0, 2, 1, 0, 0, 0],
        [0, 0, 1, 0, 4, 6, 9, 7, 3],
    ]

    sudoku_a = Sudoku(grid_a)
    sudoku_b = Sudoku(grid_b)

    assert sudoku_a != sudoku_b
    assert sudoku_a.solve() != sudoku_b.solve()


def test_solver(original_sudoku, solved_sudoku):

    grid = Sudoku(original_sudoku)

    solution = grid.solve()
    assert solution == solved_sudoku
    assert solution != []
    for row in solution:
        assert len(row) == len(set(row))
        assert len(row) == 9
        assert 0 not in row
