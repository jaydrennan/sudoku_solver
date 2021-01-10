import json
from application.app import app


def test_index(original_sudoku):
    response = app.test_client().get("/")
    assert response.status_code == 200


def test_solve(original_sudoku_single, solved_sudoku):
    data = []
    i = 0
    for y in range(9):
        for x in range(9):
            input_key = str(y) + str(x)
            data.append({"name": input_key, "value": original_sudoku_single[i]})
            i += 1

    json_data = json.dumps(data)
    response = app.test_client().post(
        "/solve", data=json_data, content_type="application/json",
    )
    assert response.status_code == 200

    response_solution = response.get_json()
    for y in range(9):
        for x in range(9):
            assert str(response_solution[f"{x}{y}"]) == str(solved_sudoku[y][x])
