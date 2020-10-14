from sudoku_solver.find_possible_values import (
    solve_grid,
    check_row,
    check_column,
    check_quadrant,
    fill_grid,
)


def test_solve(original_sudoku_single, solution_single):
    solution = solve_grid(original_sudoku_single)
    assert solution == solution_single


def test_fill_grid(original_sudoku_single, solution_single):
    fill_grid(original_sudoku_single)
    assert original_sudoku_single[5] == 8


def test_check_row(original_sudoku_single):
    assert check_row(4, 0, original_sudoku_single) is True
    assert check_row(1, 31, original_sudoku_single) is False


def test_check_column(original_sudoku_single):
    assert check_column(5, 0, original_sudoku_single) is True
    assert check_column(8, 28, original_sudoku_single) is False


def test_check_quadrant(original_sudoku_single):
    assert check_quadrant(7, 79, original_sudoku_single) is True
    assert check_quadrant(1, 1, original_sudoku_single) is False
    assert check_quadrant(2, 5, original_sudoku_single) is True

