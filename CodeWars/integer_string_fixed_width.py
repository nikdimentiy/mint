def solution(number, width):
    """
    Formats a number to a specified width by padding with leading zeros or truncating from the left.
    
    Args:
        number (int): The number to format
        width (int): The desired width of the resulting string
    
    Returns:
        str: A string representation of the number with exactly 'width' characters.
             If number's length is greater than width, returns the rightmost 'width' digits.
             If number's length is less than width, pads with leading zeros.
    
    Examples:
        >>> solution(123, 5)
        '00123'
        >>> solution(123, 2)
        '23'
        >>> solution(123, 3)
        '123'
    """
    # Convert the number to string for easier manipulation
    num_str = str(number)
    
    # If the number's length is greater than or equal to desired width
    # Return the rightmost 'width' characters
    if len(num_str) >= width:
        return num_str[-width:]
    # If the number's length is less than desired width
    # Pad with zeros on the left
    else:
        return "0"*(width-len(num_str)) + num_str

# Driver code
if __name__ == "__main__":
    # Test cases
    test_cases = [
        (123, 5),
        (123, 2),
        (123, 3),
        (54321, 3),
        (7, 3)
    ]
    
    for number, width in test_cases:
        result = solution(number, width)
        print(f"Number: {number}, Width: {width}, Result: '{result}'")
