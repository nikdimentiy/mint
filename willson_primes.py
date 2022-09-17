import math


def am_i_wilson(n):
    if n <= 2:
        return False
    fact = math.factorial(n-1)
    # this conditional checks that the number is prime or not
    # this condition is called wilson theorem in number theory
    if (fact+1) % n == 0:
        x = (fact+1) % (n**2)
        if x == 0:
            return True
        else:
            return False
    else:
        return False

