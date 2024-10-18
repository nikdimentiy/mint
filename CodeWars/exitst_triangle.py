def is_triangle(a, b, c):
    """
    Determine if three lengths can form a triangle.

    Parameters:
    a (float): Length of the first side.
    b (float): Length of the second side.
    c (float): Length of the third side.

    Returns:
    bool: True if the lengths can form a triangle, False otherwise.
    """
    # Check if any side length is less than or equal to zero
    if a <= 0 or b <= 0 or c <= 0:
        return False
    
    # Check the triangle inequality theorem
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

# Driver code to test the is_triangle function
if __name__ == "__main__":
    # Test cases
    test_cases = [
        (3, 4, 5),  # Valid triangle
        (1, 1, 2),  # Not a triangle
        (5, 5, 5),  # Valid triangle
        (0, 4, 5),  # Not a triangle (zero length)
        (-1, 2, 3), # Not a triangle (negative length)
        (2, 2, 3)   # Valid triangle
    ]

    for a, b, c in test_cases:
        result = is_triangle(a, b, c)
        print(f"Lengths {a}, {b}, {c} can form a triangle: {result}")
