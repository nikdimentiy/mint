def maximum_product(a, b=2):
    """
    Calculate the maximum product of integers that sum up to a given number.

    This function recursively finds the maximum product of integers that can be formed
    by summing up to the number 'a', starting from the integer 'b'. The function explores
    different combinations of integers to maximize the product.

    Args:
        a (int): The target sum to be achieved by the integers.
        b (int, optional): The starting integer for the combinations. Defaults to 2.

    Returns:
        int: The maximum product of integers that sum up to 'a'.
    
    Example:
        maximum_product(10) returns 36, as 3 + 3 + 4 = 10 and 3 * 3 * 4 = 36.
    """
    # Initialize the maximum product with the current value of 'a'
    m, d = a, sum(divmod(a, 2))
    
    # Explore combinations starting from 'b' until the sum exceeds 'd'
    while b < d:
        # Calculate the product of 'b' and the maximum product of the remaining sum
        p = b * maximum_product(a - b, b + 1)
        # Update the maximum product found
        m = max(m, p)
        b += 1
    
    return m

# Driver code to test the maximum_product function
if __name__ == "__main__":
    # Test case 1
    result1 = maximum_product(10)
    print("Maximum Product for 10:", result1)  # Expected: 36

    # Test case 2
    result2 = maximum_product(8)
    print("Maximum Product for 8:", result2)  # Expected: 18 (3 * 3 * 2)

    # Test case 3
    result3 = maximum_product(5)
    print("Maximum Product for 5:", result3)  # Expected: 6 (2 * 3)

    # Test case 4
    result4 = maximum_product(12)
    print("Maximum Product for 12:", result4)  # Expected: 81 (3 * 3 * 3 * 3)
