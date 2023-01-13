import operator


def inf_database(range_, str_, val):
    global A001055
    s = {
        "higher than": operator.gt,
        "higher and equals to": operator.ge,
        "equals to": operator.eq,
        "lower than": operator.lt,
        "lower and equals to": operator.le}

    if str_ in s:
        l = [i for i in range(range_[0], range_[1]+1)
             if s[str_](A001055[i], val)]
        return (len(l), l)
    else:
        return "wrong constraint"
