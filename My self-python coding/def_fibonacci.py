# function of Fibonacci sequence
def fib(n):
    if n == 1 or n == 2:  # condition to exit for first and second numbers of sequence 
        return 1
    else:
        return fib(n - 1) + fib(n - 2)  # recursion call


index = int(input('Enter the needed number of Fibonacci sequence: '))
print(fib(index))
