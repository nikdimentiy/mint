def double_char(s):
    """
    Returns a new string where each character in the input string is repeated twice.

    Args:
        s (str): The input string to be processed.

    Returns:
        str: A new string with each character from the input string repeated.
    """
    # Use a list comprehension to create a list of characters, each repeated twice
    return "".join([c * 2 for c in s])

# Driver code to test the double_char function
if __name__ == "__main__":
    # Test cases
    test_strings = [
        "String",
        "Hello World",
        "1234!_ "
    ]
    
    for test in test_strings:
        result = double_char(test)
        print(f'double_char("{test}") ==> "{result}"')
