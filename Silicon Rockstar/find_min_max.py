def find_min_max(arr):
    """
    Find the minimum and maximum values in an array.

    Parameters:
    arr (list): A list of numerical values.

    Returns:
    tuple: A tuple containing the minimum and maximum values. 
           Returns (None, None) if the array is empty.
    """
    if len(arr) == 0:
        return None, None  # Return None for both min and max if the array is empty
    elif len(arr) == 1:
        return arr[0], arr[0]  # If the array has only one element, return it as both min and max

    # Initialize min and max values
    if arr[0] > arr[1]:
        min_val = arr[1]
        max_val = arr[0]
    else:
        min_val = arr[0]
        max_val = arr[1]

    # Compare pairs of elements
    for i in range(2, len(arr), 2):
        if i + 1 < len(arr):  # Check if there is a pair
            if arr[i] > arr[i + 1]:
                max_val = max(max_val, arr[i])  # Update max_val
                min_val = min(min_val, arr[i + 1])  # Update min_val
            else:
                max_val = max(max_val, arr[i + 1])  # Update max_val
                min_val = min(min_val, arr[i])  # Update min_val
        else:  # If there is one element left
            min_val = min(min_val, arr[i])  # Update min_val
            max_val = max(max_val, arr[i])  # Update max_val

    return min_val, max_val  # Return the minimum and maximum values

# Driver code
if __name__ == "__main__":
    arr = [1, 6, 2, 4, 7, 8, 7, 5, 6]  # Example array
    minimum, maximum = find_min_max(arr)  # Find min and max
    print(f'Minimum: {minimum}, Maximum: {maximum}')  # Print the results
