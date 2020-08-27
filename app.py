from flask import Flask, request, render_template
from sudoku_solver.sudoku_grid import Sudoku


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/update", methods=["GET", "POST"])
def update():
    input_sudoku = [[]]

    for y in range(9):
        for x in range(9):
            input_sudoku[y][x] = int(request.form[f"{x}{y}"])
    sudoku_grid = Sudoku(input_sudoku)
    final_solution = sudoku_grid.solve()
    return render_template("solutions.html", final_solution=final_solution)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
