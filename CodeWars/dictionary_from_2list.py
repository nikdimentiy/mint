def createDict(keys, values):
    d = {}
    for e, i in enumerate(keys):
        if e < len(values):
            d[i] = values[e]
        else:
            d[i] = None
    return d
