def gcd(a, b) -> int:
    while (b != 0):
        temp = a
        a = b
        b = temp % b
    return a


print(gcd(20, 8))
