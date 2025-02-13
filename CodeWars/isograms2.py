def is_isogram(string):
    """
    Determine if a given string is an isogram (has no repeating letters).
    
    An isogram is a word or phrase without a repeating letter. The same letter in 
    different cases (uppercase/lowercase) is considered a repeat. Empty strings 
    are considered isograms.
    
    Args:
        string (str): The string to check. Can contain any characters, but only
                     letters are checked for repetition.
    
    Returns:
        bool: True if the string is an isogram, False otherwise
        
    Examples:
        >>> is_isogram("Dermatoglyphics")
        True
        >>> is_isogram("aba")
        False
        >>> is_isogram("moOse")  # Case-insensitive
        False
        >>> is_isogram("")  # Empty string is valid
        True
    """
    # Convert string to lowercase for case-insensitive comparison
    string = string.lower()
    
    # Create dictionary counting occurrences of each letter
    letters = {letter: string.count(letter) for letter in string}
    
    # Check if all letters appear exactly once or string is empty
    if set(letters.values()) == {1} or set(letters.values()) == set():
        return True
    else:
        return False

def test_is_isogram():
    """
    Test suite for the is_isogram function.
    """
    # Test cases as tuples of (input, expected_output)
    test_cases = [
        ("Dermatoglyphics", True),  # Classic isogram
        ("aba", False),             # Simple repeating letter
        ("moOse", False),           # Case-insensitive repeat
        ("", True),                 # Empty string
        ("isogram", True),          # Another valid isogram
        ("eleven", False),          # Multiple repeating letters
        ("thumbscrew", True),       # Valid isogram
        ("alphabet", True),         # Valid isogram
        ("thumbscrews", False),     # Repeating 's'
        ("background", True),       # Valid isogram
        ("downstream", True),       # Valid isogram
        ("six-year-old", True),     # Isogram with hyphens
    ]
    
    # Run all test cases
    for test_string, expected in test_cases:
        result = is_isogram(test_string)
        status = "✓ PASS" if result == expected else "✗ FAIL"
        print(f"{status} - Input: '{test_string}'")
        print(f"    Expected: {expected}, Got: {result}")

if __name__ == "__main__":
    print("Running isogram checker tests...\n")
    test_is_isogram()

# Alternative implementation (more efficient):
def is_isogram_alt(string):
    """
    Alternative implementation using set comparison.
    This version is more efficient for longer strings.
    """
    string = string.lower()
    # Compare length of string with length of unique characters
    return len(string) == len(set(string))
