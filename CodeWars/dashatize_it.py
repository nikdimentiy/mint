def dashatize(n):
    print(n)
    if type(n) == int:
        n = str(abs(n))
        new = ""
        for e, i in enumerate(n):
            if int(i) % 2 != 0:
                if e == 0:
                    new += "{}-".format(i)
                elif e == len(n)-1:
                    new += "-{}".format(i)
                else:
                    new += "-{}-".format(i)
            else:
                new += i
        if new[-1] == "-":
            new = new[:-1]
        return new.replace("--", "-")
    else:
        return "None"
