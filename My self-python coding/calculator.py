# basic carculator
x = float(input("Enter first number, please: "))
y = float(input("Enter second number, please: "))

print("Enter the desire operation: +, -, *, /, mod, div, pow  ")
operation = input()
result = None

if operation == '+':
    result = x + y

elif operation == '-':
    result = x - y

elif operation == '/' and y == 0:
    print("Invalid operation.Division on zero!")

elif operation == '/':
    result = x / y

elif operation == '*':
    result = x * y

elif operation == 'mod'and y == 0:
    print("Invalid operation.Division on zero!")

elif operation == 'mod':
    result = x % y

elif operation == 'pow':
    result = x ** y

elif operation == 'div' and y == 0:
    print("Invalid operation.Division on zero!")

elif operation == 'div':
    result = x // y

if result is not None:
    print(result)
