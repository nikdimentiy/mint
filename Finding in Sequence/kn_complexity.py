#  k*n complexity of the algorithm 
#  (where k - it's number of unique symbols, n - number of sequence elements)

s = input()
ans = ""
anscnt = 0
for now in set(s):
    nowcnt = 0
    for j in range(len(s)):
        if now == s[j]:
            nowcnt += 1
    if nowcnt > anscnt:
        ans = now
        anscnt = nowcnt

print(ans)
