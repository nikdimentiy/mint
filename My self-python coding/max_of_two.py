a = int(input("Enter first integer number: "))
b = int(input("Enter second integer number: "))

c = a // b
d = b // a
print("The max number, of two entered numbers is:", (a * c + b * d) // (c + d))
