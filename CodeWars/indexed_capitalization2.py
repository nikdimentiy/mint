def capitalize(s, ind):
    """
    Capitalizes characters in a string at specified indices.
    
    Args:
        s (str): A lowercase string with no spaces.
        ind (list): A list of integer indices where characters should be capitalized.
                   Invalid indices (negative or beyond string length) are ignored.
    
    Returns:
        str: The input string with characters capitalized at the specified valid indices.
    
    Examples:
        >>> capitalize("abcdef", [1,2,5])
        'aBCdeF'
        >>> capitalize("abcdef", [1,2,5,100])
        'aBCdeF'
        >>> capitalize("python", [0,2,4])
        'PyThOn'
    """
    # Convert list of indices to set for O(1) lookup
    ind = set(ind)
    
    # Use list comprehension to build the result string:
    # - Enumerate gives us both index and character
    # - Uppercase if index is in our set, otherwise keep as is
    return ''.join(c.upper() if i in ind else c for i, c in enumerate(s))

# Driver code
if __name__ == "__main__":
    # Test case 1: Basic capitalization
    test1 = capitalize("abcdef", [1,2,5])
    print(f"Test 1: {test1}")  # Expected: aBCdeF
    
    # Test case 2: Index out of range
    test2 = capitalize("abcdef", [1,2,5,100])
    print(f"Test 2: {test2}")  # Expected: aBCdeF
    
    # Test case 3: Empty indices list
    test3 = capitalize("hello", [])
    print(f"Test 3: {test3}")  # Expected: hello
    
    # Test case 4: All valid indices
    test4 = capitalize("python", [0,1,2,3,4,5])
    print(f"Test 4: {test4}")  # Expected: PYTHON
