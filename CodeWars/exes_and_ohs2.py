# Check to see if a string has the same amount of 'x's and 'o's.
# The method must return a boolean and be case insensitive. The string can contain any char.

# Examples:

# XO("ooxx") => true
# XO("xooxx") => false
# XO("ooxXm") => true
# XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
# XO("zzoo") => false


def xo(s):
    x_count, o_count = 0, 0

    for i in s:
        if i == 'x' or i == 'X':
            x_count += 1

        elif i == 'o' or i == 'O':
            o_count += 1

    if x_count == o_count:
        s = True
    else:
        s = False

    return s


print(xo("ooxXm") == True)
print(xo("ooxm") == False)
print(xo("mmnbm") == True)  # no x's or o's
print(xo("xmnOm") == True)
