# You've just moved into a perfectly straight street with exactly n identical houses on either side of the road.
# Naturally, you would like to find out the house number of the people on the other side of the street.
# Given your house number address and length of street n, give the house number on the opposite side of the street.
# over_the_road(address, n)
# over_the_road(1, 3) = 6
# over_the_road(3, 3) = 4
# over_the_road(2, 3) = 5
# over_the_road(3, 5) = 8

def over_the_road(address, n):
    return (n*2) - address + 1
