from flask import Flask, request, render_template, jsonify, abort
from sudoku_solver.sudoku_grid import Sudoku


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/solve", methods=["POST"])
def solve():

    input_sudoku = []
    sudoku_json = request.get_json()
    for box in sudoku_json:
        if box["value"] == "":
            input_sudoku.append(0)
        else:
            input_sudoku.append(int(box["value"]))
    sudoku_grid = Sudoku(input_sudoku)

    # if sudoku_grid.is_valid() == False:
    #     abort(433, description="Invalid sudoku puzzle")

    final_solution = sudoku_grid.solve()
    grid_dict = {}

    index = 0
    for y in range(9):
        for x in range(9):
            grid_dict[f"{x}{y}"] = final_solution[index]
            index += 1
    solved_json = jsonify(grid_dict)

    return solved_json


# @app.errorhandler(433)
# def resource_not_found(e):
#     return jsonify(error=str(e)), 433
