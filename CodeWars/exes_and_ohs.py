def xo(s):
    """
    Check if a string has the same number of 'x's and 'o's.

    Args:
    s (str): The input string to check.

    Returns:
    bool: True if the number of 'x's and 'o's are the same, False otherwise.
          The check is case insensitive.
    """
    # Convert the string to lowercase to make the check case insensitive
    s_lower = s.lower()
    
    # Count the occurrences of 'x' and 'o' in the lowercase string
    count_x = s_lower.count("x")
    count_o = s_lower.count("o")
    
    # Return True if counts are equal, otherwise return False
    return count_x == count_o

# Driver code to test the function
if __name__ == "__main__":
    test_cases = [
        ("ooxx", True),
        ("xooxx", False),
        ("ooxXm", True),
        ("zpzpzpp", True),
        ("zzoo", False),
        ("", True),  # Edge case: empty string
        ("XxOo", True),  # Case insensitive check
        ("abc", True),  # No 'x' or 'o'
        ("xXoO", True),  # Equal counts with mixed case
    ]

    for s, expected in test_cases:
        result = xo(s)
        print(f"xo({s!r}) = {result}; Expected = {expected}; Test {'Passed' if result == expected else 'Failed'}")
