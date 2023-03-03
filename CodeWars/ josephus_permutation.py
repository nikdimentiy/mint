def josephus(items, k):
    result = []
    index = 0
    while len(items) > 0:
        index = (index + k - 1) % len(items)
        result.append(items.pop(index))
    return result
