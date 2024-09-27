def char_to_ascii(s):
    """
    Convert a string into a dictionary of ASCII values for its unique alphabetic characters.

    Args:
    s (str): The input string from which to extract characters.

    Returns:
    dict: A dictionary where the keys are unique alphabetic characters from the string,
          and the values are their corresponding ASCII values. Returns None if the input string is empty.
    """
    # Check if the input string is empty
    if s:
        # Create a dictionary comprehension to build the result
        return {c: ord(c) for c in set(s) if c.isalpha()}
    else:
        # Return None for an empty string
        return None

# Driver code to test the function
if __name__ == "__main__":
    test_string = "Hello, World!"
    result = char_to_ascii(test_string)
    print(f"Input String: '{test_string}'")
    print("ASCII Values:", result)

    empty_string = ""
    result_empty = char_to_ascii(empty_string)
    print(f"Input String: '{empty_string}'")
    print("ASCII Values:", result_empty)
