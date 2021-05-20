# the code demonstrate: classic game - sapper
print("Enter in a space: 1 - number of lines field, 2 - number of column field, 3 - number of bombs: ")
n, m, k = (int(i) for i in input().split())  # input field sizes and number of bombs
a = [[0 for j in range(m)] for i in range(n)]  # filling the fields with default value = zero
print("Enter in a space: the coordinates of the bomb (row, column): ")
for i in range(k):
    row, col = (int(i) - 1 for i in input().split())
    a[row][col] = -1  # placing bombs
for i in range(n):
    for j in range(m):
        if a[i][j] == 0:  # there is no bomb in this cell, so we count the number of bombs around
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    ai = i + di
                    aj = j + dj
                    # (ai, aj)
                    if 0 <= ai < n and 0 <= aj < m and a[ai][aj] == -1:
                        a[i][j] += 1
# output results
for i in range(n):
    for j in range(m):
        if a[i][j] == -1:
            print('*', end='')
        elif a[i][j] == 0:
            print('.', end='')
        else:
            print(a[i][j], end='')
    print()
