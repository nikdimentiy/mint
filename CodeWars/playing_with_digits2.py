def dig_pow(n, p):
    """
    Calculate the integer k such that the sum of the digits of n raised to successive powers
    starting from p equals k times n.

    Given a positive integer n and a positive integer p, the function checks if there exists
    a positive integer k such that:

    (a^p + b^(p+1) + c^(p+2) + d^(p+3) + ...) = n * k

    where a, b, c, d are the digits of n. If such a k exists, the function returns k; otherwise, it returns -1.

    Parameters:
    n (int): The positive integer whose digits will be used.
    p (int): The starting power for the first digit.

    Returns:
    int: The value of k if it exists, otherwise -1.
    """
    # Convert the number to a string to iterate over each digit
    digits = str(n)
    digit_powers_sum = 0  # Initialize the sum of digit powers

    # Iterate over each digit and its corresponding power
    for i, d in enumerate(digits):
        # Calculate the power of the digit and add it to the sum
        digit_powers_sum += int(d) ** (p + i)

    # Check if the sum of powers is divisible by n
    if digit_powers_sum % n == 0:
        # Return the quotient as k
        return digit_powers_sum // n
    else:
        # Return -1 if no such k exists
        return -1

# Driver code to test the function
if __name__ == "__main__":
    # Test cases
    print(dig_pow(89, 1))      # Expected output: 1
    print(dig_pow(695, 2))     # Expected output: 2
    print(dig_pow(46288, 3))   # Expected output: 51
    print(dig_pow(123, 1))     # Expected output: -1 (no such k exists)
    print(dig_pow(1, 5))       # Expected output: 1 (1^5 = 1 * 1)
