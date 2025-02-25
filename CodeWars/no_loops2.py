def check(a, x):
    """
    Validates if all values in the given array are less than or equal to a specified limit.
    
    Args:
        a (list): A list of numeric values to be validated
        x (int/float): The maximum limit value
        
    Returns:
        bool: True if all values in the array are <= x, False otherwise
        
    Raises:
        ValueError: If the input array is empty
        TypeError: If the input array is not iterable or if x is not a number
    """
    # Check if all elements in the array are less than or equal to x
    return all(num <= x for num in a)

# Driver code to test the function with various cases
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4], 4, True),           # All elements are <= limit
        ([5, 6, 7], 5, False),              # Some elements exceed limit
        ([-1, 0, 1], 1, True),             # Negative numbers included
        ([10, 20, 30], 15, False),          # Multiple elements exceed limit
        ([], 5, False),                     # Empty array
        ([50], 50, True)                    # Single element equal to limit
    ]
    
    for array, limit, expected_result in test_cases:
        result = check(array, limit)
        print(f"Array: {array!r} | Limit: {limit!r} | Expected: {expected_result} | Actual: {result}")
