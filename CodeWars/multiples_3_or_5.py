def solution(number):
    """
    Calculate the sum of all multiples of 3 or 5 below a given number.
    
    This function finds all natural numbers below the input number that are
    multiples of 3 or 5 and returns their sum. Numbers that are multiples
    of both 3 and 5 are only counted once.
    
    Args:
        number (int): The upper bound (exclusive) for finding multiples
    
    Returns:
        int: The sum of all multiples of 3 or 5 below the input number.
             Returns 0 for negative input.
    
    Examples:
        >>> solution(10)
        23  # Sum of 3, 5, 6, 9
        >>> solution(20)
        78  # Sum of 3, 5, 6, 9, 10, 12, 15, 18
        >>> solution(-5)
        0   # Negative input returns 0
    """
    # Return 0 for negative input
    if number < 0:
        return 0
    
    # Use list comprehension to find all numbers below 'number'
    # that are divisible by either 3 or 5
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)

# Driver code
if __name__ == "__main__":
    # Test cases
    test_cases = [10, 20, 100, -5, 0]
    
    for test in test_cases:
        result = solution(test)
        print(f"Sum of multiples of 3 or 5 below {test}: {result}")
        
    # Additional verification
    assert solution(10) == 23, "Test case 1 failed"
    assert solution(-5) == 0, "Test case 2 failed"
    assert solution(0) == 0, "Test case 3 failed"
    print("All test cases passed!")
