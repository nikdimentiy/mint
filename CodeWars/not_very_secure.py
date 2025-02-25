def alphanumeric(password):
    """
    Validates if a given password string is alphanumeric.
    
    The string is considered alphanumeric if it meets the following conditions:
    - Contains at least one character (empty strings are invalid)
    - Contains only uppercase/lowercase Latin letters and digits 0-9
    - Contains no whitespaces or special characters
    
    Args:
        password (str): The input string to be validated
        
    Returns:
        bool: True if the string is alphanumeric, False otherwise
        
    Raises:
        TypeError: If the input is not a string
    """
    # Check if the password contains any whitespace
    # and ensure all characters are alphanumeric
    return (
        " " not in password and 
        len([c for c in password if c.isdigit() or c.isalpha()]) == len(password) and 
        len(password) > 0
    )

# Driver code to test the function
if __name__ == "__main__":
    test_cases = [
        ("Password123", True),                  # Valid alphanumeric string
        ("Password 123", False),                 # Contains whitespace
        ("Password_123", False),                 # Contains underscore
        ("Password!", False),                   # Contains special character
        ("123", True),                          # Valid numeric string
        ("password", True),                     # Valid alphabetic string
        ("", False),                            # Empty string
        ("    ", False)                         # String with only spaces
    ]
    
    for test_string, expected_result in test_cases:
        result = alphanumeric(test_string)
        print(f"Test: {test_string!r} | Expected: {expected_result} | Actual: {result}")
