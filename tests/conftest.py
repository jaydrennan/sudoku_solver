import pytest


@pytest.fixture()
def original_sudoku():
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
    return original_sudoku


@pytest.fixture()
def solved_sudoku():
    solution = [
        [4, 6, 9, 7, 5, 8, 3, 2, 1],
        [1, 8, 7, 2, 3, 4, 6, 9, 5],
        [5, 3, 2, 6, 1, 9, 4, 8, 7],
        [7, 1, 8, 4, 9, 3, 2, 5, 6],
        [3, 4, 5, 8, 6, 2, 7, 1, 9],
        [2, 9, 6, 1, 7, 5, 8, 3, 4],
        [6, 5, 3, 9, 8, 7, 1, 4, 2],
        [9, 7, 4, 3, 2, 1, 5, 6, 8],
        [8, 2, 1, 5, 4, 6, 9, 7, 3],
    ]
    return solution


@pytest.fixture()
def original_sudoku_single():
    original_sudoku = [
        4,
        6,
        9,
        7,
        5,
        0,
        3,
        0,
        0,
        0,
        0,
        0,
        2,
        3,
        0,
        0,
        9,
        5,
        5,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        7,
        0,
        8,
        0,
        9,
        3,
        0,
        0,
        6,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        2,
        0,
        0,
        1,
        7,
        0,
        8,
        0,
        4,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        2,
        9,
        7,
        0,
        0,
        2,
        1,
        0,
        0,
        0,
        0,
        0,
        1,
        0,
        4,
        6,
        9,
        7,
        3,
    ]
    return original_sudoku


@pytest.fixture()
def original_sudoku_single_duplicates():
    original_sudoku_single_duplicates = [
        4,
        6,
        9,
        7,
        5,
        6,
        3,
        0,
        0,
        4,
        6,
        0,
        2,
        3,
        0,
        0,
        9,
        5,
        5,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        7,
        0,
        8,
        0,
        9,
        3,
        0,
        0,
        6,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        2,
        0,
        0,
        1,
        7,
        0,
        8,
        0,
        4,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        2,
        9,
        7,
        0,
        0,
        2,
        1,
        0,
        0,
        0,
        0,
        0,
        1,
        0,
        4,
        6,
        9,
        7,
        3,
    ]
    return original_sudoku_single_duplicates


@pytest.fixture()
def solution_single():
    solution = [
        4,
        6,
        9,
        7,
        5,
        8,
        3,
        2,
        1,
        1,
        8,
        7,
        2,
        3,
        4,
        6,
        9,
        5,
        5,
        3,
        2,
        6,
        1,
        9,
        4,
        8,
        7,
        7,
        1,
        8,
        4,
        9,
        3,
        2,
        5,
        6,
        3,
        4,
        5,
        8,
        6,
        2,
        7,
        1,
        9,
        2,
        9,
        6,
        1,
        7,
        5,
        8,
        3,
        4,
        6,
        5,
        3,
        9,
        8,
        7,
        1,
        4,
        2,
        9,
        7,
        4,
        3,
        2,
        1,
        5,
        6,
        8,
        8,
        2,
        1,
        5,
        4,
        6,
        9,
        7,
        3,
    ]
    return solution


@pytest.fixture()
def medium():
    medium = [
        0,
        7,
        0,
        0,
        3,
        0,
        0,
        1,
        0,
        1,
        3,
        9,
        0,
        8,
        2,
        0,
        6,
        0,
        6,
        0,
        0,
        0,
        0,
        0,
        0,
        8,
        0,
        7,
        0,
        2,
        0,
        0,
        0,
        0,
        0,
        1,
        0,
        0,
        0,
        9,
        0,
        4,
        0,
        0,
        0,
        8,
        0,
        0,
        0,
        0,
        0,
        9,
        0,
        6,
        0,
        8,
        0,
        0,
        0,
        0,
        0,
        0,
        5,
        0,
        5,
        0,
        1,
        4,
        0,
        2,
        9,
        7,
        0,
        1,
        0,
        0,
        9,
        0,
        0,
        3,
        0,
    ]
    return medium


