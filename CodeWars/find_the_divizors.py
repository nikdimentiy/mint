def divisors(integer):
    l = [n for n in range(2, integer) if integer % n == 0]
    return l if len(l) > 0 else "{} is prime".format(integer)
