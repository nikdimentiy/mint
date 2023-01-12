def gen_bin(M, prefix=''):
    if M == 0:
        print(prefix)
        return
    for digits in "0", "1":
        gen_bin(M-1, prefix+digits)


def generate_number(N: int, M: int, prefix=None):
    """ genaration of numbers in N (number system)--> N <= 10
        N = number system
        M = length of number
    """
    prefix = prefix or []
    if M == 0:
        print(prefix)
        return
    for digit in range(N):
        prefix.append(digit)
        generate_number(N, M - 1, prefix)
        prefix.pop()


# gen_bin(12)
generate_number(2, 8)

