a = float(input("Enter the first number: "))
b = float(input("Enter the second number, please: "))
act = input("Enter the needed operation - like: +, -, *, /, div, mod, pow: ")

if (act == "/" or act == "mod" or act == "div") and b == 0:
    result_of_operation = "Invalid operation - ZERO division!"
elif act == "+":
    result_of_operation = a + b
elif act == "-":
    result_of_operation = a - b
elif act == "/":
    result_of_operation = a / b
elif act == "*":
    result_of_operation = a * b
elif act == "mod":
    result_of_operation = a % b
elif act == "div":
    result_of_operation = a // b
elif act == "pow":
    result_of_operation = a ** b

print("The result of operation is: ", result_of_operation)
