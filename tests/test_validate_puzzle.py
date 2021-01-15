from sudoku_solver.validate_puzzle import (
    validate,
    rows_valid,
    columns_valid,
    quadrants_valid,
)


def test_validate(original_sudoku_single, original_sudoku_single_duplicates):
    assert validate(original_sudoku_single) == True
    assert validate(original_sudoku_single_duplicates) == False


def test_rows_valid(original_sudoku_single, original_sudoku_single_duplicates):
    assert rows_valid(original_sudoku_single) is True
    assert rows_valid(original_sudoku_single_duplicates) is False


def test_columns_valid(original_sudoku_single, original_sudoku_single_duplicates):
    assert columns_valid(original_sudoku_single) is True
    assert columns_valid(original_sudoku_single_duplicates) is False


def test_quadrants_valid(original_sudoku_single, original_sudoku_single_duplicates):
    assert quadrants_valid(original_sudoku_single) is True
    assert quadrants_valid(original_sudoku_single_duplicates) is False
