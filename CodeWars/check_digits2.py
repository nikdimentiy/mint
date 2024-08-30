def check_digit(n, i1, i2, d):
    """
    Check if a digit is present in a specified range of indices in a number.

    Parameters:
    n (int or str): The number in which to check for the digit.
    i1 (int): The starting index of the range (inclusive).
    i2 (int): The ending index of the range (inclusive).
    d (int or str): The digit to check for.

    Returns:
    bool: True if the digit is found within the specified range of indices, False otherwise.

    Example:
    >>> check_digit(123456, 1, 4, 3)
    True
    >>> check_digit(123456, 1, 4, 7)
    False
    """
    # Convert the digit to a string for comparison
    return str(d) in str(n)[min(i1, i2):max(i1, i2) + 1]

# Driver code to test the function
if __name__ == "__main__":
    # Test cases
    print(check_digit(123456, 1, 4, 3))  # Expected output: True
    print(check_digit(123456, 1, 4, 7))  # Expected output: False
    print(check_digit(9876543210, 0, 5, 5))  # Expected output: True
    print(check_digit(9876543210, 0, 5, 0))  # Expected output: False
    print(check_digit(12345, 2, 2, 4))  # Expected output: True
    print(check_digit(12345, 2, 3, 5))  # Expected output: True
