import math
from functools import cache


def maximum_product(n):
    return max(map(math.prod, partitions(n)))


@cache
def partitions(n, largest=math.inf):
    largest = min(n, largest)
    if not n:
        return [[]]
    res = []
    for i in range(1, largest + 1):
        rest = partitions(n - i, i - 1)
        for r in rest:
            res.append([i] + r)

    return res

