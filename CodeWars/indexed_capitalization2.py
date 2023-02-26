# For example:
# capitalize("abcdef",[1,2,5]) = "aBCdeF"
# capitalize("abcdef",[1,2,5,100]) = "aBCdeF". There is no index 100.
# The input will be a lowercase string with no spaces and an array of digits.


def capitalize(s, ind):
    ind = set(ind)
    return ''.join(c.upper() if i in ind else c for i, c in enumerate(s))
