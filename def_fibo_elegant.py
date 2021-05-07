# Elegance version of code - Fibonacci sequence
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a + b
    print()


n = int(input("Enter integer number: "))
print("The Fibonacci sequence - before the entered number is", fib(n))
