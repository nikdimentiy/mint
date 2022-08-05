n = int(input())
k = 1
i = 1
while k <= n:
    for i in range(1, k + 1):
        print(i, end="")
    print()
    k += 1
