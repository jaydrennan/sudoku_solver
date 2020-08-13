from sudoku_solver.sudoku_solver import get_solution


def test_get_iterations():
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
    solution = get_solution(original_sudoku)
    assert solution == [
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
    assert len(solution) == 9
    for row in solution:
        assert len(row) == len(set(row))
        assert len(row) == 9
        assert 0 not in row
