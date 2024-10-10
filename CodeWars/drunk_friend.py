def decode(string_):
    """
    Decodes a given string by reversing the alphabet. 
    Each letter is replaced by its counterpart from the opposite end of the alphabet:
    'a' becomes 'z', 'b' becomes 'y', etc. Non-alphabetic characters remain unchanged.

    Parameters:
    string_ (str): The input string to be decoded.

    Returns:
    str: The decoded string or an error message if the input is not a string.
    """
    # Check if the input is a string
    if type(string_) != str:
        return 'Input is not a string'
    
    # Define the alphabet
    letters = "abcdefghijklmnopqrstuvwxyz"
    translate = ""  # Initialize an empty string for the translated result

    # Iterate through each character in the input string
    for l in string_:
        ind = letters.find(l.lower())  # Find the index of the letter in the alphabet
        if l.isalpha() and l.islower():  # Check if the letter is lowercase
            translate += letters[::-1][ind]  # Append the corresponding reversed letter
        elif l.isalpha() and l.isupper():  # Check if the letter is uppercase
            translate += letters[::-1][ind].upper()  # Append the corresponding reversed letter in uppercase
        else:
            translate += l  # Append non-alphabetic characters unchanged

    return translate  # Return the final decoded string

# Driver code to test the decode function
if __name__ == "__main__":
    test_strings = [
        "Hello, World!",  # Mixed case with punctuation
        "abcxyz",         # Lowercase letters
        "ABCXYZ",         # Uppercase letters
        "12345",          # Numbers only
        "aBc123!@#",      # Mixed case with numbers and symbols
        12345             # Non-string input
    ]

    for test in test_strings:
        result = decode(test)
        print(f"Input: {test} => Decoded: {result}")
