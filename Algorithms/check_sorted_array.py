def check_sorted_array(array):
    """
    This function checks if the given array is sorted in ascending order.

    Args:
        array: The array to check.

    Returns:
        True if the array is sorted, False otherwise.
    """
    # Iterate through the array
    for i in range(len(array) - 1):
        # Check if the current element is greater than the next element
        if array[i] > array[i + 1]:
            # If so, the array is not sorted in ascending order
            return False
    
    # If we reach this point, the array is sorted in ascending order
    return True

# Driver code to test the function
arr = [1, 2, 3, 4, 5]
print(check_sorted_array(arr))  # True

arr = [5, 4, 3, 2, 1]
print(check_sorted_array(arr))  # False

arr = [1, 3, 2, 4, 5]
print(check_sorted_array(arr))  # False
