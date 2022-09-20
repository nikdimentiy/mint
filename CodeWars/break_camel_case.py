# Complete the solution so that the function will break up camel casing, using a space between words.

def solution(s):
    return "".join([" " + c if c.isupper() else c for c in s])

