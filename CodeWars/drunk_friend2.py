def parse_character(char):
    """
    Parse a single character and return its 'decoded' counterpart.
    
    For uppercase letters (A-Z), it returns the character that is 
    symmetrically opposite in the alphabet (A <-> Z, B <-> Y, etc.).
    
    For lowercase letters (a-z), it does the same (a <-> z, b <-> y, etc.).
    
    Any non-alphabetic character is returned unchanged.
    
    Args:
        char (str): A single character to be parsed.
    
    Returns:
        str: The decoded character.
    """
    if 65 <= ord(char) <= 90:  # Check if the character is uppercase
        return chr(155 - ord(char))  # Decode uppercase letters
    elif 97 <= ord(char) <= 122:  # Check if the character is lowercase
        return chr(219 - ord(char))  # Decode lowercase letters
    else:
        return char  # Return non-alphabetic characters unchanged


def decode(string_):
    """
    Decode a string by parsing each character using the parse_character function.
    
    This function transforms each letter in the string to its opposite letter 
    in the alphabet while leaving non-alphabetic characters unchanged.
    
    Args:
        string_ (str): The string to be decoded.
    
    Returns:
        str: The decoded string or an error message if the input is not a string.
    """
    if not isinstance(string_, str):
        return "Input is not a string"  # Return error message for non-string input
    return "".join(map(parse_character, string_))  # Decode the string


# Driver code to demonstrate the functionality
if __name__ == "__main__":
    test_string = "Hello, World! zYx"
    decoded_string = decode(test_string)
    print(f"Original string: {test_string}")
    print(f"Decoded string: {decoded_string}")
