def sentinel_linear_search(arr, x):
    """
    Perform a sentinel linear search for a target value in an array.

    Parameters:
    arr (list): The list of elements to search through.
    x: The target value to search for.

    Returns:
    int: The index of the target value if found, otherwise "NOT-FOUND".
    """
    n = len(arr)
    
    # Step 1: Save the last element and set the sentinel
    last = arr[n - 1]
    arr[n - 1] = x  # Set the sentinel value to the target

    i = 0  # Step 2: Initialize index i to 0

    # Step 3: Search for x
    while arr[i] != x:
        i += 1

    # Step 4: Restore the last element to its original value
    arr[n - 1] = last

    # Step 5: Check if the target was found
    if i < n - 1 or arr[n - 1] == x:
        return i  # Return the index of x
    else:
        return "NOT-FOUND"  # Return NOT-FOUND if x is not in the array

# Driver code to test the sentinel_linear_search function
if __name__ == "__main__":
    # Test cases
    test_arrays = [
        [3, 5, 2, 4, 1],
        [10, 20, 30, 40, 50],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [1, 1, 1, 1, 1]
    ]
    
    test_values = [4, 30, 1, 6, 1]  # Values to search for

    for arr, x in zip(test_arrays, test_values):
        result = sentinel_linear_search(arr, x)
        print(f"Searching for {x} in {arr}: {result}")
