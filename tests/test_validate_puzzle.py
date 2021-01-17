from sudoku_solver.validate_puzzle import (
    is_valid_sudoku_grid,
    rows_valid,
    columns_valid,
    quadrants_valid,
    correct_range,
)


def test_validate(original_sudoku_single, original_sudoku_single_duplicates):
    assert is_valid_sudoku_grid(original_sudoku_single)
    assert not is_valid_sudoku_grid(original_sudoku_single_duplicates)


def test_rows_valid(original_sudoku_single, original_sudoku_single_duplicates):
    assert rows_valid(original_sudoku_single)
    assert not rows_valid(original_sudoku_single_duplicates)


def test_columns_valid(original_sudoku_single, original_sudoku_single_duplicates):
    assert columns_valid(original_sudoku_single)
    assert not columns_valid(original_sudoku_single_duplicates)


def test_quadrants_valid(original_sudoku_single, original_sudoku_single_duplicates):
    assert quadrants_valid(original_sudoku_single)
    assert not quadrants_valid(original_sudoku_single_duplicates)


def test_correct_range():
    correct = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    incorrect = [0, 1, 10, 3, 4, 5, 6, -1, 8, 9]
    assert correct_range(correct)
    assert not correct_range(incorrect)
