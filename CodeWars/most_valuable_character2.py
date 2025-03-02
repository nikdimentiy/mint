def solve(st):
    """
    Find the most valuable character in a string.
    
    The value of a character is the difference between the index of its last occurrence 
    and the index of its first occurrence (a negative number since rfind returns the last
    occurrence index). The character with the highest absolute difference has the highest value.
    
    If there is a tie in values, return the lexicographically lowest character.
    
    Args:
        st (str): The input string (all lowercase)
        
    Returns:
        str: The character with the highest value or the lexicographically 
             lowest in case of a tie
    
    Examples:
        >>> solve('a')
        'a'
        >>> solve('ab')
        'a'
        >>> solve('axyzxyz')
        'x'
    """
    # Create a list of tuples (value, character) for each unique character in the string
    # Note: st.find() returns the first occurrence index
    #       st.rfind() returns the last occurrence index
    #       The difference is negative because rfind will be larger than find
    #       Smaller (more negative) difference means higher character value
    char_values = [(st.find(c) - st.rfind(c), c) for c in set(st)]
    
    # Sort by value (primary) and character (secondary)
    # Since the differences are negative, the smallest value represents the largest span
    # When values are tied, sorted() uses the character for comparison (lexicographical order)
    sorted_values = sorted(char_values)
    
    # Return the character with the highest value (first item from sorted list)
    return sorted_values[0][1]

# Driver code to test the function
if __name__ == "__main__":
    test_cases = [
        "a",           # Expected: 'a'
        "ab",          # Expected: 'a'
        "axyzxyz",     # Expected: 'x'
        "aabccc",      # Expected: 'c'
        "pneumonoultramicroscopicsilicovolcanoconiosis",  # Test with a long word
        "abcdefghijklmnopqrstuvwxyz",  # Test with all letters
        "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba"  # Test with a palindrome-like pattern
    ]
    
    for test in test_cases:
        result = solve(test)
        print(f"solve('{test}') = '{result}'")
