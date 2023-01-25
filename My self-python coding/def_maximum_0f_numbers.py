def max_2(x, y):
    if x > y:
        return x
    return y


def max_3(x, y, z):
    return max_2(x, max_2(y, z))


print("Enter 3 numbers to calculate the max value of them: ")
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
z = int(input("Enter the third number: "))

result = max_3(x, y, z)
print("The result of operation is: ", result)

