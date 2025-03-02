def alphanumeric(string):
    """
    Validate if a user input string is alphanumeric.
    
    A string is considered alphanumeric if:
    - It contains at least one character (empty strings are not valid)
    - It contains only uppercase/lowercase Latin letters (A-Z, a-z) and digits (0-9)
    - It has no whitespaces, underscores, or other special characters
    
    Args:
        string (str): The input string to validate
        
    Returns:
        bool: True if the string is alphanumeric, False otherwise
        
    Examples:
        >>> alphanumeric("Mazinkaiser")
        True
        >>> alphanumeric("hello world_")
        False
        >>> alphanumeric("PassW0rd")
        True
        >>> alphanumeric("")
        False
    """
    # The isalnum() method checks if all characters in the string are alphanumeric
    # (consists of only letters A-Z, a-z and digits 0-9)
    # It returns False if the string is empty or contains any non-alphanumeric characters
    # like spaces, symbols, or underscores
    return string.isalnum()

# Driver code to test the function
if __name__ == "__main__":
    test_cases = [
        # Valid alphanumeric strings
        "Mazinkaiser",  # Letters only
        "PassW0rd",     # Letters and numbers
        "123",          # Numbers only
        "a",            # Single letter
        "7",            # Single digit
        
        # Invalid cases
        "",             # Empty string
        "hello world",  # Contains space
        "hello_world",  # Contains underscore
        "hello!",       # Contains special character
        "hello\tworld", # Contains tab
        "hello\nworld", # Contains newline
        "résumé"        # Contains non-Latin letters
    ]
    
    for test in test_cases:
        result = alphanumeric(test)
        if result:
            status = "Valid"
        else:
            status = "Invalid"
        print(f"'{test}' -> {result} ({status})")
