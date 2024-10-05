def descending_order(num):
    """
    Rearranges the digits of a given non-negative integer in descending order.

    Parameters:
    num (int): A non-negative integer whose digits are to be rearranged.

    Returns:
    int: A new integer formed by the digits of the input integer arranged in descending order.
    """
    # Convert the number to a string to access its digits
    # Sort the digits in reverse order (descending)
    # Join the sorted digits back into a string and convert it to an integer
    return int("".join(sorted([digit for digit in str(num)], reverse=True)))

# Driver code to test the function
if __name__ == "__main__":
    # Test cases
    print(descending_order(42145))  # Expected output: 54421
    print(descending_order(145263))  # Expected output: 654321
    print(descending_order(123456789))  # Expected output: 987654321
    print(descending_order(0))  # Expected output: 0
    print(descending_order(1001))  # Expected output: 1100
