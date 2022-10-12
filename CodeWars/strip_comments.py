def solution(string, markers):
    s = string.splitlines()
    for i in range(len(s)):
        for j in markers:
            if j in s[i]:
                s[i] = s[i][:s[i].index(j)].rstrip()
    return "\n".join(s)
