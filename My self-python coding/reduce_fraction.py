n, m = int(input()), int(input())


def gcd(n, m):  # Greatest Common Divisor
    if n > m:
        if n % m == 0:
            return m
        return gcd(n % m, m)
    if m % n == 0:
        return n
    return gcd(n, m % n)


def ReduceFraction(n, m):
    p = int((n / gcd(n, m)))
    q = int((m / gcd(n, m)))
    return p, q


print(*ReduceFraction(n, m))
