def findMax(seq):
    ans = seq[0]
    for i in range(len(seq)):
        if seq[i] > ans:
            ans = seq[i]
    return ans


seq = list(map(int, input().split()))
x = findMax(seq)
print("Maximum value in entered sequence is:", x)
