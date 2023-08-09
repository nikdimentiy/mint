"""
This program implements the selection sort algorithm.

The selection sort algorithm works by repeatedly finding the smallest element in the unsorted array and moving it to the front of the array.

Args:
    array: The array to be sorted.

Returns:
    The sorted array.
"""

def findSmallest(array):
    """Finds the smallest element in the array."""

    smallest = array[0]
    smallest_index = 0
    for i in range(1, len(array)):
        if array[i] < smallest:
            smallest = array[i]
            smallest_index = i
    return smallest_index


def selectionSort(array):
    """Sorts the array using the selection sort algorithm."""

    newArray = []
    for i in range(len(array)):
        # Find the smallest element in the unsorted array.
        smallest_index = findSmallest(array)

        # Remove the smallest element from the unsorted array.
        smallest = array.pop(smallest_index)

        # Append the smallest element to the sorted array.
        newArray.append(smallest)

    return newArray


# Test the function.
array = [3, 9, 8, 4, 2, 0, 7, 1]
print(selectionSort(array))
