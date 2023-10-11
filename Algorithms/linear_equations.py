# # Import the sympy library for symbolic computations
# import sympy as sp
#
# # Define the symbols x and y
# x, y = sp.symbols('x y')
#
# # Define the linear equations
# eq1 = sp.Eq(x + y, 25)  # x + y = 25
# eq2 = sp.Eq(y, x - 5)  # y = x - 8
#
# # Solve the system of equations using the solve function
# solution = sp.solve([eq1, eq2], [x, y])
#
# # Extract the decimal values from the solution and round to two decimal places
# x_value = round(solution[x].evalf(), 1)
# y_value = round(solution[y].evalf(), 1)
#
# # Print the rounded solution
# print(f"x = {x_value:.1f}")
# print(f"y = {y_value:.1f}")

# Import the sympy library for symbolic computations
import sympy as sp

# Define the symbols x and y
x, y = sp.symbols('x y')

# Ask the user to enter the final result of x + y and the value of any number
final_result = float(input("Enter the final result of x + y: "))
any_number = float(input("Enter any number -> (y = x - number): "))

# Define the linear equations
eq1 = sp.Eq(x + y, final_result)  # x + y = final_result
eq2 = sp.Eq(y, x - any_number)  # y = x - any_number

# Solve the system of equations using the solve function
solution = sp.solve([eq1, eq2], [x, y])

# Extract the decimal values from the solution and round to two decimal places
x_value = round(solution[x].evalf(), 2)
y_value = round(solution[y].evalf(), 2)

# Print the rounded solution
print(f"x = {x_value}")
print(f"y = {y_value}")
