def heron(a, b, c):
    """
    Calculate the area of a triangle using Heron's formula.
    
    Heron's formula determines the area of a triangle when the lengths 
    of all three sides are known. The formula uses the semi-perimeter 
    and the side lengths to compute the area.
    
    Args:
        a (float): Length of the first side of the triangle
        b (float): Length of the second side of the triangle
        c (float): Length of the third side of the triangle
    
    Returns:
        float: Area of the triangle, rounded to 2 decimal places
    
    Raises:
        ValueError: If the given side lengths cannot form a valid triangle
    
    Formula:
        1. Calculate semi-perimeter s = (a + b + c) / 2
        2. Area = sqrt(s * (s-a) * (s-b) * (s-c))
    
    Example:
        >>> heron(3, 4, 5)
        6.0
        >>> heron(6, 8, 10)
        24.0
    """
    # Validate triangle inequality theorem
    # Sum of any two sides must be greater than the third side
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        raise ValueError("Invalid triangle: Side lengths cannot form a triangle")
    
    # Calculate semi-perimeter
    s = (a + b + c) / 2.0
    
    # Calculate area using Heron's formula
    # Using ** 0.5 for square root calculation
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    
    # Round the area to 2 decimal places
    return round(area, 2)

# Driver code to demonstrate the function
if __name__ == "__main__":
    # Test cases
    try:
        # Valid triangles
        print("Area of triangle (3,4,5):", heron(3, 4, 5))    # Expected: 6.0
        print("Area of triangle (6,8,10):", heron(6, 8, 10))  # Expected: 24.0
        print("Area of triangle (5,5,5):", heron(5, 5, 5))    # Expected: 10.83
        
        # Invalid triangle (should raise ValueError)
        print("Invalid triangle (1,2,3):", heron(1, 2, 3))
    
    except ValueError as e:
        print(f"Error: {e}")
