def solve(a, b):
    """
    Returns a string containing the characters that are not common between the two input strings.

    The function takes two strings 'a' and 'b' and finds:
        - Characters in 'a' that are not present in 'b'
        - Characters in 'b' that are not present in 'a'
    and then concatenates these two sets of characters.

    Parameters:
        a (str): The first string.
        b (str): The second string.

    Returns:
        str: A new string with characters from 'a' (that are not in 'b') followed by
             characters from 'b' (that are not in 'a').

    Example:
        >>> solve("xyab", "xzca")
        'ybzc'
        Explanation:
            - Characters in "xyab" not in "xzca": 'yb'
            - Characters in "xzca" not in "xyab": 'zc'
            Combined result: 'ybzc'
    """
    # List comprehension to extract characters from 'a' that are not in 'b'
    uncommon_from_a = [c for c in a if c not in b]
    
    # List comprehension to extract characters from 'b' that are not in 'a'
    uncommon_from_b = [c for c in b if c not in a]
    
    # Concatenate the two lists and join to form the result string
    return "".join(uncommon_from_a + uncommon_from_b)

# Driver code to test the `solve()` function
if __name__ == "__main__":
    # Define test cases as tuples: (input_a, input_b, expected_output)
    test_cases = [
        ("xyab", "xzca", "ybzc"),
        ("abcdef", "defghi", "abcghi"),
        ("", "abc", "abc"),
        ("abc", "", "abc"),
        ("abc", "abc", "")
    ]

    # Run tests and print results
    for a, b, expected in test_cases:
        result = solve(a, b)
        print("solve({!r}, {!r}) = {!r} | Expected: {!r} | Test: {}".format(
            a, b, result, expected, "PASS" if result == expected else "FAIL"
        ))
