import json
from application.app import app


def test_index(original_sudoku):
    response = app.test_client().get("/")
    assert response.status_code == 200


def test_json(original_sudoku_single, solved_sudoku):

    data = {}
    for i, val in enumerate(original_sudoku_single):
        data[i] = str(val)

    json_data = json.dumps(data)
    response = app.test_client().post(
        "/json", data=json_data, content_type="application/json",
    )
    assert response.status_code == 200

    response_solution = response.get_json()
    for y in range(9):
        for x in range(9):
            assert str(response_solution[f"{x}{y}"]) == str(solved_sudoku[y][x])


def test_update(original_sudoku_single):
    form_data = {}
    i = 0
    for y in range(9):
        for x in range(9):
            form_data[f"{x}{y}"] = original_sudoku_single[i]
    response = app.test_client().post("/update", data=form_data)
    assert response.status_code == 200
