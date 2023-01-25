def isprime(n):
    if n <= 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True


def list_primes():
    for n in range(100):
        if isprime(n):
            print(n, end=' ')
    print()


n = int(input("Please, enter positive integer: "))

if isprime(n):
    print(f"{n} is prime number!")
else:
    print(f"{n} not is a prime number!")


list_primes()
