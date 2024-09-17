def char_to_ascii(string):
    """
    Convert a string into a dictionary of ASCII values for each unique alphabetic character.

    Args:
        string (str): The input string from which to extract characters.

    Returns:
        dict or None: A dictionary where the keys are unique alphabetic characters 
                      and the values are their corresponding ASCII values. 
                      Returns None if the input string is empty.
    """
    # Check if the input string is empty
    if len(string) == 0:
        return None
    
    # Create a dictionary comprehension to build the result
    return {c: ord(c) for c in string if c.isalpha()}

# Driver code to test the function
if __name__ == "__main__":
    test_string = "Hello, World!"
    result = char_to_ascii(test_string)
    print(f"Input String: '{test_string}'")
    print("ASCII Values:", result)

    # Test with an empty string
    empty_string = ""
    result_empty = char_to_ascii(empty_string)
    print(f"Input String: '{empty_string}'")
    print("ASCII Values:", result_empty)

    # Test with a string containing non-alphabetic characters
    mixed_string = "abc123!@#"
    result_mixed = char_to_ascii(mixed_string)
    print(f"Input String: '{mixed_string}'")
    print("ASCII Values:", result_mixed)
