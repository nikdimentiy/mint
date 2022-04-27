def findleft_x(seq, x):
    ans = -1
    for i in range(len(seq)):
        if ans == -1 and seq[i] == x:
            ans = i
    return ans

sequence = [4, 7, 9, 23, 4, 7, 9, 3, 1, 2, 7]
number = int(input("Enter the integer number: "))
print(findleft_x(sequence, number))
