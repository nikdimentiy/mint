def get_middle(s):
    """
    Returns the middle character(s) of a given word.
    
    If the length of the word is odd, it returns the middle character.
    If the length of the word is even, it returns the two middle characters.
    
    Parameters:
    s (str): A word (string) of length 0 < str < 1000.
    
    Returns:
    str: The middle character(s) of the word.
    """
    # Calculate the length of the string
    length = len(s)
    
    # Check if the length is odd
    if length % 2 != 0:
        # Return the middle character
        return s[length // 2]
    else:
        # Return the two middle characters
        return s[length // 2 - 1:length // 2 + 1]

# Driver code to test the function
if __name__ == "__main__":
    # Test cases
    print(get_middle("test"))      # Should return "es"
    print(get_middle("testing"))   # Should return "t"
    print(get_middle("middle"))    # Should return "dd"
    print(get_middle("A"))         # Should return "A"
    print(get_middle("example"))   # Should return "am"
    print(get_middle("abcdef"))    # Should return "cd"
