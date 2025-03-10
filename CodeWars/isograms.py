def is_isogram(string):
    """
    Determines whether a string is an isogram (contains no repeating letters).
    
    An isogram is a word or phrase without a repeating letter, regardless of case.
    The empty string is considered an isogram.
    
    Args:
        string (str): The string to check
        
    Returns:
        bool: True if the input is an isogram, False otherwise
        
    Examples:
        >>> is_isogram("Dermatoglyphics")
        True
        >>> is_isogram("aba")
        False
        >>> is_isogram("moOse")
        False
    """
    # Convert string to lowercase
    string_lower = string.lower()
    
    # Convert string to a set to remove duplicates and compare lengths
    # If the lengths are equal, there were no duplicate letters (isogram)
    # If the lengths are different, there were duplicate letters (not an isogram)
    return len(string) == len(set(string_lower))


# Driver code to test the function
if __name__ == "__main__":
    # Test cases
    test_cases = [
        ("", True),                     # Empty string is an isogram
        ("isogram", True),              # Simple isogram
        ("Dermatoglyphics", True),      # Longer isogram
        ("aba", False),                 # Contains repeating 'a'
        ("moOse", False),               # Contains repeating 'o' (case-insensitive)
        ("isIsogram", False),           # Contains repeating 'i' (case-insensitive)
        ("eleven", False),              # Contains repeating 'e'
        ("subdermatoglyphic", True),    # Longest English word isogram
        ("thumbscrew-japingly", True),  # Compound isogram with hyphen
        ("AlPhAbEt", False)             # Contains repeating 'a' with mixed case
    ]
    
    # Run tests and display results
    for word, expected in test_cases:
        result = is_isogram(word)
        print(f"is_isogram('{word}') = {result}, Expected: {expected}, {'✓' if result == expected else '✗'}")
