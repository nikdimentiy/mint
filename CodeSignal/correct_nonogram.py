import itertools


def solution(size, nonogramField):
    w = (size + 1) // 2
    return all(
        [int(s) for s in row[:w] if s.isdigit()] ==
        [len(list(x)) for k, x in itertools.groupby(row) if k == '#']
        for row in nonogramField + list(zip(*nonogramField)))
