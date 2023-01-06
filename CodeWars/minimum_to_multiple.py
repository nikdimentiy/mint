# Given two integers a and x, return the minimum non-negative number
# to add to / subtract from a to make it a multiple of x.

# minimum(10, 6)  #= 2

# 10+2 = 12 which is a multiple of 6
# Note

# 0 is always a multiple of x


def minimum(a, x):
    return min([a % x, x-(a % x)])
