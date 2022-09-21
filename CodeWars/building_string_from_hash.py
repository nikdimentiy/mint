# Complete the solution so that it takes the object  or hash,
# passed in and generates a human readable string from its key/value pairs.

# The format should be "KEY = VALUE". Each key/value pair should be separated by a comma except for the last pair.


def solution(pairs):
    return ",".join(sorted(["{} = {}".format(k, v) for k, v in pairs.items()]))
