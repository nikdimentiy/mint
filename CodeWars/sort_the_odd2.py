def sort_array(arr):
    """
    Sorts odd numbers in ascending order while keeping even numbers in their original positions.
    
    Args:
        arr (list): A list of integers to be processed
        
    Returns:
        list: A new list where odd numbers are sorted in ascending order and 
              even numbers remain in their original positions
              
    Example:
        >>> sort_array([5, 2, 3, 8, 1, 4])
        [1, 2, 3, 8, 5, 4]
    """
    # Extract and sort all odd numbers in descending order
    # (we use reverse=True because we'll be popping from the end)
    odds = sorted((x for x in arr if x % 2 != 0), reverse=True)
    
    # Create the result list by keeping even numbers in place
    # and replacing odd numbers with values from the sorted odds list
    return [x if x % 2 == 0 else odds.pop() for x in arr]


# Driver code to test the function
if __name__ == "__main__":
    # Test case 1: Mixed odd and even numbers
    test1 = [5, 3, 2, 8, 1, 4]
    print(f"Original array: {test1}")
    print(f"After sorting odds: {sort_array(test1)}")
    # Expected output: [1, 3, 2, 8, 5, 4]
    
    # Test case 2: Only odd numbers
    test2 = [9, 7, 5, 3, 1]
    print(f"\nOriginal array: {test2}")
    print(f"After sorting odds: {sort_array(test2)}")
    # Expected output: [1, 3, 5, 7, 9]
    
    # Test case 3: Only even numbers (no change expected)
    test3 = [8, 6, 4, 2]
    print(f"\nOriginal array: {test3}")
    print(f"After sorting odds: {sort_array(test3)}")
    # Expected output: [8, 6, 4, 2]
    
    # Test case 4: Empty array
    test4 = []
    print(f"\nOriginal array: {test4}")
    print(f"After sorting odds: {sort_array(test4)}")
    # Expected output: []
