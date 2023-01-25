# Factorial of a non-negative integer, is multiplication of all integers smaller than or equal to n
def factorial(n):
    if n == 0:
        return 1  # condition to exit
    else:
        return n * factorial(n - 1)  # recursion call


number = int(input("Enter the integer number to factorize: "))
print(factorial(number))