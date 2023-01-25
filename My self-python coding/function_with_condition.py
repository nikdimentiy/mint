def function(x):
    if x < 0:
        return x ** 2
    else:
        return x * 3

def main():
    for i in range(-3, 5):
        y = function(i)
        print("result of operation: ", "i = ", i, "|", "y = ", y)


x = int(input("Enter the integer number, please: "))

print("Result of operation is: ", main())

