def check_digit(number, index1, index2, digit):
    """
    Check if a specified digit is present in a substring of a given number.

    Parameters:
    number (int or str): The number in which to search for the digit.
    index1 (int): The starting index of the substring (inclusive).
    index2 (int): The ending index of the substring (inclusive).
    digit (int): The digit to search for within the specified substring.

    Returns:
    bool: True if the digit is found in the specified substring, False otherwise.
    
    Note:
    The function checks the substring from index1 to index2 and also from index2 to index1,
    allowing for both ascending and descending index ranges.
    """
    # Convert the digit to a string for comparison
    digit_str = str(digit)
    
    # Convert the number to a string to facilitate substring extraction
    number_str = str(number)
    
    # Check if the digit is in the substring defined by index1 and index2
    return digit_str in number_str[index1:index2 + 1] or digit_str in number_str[index2:index1 + 1]

# Driver code to test the function
if __name__ == "__main__":
    # Test cases
    number = 123456789
    index1 = 2
    index2 = 5
    digit = 4

    # Check if the digit is present in the specified range
    result = check_digit(number, index1, index2, digit)
    print(f"Is digit {digit} present in number {number} between indices {index1} and {index2}? {result}")

    # Another test case
    digit = 0
    result = check_digit(number, index1, index2, digit)
    print(f"Is digit {digit} present in number {number} between indices {index1} and {index2}? {result}")

    # Test with reversed indices
    index1 = 5
    index2 = 2
    digit = 3
    result = check_digit(number, index1, index2, digit)
    print(f"Is digit {digit} present in number {number} between indices {index1} and {index2}? {result}")
