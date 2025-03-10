def minimum(a, x):
    """
    Calculate the minimum non-negative number to add or subtract from a
    to make it a multiple of x.
    
    Args:
        a (int): The source integer
        x (int): The divisor to check multiples against
        
    Returns:
        int: The minimum non-negative number to add/subtract from a
             to make it a multiple of x
             
    Examples:
        >>> minimum(10, 6)
        2
        # 10+2 = 12 which is a multiple of 6
        
        >>> minimum(13, 4)
        1
        # 13-1 = 12 which is a multiple of 4
        
        >>> minimum(24, 8)
        0
        # 24 is already a multiple of 8
    """
    # Handle special case where a is already a multiple of x
    if a % x == 0:
        return 0
    
    # Find the nearest multiple of x below a
    lower_multiple = (a // x) * x
    
    # Find the nearest multiple of x above a
    upper_multiple = lower_multiple + x
    
    # Calculate distances to the multiples
    distance_down = a - lower_multiple
    distance_up = upper_multiple - a
    
    # Return the smaller of the two distances
    return min(distance_down, distance_up)


# Driver code to test the function
if __name__ == "__main__":
    # Test cases
    test_cases = [
        (10, 6, 2),    # Example from the problem statement
        (13, 4, 1),    # 13-1=12 is a multiple of 4
        (24, 8, 0),    # Already a multiple
        (0, 5, 0),     # 0 is a multiple of any number
        (7, 3, 1),     # 7+1=8 and 7-1=6, both work, return 1
        (15, 5, 0),    # Already a multiple
        (17, 9, 1),    # 17+1=18 is a multiple of 9
        (14, 7, 0),    # Already a multiple
        (20, 7, 1),    # 20+1=21 is a multiple of 7
        (100, 33, 1)   # 100-1=99 is a multiple of 33
    ]
    
    # Run tests and display results
    for a, x, expected in test_cases:
        result = minimum(a, x)
        print(f"minimum({a}, {x}) = {result}, Expected: {expected}, {'✓' if result == expected else '✗'}")
        
        # Verify the result actually works
        adjusted = a + result if (a + result) % x == 0 else a - result
        print(f"  {a} {'+ ' if adjusted > a else '- '}{result} = {adjusted}, divisible by {x}: {adjusted % x == 0}")
        print()
