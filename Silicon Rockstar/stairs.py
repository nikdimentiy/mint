# Given a natural number -> output a ladder of n steps, the i-th step consists of numbers from 1 to i without spaces.

n = int(input())
k = 1
i = 1
while k <= n:
    for i in range(1, k + 1):
        print(i, end="")
    print()
    k += 1
