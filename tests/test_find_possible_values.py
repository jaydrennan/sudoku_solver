from sudoku_solver.find_possible_values import (
    find_possible_values,
    check_row,
    check_column,
    check_area,
)

original_sudoku = [
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


def test_find_possible_values():
    possible_values = find_possible_values(original_sudoku)
    for row in possible_values:
        for value in row:
            if isinstance(value, list):
                for possible_answer in value:
                    assert possible_answer < 10
                    assert possible_answer > 0
                assert len(value) == len(set(value))


def test_check_row():
    row = [1, 0, 3, 0, 4, 5, 0, 0, 0]
    assert check_row(7, row) is True
    assert check_row(1, row) is False
    assert len(row) == 9


def test_check_column():
    assert check_column(5, 3, original_sudoku) is True
    assert check_column(5, 0, original_sudoku) is False


def test_check_area():
    assert check_area(0, 0, 1, original_sudoku) is True
    assert check_area(0, 0, 6, original_sudoku) is False
