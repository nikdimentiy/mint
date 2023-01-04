def findSmallest(array):
    smallest = array[0]
    smallest_index = 0
    for i in range(1, len(array)):
        if array[i] < smallest:
            smallest = array[i]
            smallest_index = i
    return smallest_index


def selectionSort(array):
    newArray = []
    for i in range(len(array)):
        small_element = findSmallest(array)
        newArray.append(array.pop(small_element))
    return newArray


print(selectionSort([3, 9, 8, 4, 2, 0, 7, 1]))
