# Tiny code: elegant version of the Fibonacci sequence calculation

n = int(input("Enter the number of sequence depth Fibonacci: "))
# List of Fibonacci numbers (originally two numbers: 1, 1)
fibs = [1, 1]
# We repeat (n - 2) times, since two numbers are already in the list
for i in range(n - 2):
    fibs.append(fibs[i] + fibs[i + 1])

print("The sequence Fibonacci:", fibs)
