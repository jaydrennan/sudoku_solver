from sudoku_solver.find_possible_values import (
    solve_grid,
    row,
    column,
    compile_all_possible_values,
    fill_grid,
)


def test_solve(original_sudoku_single, solution_single):
    solution = solve_grid(original_sudoku_single)
    assert solution == solution_single


def test_medium(medium, medium_solution):
    solution_medium = solve_grid(medium)
    assert solution_medium == medium_solution


def test_hard(hard, hard_solution):
    solution_hard = solve_grid(hard)
    assert solution_hard == hard_solution


def test_extreme(extremly_hard, extremely_solution):
    solution_extreme = solve_grid(extremly_hard)
    assert solution_extreme == extremely_solution


def test_fill_grid(medium):
    fill_grid(medium)
    assert medium[2] == 8


def test_compile_all_possible_values():
    index_possible_solutions = {0: [1, 2, 3], 4: [3, 4, 5], 6: [1, 2, 4, 5, 6, 7]}
    combined = [1, 2, 3, 3, 4, 5, 1, 2, 4, 5, 6, 7]
    assert compile_all_possible_values(index_possible_solutions) == combined


def test_check_row(original_sudoku_single):
    assert row(0, 1, original_sudoku_single) is False
    assert row(9, 2, original_sudoku_single) is True
    assert row(27, 9, original_sudoku_single) is True
    assert row(54, 2, original_sudoku_single) is True


def test_column(original_sudoku_single):
    assert column(1, 6, original_sudoku_single) is True
    assert column(6, 3, original_sudoku_single) is True
    assert column(8, 28, original_sudoku_single) is False
    assert column(8, 5, original_sudoku_single) is True
    assert column(8, 1, original_sudoku_single) is False
