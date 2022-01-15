# square complexity of the algorithm

s = input() #input sequence
ans = ""  # empty string
anscnt = 0  # empty (zero) counting
for i in range(len(s)):
    nowcnt = 0
    for j in range(len(s)):
        if s[i] == s[j]:
            nowcnt += 1
    if nowcnt > anscnt:
        ans = s[i]
        anscnt = nowcnt
print(ans)
