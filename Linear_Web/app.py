from flask import Flask, render_template, request
import sympy as sp

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def solve_equations():
    """
    Solves a system of two equations with two variables and displays the result.

    This function handles both GET and POST requests. In a GET request, it renders
    the initial input form. In a POST request, it solves the equations and displays
    the results.

    Returns:
        HTML page with the results or the input form.
    """

    if request.method == 'POST':
        # Retrieve user input from the form
        final_result = float(request.form['final_result'])
        any_number = float(request.form['any_number'])

        # Define symbolic variables and equations
        x, y = sp.symbols('x y')
        eq1 = sp.Eq(x + y, final_result)
        eq2 = sp.Eq(y, x - any_number)

        # Solve the system of equations
        solution = sp.solve([eq1, eq2], [x, y])
        x_value = round(float(solution[x].evalf()), 1)
        y_value = round(float(solution[y].evalf()), 1)

        # Render the results page with the computed values
        return render_template('result.html', x=x_value, y=y_value)

    # Render the initial input form for GET requests
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