@pytest.fixture()
def medium_solution():
    medium_solution = [
        4,
        7,
        8,
        6,
        3,
        9,
        5,
        1,
        2,
        1,
        3,
        9,
        5,
        8,
        2,
        7,
        6,
        4,
        6,
        2,
        5,
        4,
        1,
        7,
        3,
        8,
        9,
        7,
        9,
        2,
        8,
        6,
        3,
        4,
        5,
        1,
        5,
        6,
        1,
        9,
        7,
        4,
        8,
        2,
        3,
        8,
        4,
        3,
        2,
        5,
        1,
        9,
        7,
        6,
        9,
        8,
        7,
        3,
        2,
        6,
        1,
        4,
        5,
        3,
        5,
        6,
        1,
        4,
        8,
        2,
        9,
        7,
        2,
        1,
        4,
        7,
        9,
        5,
        6,
        3,
        8,
    ]
    return medium_solution


@pytest.fixture()
def hard():
    hard = [
        0,
        4,
        3,
        1,
        0,
        0,
        0,
        0,
        0,
        7,
        0,
        9,
        4,
        6,
        0,
        0,
        0,
        0,
        8,
        0,
        6,
        0,
        0,
        3,
        0,
        1,
        0,
        9,
        0,
        2,
        0,
        0,
        7,
        0,
        0,
        0,
        0,
        6,
        0,
        0,
        0,
        0,
        0,
        4,
        0,
        0,
        0,
        0,
        3,
        0,
        0,
        9,
        0,
        7,
        0,
        7,
        0,
        6,
        0,
        0,
        2,
        0,
        5,
        0,
        0,
        0,
        0,
        2,
        4,
        6,
        0,
        1,
        0,
        0,
        0,
        0,
        0,
        1,
        4,
        3,
        0,
    ]
    return hard


@pytest.fixture()
def hard_solution():
    hard_solution = [
        2,
        4,
        3,
        1,
        7,
        5,
        8,
        9,
        6,
        7,
        1,
        9,
        4,
        6,
        8,
        3,
        5,
        2,
        8,
        5,
        6,
        2,
        9,
        3,
        7,
        1,
        4,
        9,
        3,
        2,
        5,
        4,
        7,
        1,
        6,
        8,
        1,
        6,
        7,
        9,
        8,
        2,
        5,
        4,
        3,
        5,
        8,
        4,
        3,
        1,
        6,
        9,
        2,
        7,
        4,
        7,
        1,
        6,
        3,
        9,
        2,
        8,
        5,
        3,
        9,
        5,
        8,
        2,
        4,
        6,
        7,
        1,
        6,
        2,
        8,
        7,
        5,
        1,
        4,
        3,
        9,
    ]
    return hard_solution


@pytest.fixture()
def extremly_hard():
    extremly_hard = [
        9,
        6,
        0,
        0,
        4,
        0,
        1,
        0,
        0,
        0,
        0,
        0,
        3,
        8,
        0,
        0,
        0,
        0,
        7,
        0,
        8,
        0,
        6,
        0,
        0,
        0,
        9,
        1,
        2,
        0,
        8,
        0,
        0,
        9,
        0,
        3,
        0,
        0,
        0,
        0,
        5,
        0,
        0,
        0,
        0,
        3,
        0,
        5,
        0,
        0,
        2,
        0,
        6,
        4,
        8,
        0,
        0,
        0,
        9,
        0,
        4,
        0,
        7,
        0,
        0,
        0,
        0,
        3,
        8,
        0,
        0,
        0,
        0,
        0,
        9,
        0,
        2,
        0,
        0,
        8,
        5,
    ]
    return extremly_hard


# @pytest.fixture()
# def extremely_solution():
#     extreme_solution = [
#         9,
#         6,
#         2,
#         7,
#         4,
#         5,
#         1,
#         3,
#         8,
#         5,
#         4,
#         1,
#         3,
#         8,
#         9,
#         2,
#         7,
#         6,
#         7,
#         3,
#         8,
#         2,
#         6,
#         1,
#         5,
#         4,
#         9,
#         1,
#         2,
#         6,
#         8,
#         7,
#         4,
#         9,
#         5,
#         3,
#         4,
#         9,
#         7,
#         6,
#         5,
#         3,
#         8,
#         1,
#         2,
#         3,
#         8,
#         5,
#         9,
#         1,
#         2,
#         7,
#         6,
#         4,
#         8,
#         5,
#         3,
#         1,
#         9,
#         6,
#         4,
#         2,
#         7,
#         2,
#         7,
#         4,
#         5,
#         3,
#         8,
#         6,
#         9,
#         1,
#         6,
#         1,
#         9,
#         4,
#         2,
#         7,
#         3,
#         8,
#         5,
#     ]
#     return extreme_solution
