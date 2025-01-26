def valid_parentheses(string):  
    """  
    Check if the input string has valid parentheses.  

    A string is considered valid if:  
    - Every opening parenthesis '(' has a corresponding closing parenthesis ')'.  
    - Parentheses are closed in the correct order.  

    Args:  
        string (str): The input string containing parentheses.  

    Returns:  
        bool: True if the parentheses are valid, False otherwise.  
    """  
    cnt = 0  # Initialize a counter to track the balance of parentheses  
    for char in string:  
        if char == '(':  
            cnt += 1  # Increment the counter for an opening parenthesis  
        if char == ')':  
            cnt -= 1  # Decrement the counter for a closing parenthesis  
        if cnt < 0:  
            return False  # If the counter is negative, there are unmatched closing parentheses  
    return cnt == 0  # Return True if all parentheses are matched, False otherwise  

# Driver code to test the function  
if __name__ == "__main__":  
    test_strings = [  
        "()",          # Valid  
        "(())",        # Valid  
        "(()())",      # Valid  
        "(()",         # Invalid  
        "())",         # Invalid  
        "((()))",      # Valid  
        "(()))(",      # Invalid  
        "((())())",    # Valid  
        "())(()",      # Invalid  
        "((())())()",  # Valid  
    ]  

    for s in test_strings:  
        result = valid_parentheses(s)  
        print(f"'{s}': {result}")
