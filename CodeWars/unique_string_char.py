# In this Kata, you will be given two strings a and b and your task
# will be to return the characters that are not common in the two strings.

# For example:

# solve("xyab","xzca") = "ybzc"
# --The first string has 'yb' which is not in the second string.
# --The second string has 'zc' which is not in the first string.
# Notice also that you return the characters from the first string concatenated with those from the second string.


def solve(a, b):
    return "".join([c for c in a if c not in b] + [c for c in b if c not in a])
