def narcissistic(value):
    """
    Check if a given positive integer is a Narcissistic (Armstrong) number.

    A Narcissistic number is a number that is equal to the sum of its own digits,
    each raised to the power of the number of digits.

    Parameters:
    value (int): A positive integer to check.

    Returns:
    bool: True if the number is Narcissistic, False otherwise.
    """
    # Convert the number to a string to iterate over its digits
    # Calculate the number of digits
    num_digits = len(str(value))
    
    # Calculate the sum of each digit raised to the power of the number of digits
    digit_power_sum = sum(int(x) ** num_digits for x in str(value))
    
    # Check if the sum is equal to the original number
    return value == digit_power_sum

# Driver code to test the function
if __name__ == "__main__":
    # Test cases
    print(narcissistic(153))  # Expected output: True (1^3 + 5^3 + 3^3 = 153)
    print(narcissistic(370))  # Expected output: True (3^3 + 7^3 + 0^3 = 370)
    print(narcissistic(371))  # Expected output: True (3^3 + 7^3 + 1^3 = 371)
    print(narcissistic(9474)) # Expected output: True (9^4 + 4^4 + 7^4 + 4^4 = 9474)
    print(narcissistic(123))  # Expected output: False (1^3 + 2^3 + 3^3 != 123)

