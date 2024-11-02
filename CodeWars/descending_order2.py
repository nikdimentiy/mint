def descending_order(num):
    """
    Rearranges the digits of a given integer in descending order.

    Parameters:
    num (int): The integer whose digits are to be rearranged.

    Returns:
    int: An integer formed by the digits of the input integer arranged in descending order.
    """
    # Convert the number to a string to access its digits
    # Sort the digits in reverse order and join them back into a string
    # Convert the resulting string back to an integer
    return int(''.join(sorted(str(num), reverse=True)))

# Driver code to test the function
if __name__ == "__main__":
    # Test cases
    test_numbers = [42145, 145263, 123456789, 0, 987654321]
    
    for number in test_numbers:
        result = descending_order(number)
        print(f"Descending order of {number} is {result}")

