def valid_parentheses(string):
    """
    Determines if the order of parentheses in the given string is valid.

    A string of parentheses is considered valid if:
    - Every opening parenthesis '(' has a corresponding closing parenthesis ')'.
    - Parentheses are closed in the correct order.

    Args:
    string (str): The input string containing parentheses.

    Returns:
    bool: True if the parentheses are valid, False otherwise.
    """
    # Filter the string to only include parentheses
    string = "".join(ch for ch in string if ch in "()")
    
    # Continuously remove valid pairs of parentheses
    while "()" in string:
        string = string.replace("()", "")
    
    # If the string is empty, all parentheses were matched correctly
    return not string

# Driver code to test the function
if __name__ == "__main__":
    test_cases = [
        "()",              # Expected: True
        ")(()))",          # Expected: False
        "(",               # Expected: False
        "(())((()())())",  # Expected: True
        "(()",             # Expected: False
        "())",             # Expected: False
        "((()))",          # Expected: True
        "(()())",          # Expected: True
        "())(",            # Expected: False
        "((())())",        # Expected: True
    ]

    for i, test in enumerate(test_cases):
        result = valid_parentheses(test)
        print(f"Test case {i + 1}: '{test}' => {result}")
