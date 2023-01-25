# The code calculates: which letter appears most often in the entered phrase

s = input("Enter some phrase or string: ")
anscnt = 0
symcnt = {}
for now in s:
    if now not in symcnt:
        symcnt[now] = 0
    symcnt[now] += 1
    if symcnt[now] > anscnt:
        ans = now
        anscnt = symcnt[now]

print(ans)
