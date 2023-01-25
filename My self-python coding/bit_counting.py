# Write a function that takes an integer as input,
# and returns the number of bits that are equal to one in the binary representation of that number.


def countBits(n):
    return bin(n).count("1")

