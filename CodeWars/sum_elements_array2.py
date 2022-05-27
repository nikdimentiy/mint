def parts_sums(ls):
    d = sum(ls)
    r = [d]
    for i in ls:
        d = d-i
        r.append(d)
    return r
