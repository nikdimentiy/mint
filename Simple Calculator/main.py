from replit import clear  # Import the 'clear' function from the 'replit' module
from art import logo  # Import the 'logo' from the 'art' module

# Define a function to add two numbers
def add(n1, n2):
  return n1 + n2

# Define a function to subtract one number from another
def subtract(n1, n2):
  return n1 - n2

# Define a function to multiply two numbers
def multiply(n1, n2):
  return n1 * n2

# Define a function to divide one number by another
def divide(n1, n2):
  return n1 / n2

# Create a dictionary that maps operation symbols to their respective functions
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

# Define the main calculator function
def calculator():
  print(logo)  # Print the calculator logo

  num1 = float(input("What's the first number?: "))  # Get the first number from the user

  # Print the available operation symbols
  for symbol in operations:
    print(symbol)

  should_continue = True  # Initialize a variable to control whether the calculator should continue

  # Start a loop for performing calculations
  while should_continue:
    operation_symbol = input("Pick an operation: ")  # Get the operation symbol from the user
    num2 = float(input("What's the next number?: "))  # Get the second number from the user

    # Retrieve the corresponding calculation function based on the operation symbol
    calculation_function = operations[operation_symbol]

    # Perform the calculation and print the result
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    # Ask the user if they want to continue with the result or start a new calculation
    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer  # Update num1 with the result if the user wants to continue
    else:
      should_continue = False  # Set should_continue to False to exit the loop

      # Clear the console screen
      clear()

      # Start a new calculation by calling the 'calculator' function recursively

# Start the calculator
calculator()
