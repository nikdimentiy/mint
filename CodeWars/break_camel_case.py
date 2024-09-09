def solution(s):
    """
    Breaks up camel casing in a given string by inserting a space before each uppercase letter.

    Args:
    s (str): The input string in camel case.

    Returns:
    str: The modified string with spaces inserted before uppercase letters.
    """
    # Use a list comprehension to iterate through each character in the string
    # If the character is uppercase, prepend it with a space; otherwise, keep it as is
    return "".join([" " + c if c.isupper() else c for c in s])

# Driver code to test the solution
if __name__ == "__main__":
    test_strings = [
        "camelCase",
        "breakCamelCase",
        "thisIsATestString",
        "anotherExampleHere",
        "singleword",
        "AlreadyHasSpaces"
    ]

    for test in test_strings:
        result = solution(test)
        print(f"Input: '{test}' => Output: '{result}'")
