# A cyclops number is a number in binary that is made up of all 1's, with one 0 in the exact middle.
# That means all cyclops numbers must have an odd number of digits for there to be an exact middle.
# A couple examples:
# 101
# 11111111011111111
# You must take an input, n, that will be in decimal format (base 10), then return True
# if that number wil be a cyclops number when converted to binary, or False if it won't.
# Assume n will be a positive integer.


def cyclops(n):
    # convert n to binary and remove the '0b' prefix
    binary = bin(n)[2:]

    # check if binary has an odd number of digits and a single '0' in the middle
    middle_index = len(binary) // 2
    return len(binary) % 2 == 1 and binary[middle_index] == '0' and '0' not in binary[:middle_index] + binary[middle_index+1:]
