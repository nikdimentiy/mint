def valid_parentheses(string):
    """
    Check if the given string has valid parentheses.

    A string is considered to have valid parentheses if each opening parenthesis '('
    has a corresponding closing parenthesis ')' in the correct order, and no closing
    parenthesis occurs before its matching opening parenthesis.

    Parameters:
        string (str): The string to be checked for valid parentheses.

    Returns:
        bool: True if the parentheses are valid, False otherwise.

    Examples:
        >>> valid_parentheses("()")
        True
        >>> valid_parentheses("(()())")
        True
        >>> valid_parentheses(")(")
        False
        >>> valid_parentheses("((()")
        False
    """
    # Initialize a counter to simulate a stack
    stack = 0
    
    # Iterate through each character in the input string
    for c in string:
        # When an opening parenthesis is encountered, increment the counter
        if c == '(':
            stack += 1
        # When a closing parenthesis is encountered, decrement the counter
        elif c == ')':
            stack -= 1
        
        # If the counter falls below zero, there are more closing parentheses than opening ones
        if stack < 0:
            return False
    
    # Return True only if all opening parentheses have been matched (counter is 0)
    return stack == 0

# Driver code to test the function with example inputs
if __name__ == "__main__":
    test_strings = [
        "()",            # Simple valid parentheses
        "(()())",        # Nested valid parentheses
        ")( ",           # Starts with closing parenthesis which is invalid
        "((()",          # More opening than closing parentheses
        "",              # Empty string should be considered valid
        "(a+b)*(c-d)"    # Mixed content with valid parentheses (ignores non-parenthesis characters)
    ]

    for test in test_strings:
        result = valid_parentheses(test)
        print(f"String: {test!r:15} -> Valid: {result}")
