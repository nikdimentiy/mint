# Time complexity:  O(n2)
# Space complexity: O(1)

def bubble_sort(sequence):
    n = len(sequence)
    for i in range(n-1):
        for j in range(n-i-1):
            if (sequence[j] > sequence[j+1]):
                sequence[j], sequence[j+1] = sequence[j+1], sequence[j]
    return sequence


my_list = [1, 8, 6, 4, 1, 3, 0, 8, 9, 3, 7]
result = bubble_sort(my_list)
print(result)
