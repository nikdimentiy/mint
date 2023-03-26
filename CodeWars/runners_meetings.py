def solution(p, s):
    if len(set(s)) == 1:
        return -1
    t = []
    a = []
    for i in range(len(p)-1):
        for j in range(i+1, len(p)):
            try:
                t.append((p[j]-p[i])/(s[i]-s[j]))
            except ZeroDivisionError:
                break
    asdkjf = (max(t, key=t.count))
    for i in range(len(p)):
        a.append(p[i]+s[i]*asdkjf)
    return a.count(max(a, key=a.count))
