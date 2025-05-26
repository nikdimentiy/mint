def dig_pow(n, p):
    """
    Determine if there exists a positive integer k such that the sum of the digits of n 
    raised to successive powers starting from p equals k times n.

    Parameters:
    n (int): A positive integer whose digits will be used in the calculation.
    p (int): The starting power for the first digit.

    Returns:
    int: The value of k if it exists, otherwise -1.
    """
    # Convert the number n to a string to iterate over its digits
    digits = str(n)
    
    # Calculate the sum of each digit raised to the power of (p + i)
    digit_powers_sum = sum(int(d) ** (p + i) for i, d in enumerate(digits))
    
    # Check if the sum is divisible by n
    if digit_powers_sum % n == 0:
        # If divisible, return the quotient which is k
        return digit_powers_sum // n
    else:
        # If not divisible, return -1
        return -1

# Driver code to test the function
if __name__ == "__main__":
    # Test cases
    print(dig_pow(89, 1))      # Expected output: 1
    print(dig_pow(695, 2))     # Expected output: 2
    print(dig_pow(46288, 3))   # Expected output: 51
    print(dig_pow(123, 1))     # Expected output: -1 (no such k exists)
    print(dig_pow(1, 5))       # Expected output: 1 (1^5 = 1 * 1)
