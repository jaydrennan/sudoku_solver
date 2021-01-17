from flask import Flask, request, render_template, jsonify, abort
from sudoku_solver.sudoku_grid import Sudoku


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/solve", methods=["POST"])
def solve():

    sudoku_json = request.get_json()

    input_sudoku = [convert_to_ints(box["value"]) for box in sudoku_json]

    sudoku_grid = Sudoku(input_sudoku)

    if not sudoku_grid.is_valid():
        abort(
            400,
            description="There are either repeat values in row, column, or quadrant. Or value is out of range(1-9)",
        )

    final_solution = sudoku_grid.solve()
    grid_dict = {}

    index = 0
    for y in range(9):
        for x in range(9):
            grid_dict[f"{x}{y}"] = final_solution[index]
            index += 1
    solved_json = jsonify(grid_dict)
    return solved_json


@app.errorhandler(400)
def resource_not_found(e):
    return jsonify(error=str(e)), 400


def convert_to_ints(val):
    if val == "":
        return 0
    return int(val)
