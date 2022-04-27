def findright_x(seq, x):
    ans = -1
    for i in range(len(seq)):
        if seq[i] == x:
            ans = i
    return ans

sequence = [4, 7, 9, 23, 4, 7, 9, 0, 1, 2]
number = int(input("Enter the integer number: "))
print(findright_x(sequence, number))
