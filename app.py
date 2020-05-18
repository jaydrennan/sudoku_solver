from flask import Flask, request, render_template

from sudoku_solver.sudoku_solver import get_solution


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

    final_solution = get_solution(input_sudoku)
    return render_template("solutions.html", final_solution=final_solution)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
