from flask import Flask, render_template, request
import sympy as sp

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def solve_equations():
    if request.method == 'POST':
        final_result = float(request.form['final_result'])
        any_number = float(request.form['any_number'])

        x, y = sp.symbols('x y')
        eq1 = sp.Eq(x + y, final_result)
        eq2 = sp.Eq(y, x - any_number)

        solution = sp.solve([eq1, eq2], [x, y])
        x_value = round(float(solution[x].evalf()), 1)
        y_value = round(float(solution[y].evalf()), 1)

        return render_template('result.html', x=x_value, y=y_value)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
