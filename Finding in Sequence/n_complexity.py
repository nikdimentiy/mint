#  n complexity of the algorithm (where n - number of sequence elements)

s = input()
anscnt = 0
symcnt = {} # using dictionary 
for now in s:
    if now not in symcnt:
        symcnt[now] = 0 # added value in dict using key=now
    symcnt[now] += 1
    if symcnt[now] > anscnt:
        ans = now
        anscnt = symcnt[now]

print(ans)
