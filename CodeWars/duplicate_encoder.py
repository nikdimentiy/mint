def duplicate_encode(word):
    """
    Convert a string to a new string where each character is represented as:
    - "(" if the character appears only once in the original string,
    - ")" if the character appears more than once in the original string.
    
    The function ignores capitalization when determining if a character is a duplicate.

    Parameters:
    word (str): The input string to be processed.

    Returns:
    str: A new string with characters encoded as described above.
    """
    # Convert the input word to lowercase and iterate through each character
    return "".join(["(" if word.lower().count(l) == 1 else ")" for l in word.lower()])

# Driver code to test the function
if __name__ == "__main__":
    test_cases = [
        "din",      # Expected output: "((("
        "recede",   # Expected output: "()()()"
        "Success",  # Expected output: ")())())"
        "(( @",     # Expected output: "))(("
    ]

    for test in test_cases:
        result = duplicate_encode(test)
        print(f"duplicate_encode('{test}') = '{result}'")
