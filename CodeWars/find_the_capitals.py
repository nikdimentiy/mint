def capitals(word):
    inds = []
    i = 0
    for l in word:
        if l.isupper():
            inds.append(i)
        i += 1
    return inds
