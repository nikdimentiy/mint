def get_middle(s):
    """
    Returns the middle character(s) of a given word.
    
    If the length of the word is odd, it returns the middle character.
    If the length of the word is even, it returns the two middle characters.
    
    Parameters:
    s (str): The input word (string) with length 0 < len(s) < 1000.
    
    Returns:
    str: The middle character(s) of the word.
    """
    # Calculate the index of the middle character
    i = (len(s) - 1) // 2
    
    # If the length of the string is odd, return the middle character
    # If the length is even, return the two middle characters
    return s[i:i+2] if len(s) % 2 == 0 else s[i]

# Driver code to test the function
if __name__ == "__main__":
    # Test cases
    print(get_middle("test"))      # Should return "es"
    print(get_middle("testing"))   # Should return "t"
    print(get_middle("middle"))    # Should return "dd"
    print(get_middle("A"))         # Should return "A"
    print(get_middle("abcde"))     # Should return "c"
    print(get_middle("abcdef"))    # Should return "cd"
