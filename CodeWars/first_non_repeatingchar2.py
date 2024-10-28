def first_non_repeating_letter(string):
    """
    Returns the first non-repeating letter in the given string.
    
    A letter is considered non-repeating if it appears exactly once in the string,
    ignoring case. If there are no non-repeating letters, the function returns an empty string.
    
    Parameters:
    string (str): The input string to search for non-repeating letters.
    
    Returns:
    str: The first non-repeating letter or an empty string if none exists.
    """
    # Create a list of characters that are non-repeating in the string
    singles = [i for i in string if string.lower().count(i.lower()) == 1]
    
    # Return the first non-repeating character if it exists, otherwise return an empty string
    return singles[0] if singles else ''

# Driver code to test the function
if __name__ == "__main__":
    test_strings = [
        "stress",        # Expected output: "t"
        "sTreSS",        # Expected output: "t"
        "aabbcc",        # Expected output: ""
        "aAbBcC",        # Expected output: ""
        "moon",          # Expected output: "n"
        "swiss",         # Expected output: "w"
        " ",             # Expected output: " "
        "",              # Expected output: ""
        "a",             # Expected output: "a"
        "abcabcde"      # Expected output: "d"
    ]
    
    for s in test_strings:
        result = first_non_repeating_letter(s)
        print(f"first_non_repeating_letter('{s}') = '{result}'")
