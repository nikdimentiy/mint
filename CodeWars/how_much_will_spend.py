def getTotal(costs, items, tax):
    return round(sum([costs[i] for i in items if i in costs]) * (1 + tax), 2)
