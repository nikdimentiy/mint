
def inf_database(range_, str_, val):
    global A001055
    s = {
        "higher than": lambda a, b: a > b,
        "higher and equals to": lambda a, b: a >= b,
        "equals to": lambda a, b: a == b,
        "lower than": lambda a, b: a < b,
        "lower and equals to": lambda a, b: a <= b}

    if str_ in s:
        l = [i for i in range(range_[0], range_[1]+1)
             if s[str_](A001055[i], val)]
        return (len(l), l)
    else:
        return "wrong constraint"
