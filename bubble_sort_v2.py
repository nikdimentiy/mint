# Python script for implementing Bubble Sort

def bubble_sort(arr):
    n = len(arr)
    # iterate through array elements
    for i in range(n):
        for j in range(0, n-i-1):
            # swap if the element found is greater than the next
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


# Main program to test the above code
arr = [98, 22, 15, 32, 2, 74, 63, 70]

bubble_sort(arr)

print("Sorted array: ")
for i in range(len(arr)):
    print("%d" % arr[i])
