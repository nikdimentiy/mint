def first_non_repeating_letter(string):
    """
    Returns the first non-repeating letter in the given string.
    
    Args:
    string (str): The input string to search for non-repeating letters.
    
    Returns:
    str: The first non-repeating letter, or an empty string if all letters repeat.
    """
    # Convert the string to lowercase to handle case insensitivity
    string_lower = string.lower()
    
    # Iterate through each letter in the string
    for i, letter in enumerate(string_lower):
        # Check if the count of the letter in the string is 1
        if string_lower.count(letter) == 1:
            # Return the original letter from the input string
            return string[i]
    
    # If no non-repeating letter is found, return an empty string
    return ""

# Driver code to test the function
if __name__ == "__main__":
    test_strings = [
        "sTreSS",      # 'T' is the first non-repeating letter
        "aabbcc",      # No non-repeating letters
        "aAbBcC",      # 'A' is the first non-repeating letter
        "swiss",       # 'w' is the first non-repeating letter
        "repeater",    # 'r' is the first non-repeating letter
        "",            # Empty string should return ''
        "a"           # Single character should return 'a'
    ]
    
    for test in test_strings:
        result = first_non_repeating_letter(test)
        print(f"First non-repeating letter in '{test}': '{result}'")
