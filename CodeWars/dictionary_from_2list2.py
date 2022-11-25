def createDict(keys, values):
    while len(keys) > len(values):
        values.append(None)

    dictionary = dict(zip(keys, values))
    return dictionary
