def solve(a, b):
    """
    Find characters that are not common between two strings.
    
    This function identifies characters that appear in only one of the two input
    strings and returns them concatenated. Characters from the first string
    are returned first, followed by characters from the second string.
    
    Args:
        a (str): The first input string
        b (str): The second input string
    
    Returns:
        str: A string containing all characters that appear in only one of the
             two input strings. Characters from string 'a' come first, followed
             by characters from string 'b'.
    
    Example:
        >>> solve("xyab", "xzca")
        'ybzc'
        >>> solve("abcd", "xyz")
        'abcdxyz'
        >>> solve("xxx", "xzca")
        'zca'
    """
    # Find the set of characters common to both strings using set intersection
    s = set(a) & set(b)
    
    # Concatenate both strings and filter out common characters
    # The order is preserved: first characters from 'a', then from 'b'
    return ''.join(c for c in a+b if c not in s)


# Driver code to test the function
if __name__ == "__main__":
    # Test case 1: Example from the problem statement
    test1_a, test1_b = "xyab", "xzca"
    result1 = solve(test1_a, test1_b)
    print(f"Test 1: solve('{test1_a}', '{test1_b}') -> '{result1}'")  # Expected: 'ybzc'
    
    # Test case 2: No common characters
    test2_a, test2_b = "abcd", "xyz"
    result2 = solve(test2_a, test2_b)
    print(f"Test 2: solve('{test2_a}', '{test2_b}') -> '{result2}'")  # Expected: 'abcdxyz'
    
    # Test case 3: All characters from first string are in second string
    test3_a, test3_b = "abc", "abcdef"
    result3 = solve(test3_a, test3_b)
    print(f"Test 3: solve('{test3_a}', '{test3_b}') -> '{result3}'")  # Expected: 'def'
    
    # Test case 4: All characters from second string are in first string
    test4_a, test4_b = "abcdef", "abc"
    result4 = solve(test4_a, test4_b)
    print(f"Test 4: solve('{test4_a}', '{test4_b}') -> '{result4}'")  # Expected: 'def'
    
    # Test case 5: Repeated characters
    test5_a, test5_b = "xxx", "xzca"
    result5 = solve(test5_a, test5_b)
    print(f"Test 5: solve('{test5_a}', '{test5_b}') -> '{result5}'")  # Expected: 'zca'
    
    # Test case 6: Empty strings
    test6_a, test6_b = "", "abc"
    result6 = solve(test6_a, test6_b)
    print(f"Test 6: solve('{test6_a}', '{test6_b}') -> '{result6}'")  # Expected: 'abc'
