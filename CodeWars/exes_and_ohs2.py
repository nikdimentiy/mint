def xo(s):
    """
    Check if a string has the same number of 'x's and 'o's, case insensitive.

    Args:
    s (str): The input string to check.

    Returns:
    bool: True if the number of 'x's and 'o's are the same, False otherwise.
    """
    # Initialize counters for 'x' and 'o'
    x_count, o_count = 0, 0

    # Iterate through each character in the string
    for i in s:
        # Count 'x' and 'X'
        if i == 'x' or i == 'X':
            x_count += 1
        # Count 'o' and 'O'
        elif i == 'o' or i == 'O':
            o_count += 1

    # Compare counts of 'x' and 'o'
    return x_count == o_count

# Driver code to test the function
if __name__ == "__main__":
    # Test cases
    print(xo("ooxx"))      # Expected: True
    print(xo("xooxx"))     # Expected: False
    print(xo("ooxXm"))     # Expected: True
    print(xo("zpzpzpp"))   # Expected: True (no 'x' or 'o')
    print(xo("zzoo"))      # Expected: False
    print(xo("xmnOm"))     # Expected: True
    print(xo("mmnbm"))     # Expected: True (no 'x' or 'o')
