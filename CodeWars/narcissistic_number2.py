def narcissistic(value):
    """
    Check if a number is a Narcissistic (Armstrong) number.

    A Narcissistic number is a positive number that is equal to the sum of its own digits,
    each raised to the power of the number of digits in the number.

    For example, 153 is a Narcissistic number because:
    1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153

    Parameters:
    value (int): The number to be checked.

    Returns:
    bool: True if the number is Narcissistic, False otherwise.
    """
    
    # Convert the number to a string to easily iterate over its digits
    value_str = str(value)
    size = len(value_str)  # Get the number of digits
    total_sum = 0          # Initialize the sum of the powered digits

    # Iterate over each digit in the string representation of the number
    for digit in value_str:
        # Raise the digit to the power of the number of digits and add to the total sum
        total_sum += int(digit) ** size

    # Check if the total sum equals the original number
    return total_sum == value

# Driver code to test the function
if __name__ == "__main__":
    test_numbers = [
        153,      # Expected output: True (1^3 + 5^3 + 3^3 = 153)
        370,      # Expected output: True (3^3 + 7^3 + 0^3 = 370)
        371,      # Expected output: True (3^3 + 7^3 + 1^3 = 371)
        9474,     # Expected output: True (9^4 + 4^4 + 7^4 + 4^4 = 9474)
        123,      # Expected output: False (1^3 + 2^3 + 3^3 != 123)
        10,       # Expected output: False (1^2 + 0^2 != 10)
        0,        # Expected output: False (0 is not a positive number)
        1,        # Expected output: True (1^1 = 1)
        2,        # Expected output: True (2^1 = 2)
    ]

    for number in test_numbers:
        print(f"{number} is Narcissistic: {narcissistic(number)}")
