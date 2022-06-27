def maximum_product(a, b=2):
    m, d = a, sum(divmod(a, 2))
    while b < d:
        p = b * maximum_product(a - b, b + 1)
        m = max(m, p)
        b += 1
    return m
