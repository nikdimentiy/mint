def getTotal(costs, items, tax):
    subtotal = sum([costs.get(i, 0) for i in items])
    total = subtotal * (1+tax)
    return round(total, 2)
