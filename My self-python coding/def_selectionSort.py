def findSmallest(arr: list):
    smallest = arr[0] # stores the smallest value
    smallest_index = 0 # stores the index of the smallest value
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionSort(arr: list): # sort an array
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr) # finds the smallest element in the array, and adds it to the new array
        newArr.append(arr.pop(smallest))
    return newArr


print(selectionSort([5, 3, 6, 2, 10]))
