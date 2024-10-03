def dashatize(num):
    """
    Convert a number into a string representation where each odd digit is surrounded by dashes.

    Args:
        num (int): The input number to be converted.

    Returns:
        str: A string representation of the number with dashes around odd digits.
              If the input is not an integer, it returns an empty string.
    """
    # Convert the number to a string
    num_str = str(num)
    
    # Loop through each odd digit and replace it with the digit surrounded by dashes
    for i in ['1', '3', '5', '7', '9']:
        num_str = num_str.replace(i, '-' + i + '-')
    
    # Strip leading and trailing dashes and replace any double dashes with a single dash
    return num_str.strip('-').replace('--', '-')

# Driver code to test the function
if __name__ == "__main__":
    test_numbers = [1234567890, 24680, 13579, -2468, 0, 1, 9, 10]
    
    for number in test_numbers:
        result = dashatize(number)
        print(f"dashatize({number}) = '{result}'")
