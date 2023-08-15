def quickSort(array):
    """
    Sorts an array using the Quick Sort algorithm.

    This function takes an input array and sorts it in ascending order using the Quick Sort algorithm.
    
    Args:
        array (list): The input list of elements to be sorted.
        
    Returns:
        list: A new sorted list containing the elements from the input array.
    """
    if len(array) < 2:
        return array
    else:
        # Choose the first element as the pivot
        pivot = array[0]

        # Divide the array into two sub-arrays: less and greater
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]

        # Recursively sort the sub-arrays and concatenate them around the pivot
        return quickSort(less) + [pivot] + quickSort(greater)

# Driver code
if __name__ == "__main__":
    unsorted_array = [3, 9, 8, 4, 2, 0, 7, 1]
    sorted_array = quickSort(unsorted_array)
    print("Unsorted Array:", unsorted_array)
    print("Sorted Array:", sorted_array)

