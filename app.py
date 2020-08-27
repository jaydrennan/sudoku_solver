from flask import Flask, request, render_template, jsonify
from sudoku_solver.sudoku_grid import Sudoku


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/update", methods=["GET", "POST"])
def update():
    input_sudoku = [[0 for j in range(9)] for k in range(9)]

    for y in range(9):
        for x in range(9):
            input_sudoku[y][x] = int(request.form[f"{x}{y}"])

    sudoku_grid = Sudoku(input_sudoku)
    final_solution = sudoku_grid.solve()
    return render_template("solutions.html", final_solution=final_solution)


@app.route("/json", methods=["POST"])
def json_route():
    input_sudoku = [[0 for j in range(9)] for k in range(9)]

    sudoku_json = request.get_json()
    for y in range(9):
        for x in range(9):
            input_sudoku[y][x] = int(sudoku_json[f"{x}{y}"])
    sudoku_grid = Sudoku(input_sudoku)
    final_solution = sudoku_grid.solve()
    grid_dict = {}

    for y in range(9):
        for x in range(9):
            grid_dict[f"{x}{y}"] = final_solution[y][x]

    solved_json = jsonify(grid_dict)
    return solved_json


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
