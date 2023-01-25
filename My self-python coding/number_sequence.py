# the code outputs part of the sequence 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ...
# (the number is repeated as many times as it is)

a = int(input())
m = []
for i in range(a):
    j = 0
    while j < i + 1:
        m.append(i + 1)
        j += 1
    if len(m) > a:
        break
m = m[0:a]
for i in m:
    print(i, end=" ")
