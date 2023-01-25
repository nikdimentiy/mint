def factorial(n):
    if n == 0:
        return 1  # exit condition
    else:
        return n * factorial(n - 1)  # recursive call


n = int(input("Enter positive integer number: "))
print(factorial(n))
