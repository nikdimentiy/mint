def summa(n):
    n = int(input())
    if n == 0:
        return n
    return n + summa(n)


n = 0
print(summa(n))
