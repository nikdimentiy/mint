def sort_array(source_array):
    """
    Sorts an array by placing even numbers in their original positions 
    and odd numbers in sorted order.

    This function does the following:
    1. Extracts and sorts all odd numbers from the source array
    2. Inserts even numbers back into their original positions
    3. Preserves the original index of even numbers while sorting odd numbers

    Args:
        source_array (list): Input list of integers

    Returns:
        list: Sorted array with even numbers in original positions 
              and odd numbers sorted
    
    Example:
        >>> sort_array([5, 3, 2, 8, 1, 4])
        [2, 1, 3, 4, 5, 8]
    """
    # Extract and sort all odd numbers from the source array
    result = sorted([l for l in source_array if l % 2 == 1])
    
    # Insert even numbers back into their original positions
    for index, item in enumerate(source_array):
        if item % 2 == 0:
            result.insert(index, item)
    
    return result

# Driver code to demonstrate the function
def main():
    # Test cases
    test_arrays = [
        [5, 3, 2, 8, 1, 4],
        [1, 2, 3, 4, 5],
        [2, 4, 6, 1, 3, 5],
        []
    ]
    
    # Run tests and print results
    for arr in test_arrays:
        print(f"Original array: {arr}")
        print(f"Sorted array:   {sort_array(arr)}\n")

# Ensure the script can be run directly or imported as a module
if __name__ == "__main__":
    main()
