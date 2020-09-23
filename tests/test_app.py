import json
from app import app


def test_index(original_sudoku):
    response = app.test_client().get("/")
    assert response.status_code == 200


def test_json(original_sudoku, solved_sudoku):

    data = {}
    for y in range(0, 9):
        for x in range(0, 9):
            data[f"{x}{y}"] = str(original_sudoku[y][x])
    json_data = json.dumps(data)
    response = app.test_client().post(
        "/json", data=json_data, content_type="application/json",
    )
    assert response.status_code == 200

    response_solution = response.get_json()
    for y in range(9):
        for x in range(9):
            assert str(response_solution[f"{x}{y}"]) == str(solved_sudoku[y][x])