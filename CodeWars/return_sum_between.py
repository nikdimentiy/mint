def get_sum(a, b):
    """
    Calculates the sum of all integers between a and b (inclusive).

    The function takes into account whether a is less than, equal to, or greater than b:
      - If a equals b, the function returns a (or b) as the sum.
      - If a is less than b, the function sums every integer from a to b.
      - If a is greater than b, the function sums every integer from b to a.

    Parameters:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The sum of all integers between a and b, inclusive.

    Examples:
        >>> get_sum(1, 3)
        6      # (1 + 2 + 3)
        >>> get_sum(3, 1)
        6      # (1 + 2 + 3) because the function handles a > b by swapping the range
        >>> get_sum(5, 5)
        5      # Single value

    """
    # Initialize sum result variable to 0.
    sum_result = 0

    # If both numbers are the same, return the number as the sum.
    if a == b:
        return a

    # If a is less than b, iterate from a to b (inclusive) and add each integer.
    if a < b:
        for i in range(a, b + 1):
            sum_result += i
        return sum_result

    # If a is greater than b, iterate from b to a (inclusive) and add each integer.
    if a > b:
        for i in range(b, a + 1):
            sum_result += i
        return sum_result

# Driver code to test the function with different example cases.
if __name__ == "__main__":
    test_cases = [
        (0, -1),  # a > b where a is zero and b is negative
        (1, 3),   # a < b
        (3, 1),   # a > b
        (5, 5)    # a equals b
    ]
    
    for a, b in test_cases:
        # Call the function get_sum with a and b.
        result = get_sum(a, b)
        print(f"The sum from {a} to {b} is: {result}")
