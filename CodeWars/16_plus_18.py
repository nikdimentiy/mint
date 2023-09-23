def add(a, b):
    """
    This function adds two integers represented as strings and returns their sum as an integer.

    Args:
    a (str): The first integer to be added.
    b (str): The second integer to be added.

    Returns:
    int: The sum of the two integers.

    Example:
    >>> add("123", "456")
    579
    >>> add("0", "789")
    789
    >>> add("999", "1")
    1000
    """

    # Initialize an empty string to store the result.
    s = ""

    # Perform addition digit by digit.
    carry = 0  # Initialize the carry to 0.
    while a or b or carry:
        # Extract the last digit from a and b, or use 0 if a or b is empty.
        digit_a = int(a[-1]) if a else 0
        digit_b = int(b[-1]) if b else 0

        # Calculate the sum of the digits and the carry from the previous step.
        total = digit_a + digit_b + carry

        # Update carry for the next iteration.
        carry = total // 10

        # Append the last digit of the total to the result string.
        s = str(total % 10) + s

        # Remove the last digit from a and b.
        a = a[:-1] if a else ""
        b = b[:-1] if b else ""

    # Convert the result string to an integer and return it.
    return int(s or '0')


# Driver code
if __name__ == "__main__":
    num1 = input("Enter the first integer: ")
    num2 = input("Enter the second integer: ")

    result = add(num1, num2)
    print("Sum:", result)
