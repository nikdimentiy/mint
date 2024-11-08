def valid_parentheses(string):
    """
    Determines if the order of parentheses in the given string is valid.

    A string of parentheses is considered valid if:
    1. Every opening parenthesis '(' has a corresponding closing parenthesis ')'.
    2. The parentheses are closed in the correct order.

    Args:
        string (str): The string containing parentheses to be checked.

    Returns:
        bool: True if the parentheses are valid, False otherwise.
    """
    # Initialize a counter for the balance of parentheses
    balance = 0
    
    # Loop through each character in the string
    for char in string:
        # If the character is an opening parenthesis, increase the balance by 1
        if char == "(":
            balance += 1
        # If the character is a closing parenthesis, decrease the balance by 1
        elif char == ")":
            balance -= 1
        
        # If the balance becomes negative at any point, return false
        if balance < 0:
            return False
    
    # If the balance is zero at the end, return true (valid parentheses)
    return balance == 0

# Driver code to test the function
if __name__ == "__main__":
    test_cases = [
        "()",              # Expected: True
        ")(()))",          # Expected: False
        "(",               # Expected: False
        "(())((()())())",  # Expected: True
        "(()())",          # Expected: True
        "())",             # Expected: False
        "((()))",          # Expected: True
        "(()",             # Expected: False
        "())(",            # Expected: False
        "",                # Expected: True (empty string is valid)
    ]

    for test in test_cases:
        result = valid_parentheses(test)
        print(f"valid_parentheses({test!r}) = {result}")
