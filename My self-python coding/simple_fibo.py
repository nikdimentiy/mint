# the code represents: Fibonacci sequence using loop (for)

userNumber = int(input("Enter a number: "))

n1 = 0
n2 = 1

print("\n The fibonacci sequence is :")
print(n1, ",", n2, end=", ")

for i in range(2, userNumber):
    next = n1 + n2
    print(next, end=", ")

    n1 = n2
    n2 = next
