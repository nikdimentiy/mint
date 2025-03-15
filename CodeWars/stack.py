def check_bracket(string):  
    """  
    Check if the brackets in the provided string are balanced.  

    A string is considered to have balanced brackets if:  
    - Each opening bracket has a corresponding and correctly ordered closing bracket.  
    - There are no unmatched closing brackets.  

    Args:  
        string (str): The input string containing brackets.  

    Returns:  
        bool: True if the brackets are balanced, False otherwise.  
    """  
    # Initialize a pseudo stack to keep track of opening brackets  
    pseudo_stack = []  

    # Dictionary to map closing brackets to their corresponding opening brackets  
    bracket_dict = {  
        ')': '(',  
        ']': '[',  
        '}': '{',  
    }  

    # Iterate through each character in the string  
    for s in string:  
        # If the character is an opening bracket, push it onto the stack  
        if s in bracket_dict.values():  
            pseudo_stack.append(s)  
        else:  # If it's a closing bracket  
            # Check for unmatched closing brackets  
            if not pseudo_stack:  
                return False  
            else:  
                # Check if the last opening bracket matches the closing bracket  
                if pseudo_stack[-1] == bracket_dict.get(s):  
                    del pseudo_stack[-1]  # Remove the matched opening bracket  
                else:  
                    return False  # Mismatched brackets  

    # If the stack is empty, all brackets were matched; otherwise, they are not balanced  
    return False if pseudo_stack else True  


# Driver code to test the check_bracket function  
if __name__ == "__main__":  
    test_strings = [  
        "(([]))",     # Expected: True  
        "([{}])",     # Expected: True  
        "(((",        # Expected: False  
        "([]",        # Expected: False  
        "([)]",       # Expected: False  
        "()",         # Expected: True  
        "([{}])",     # Expected: True  
        "{[()]}[{}]", # Expected: True  
        "({[}])"      # Expected: False  
    ]  

    for test in test_strings:  
        result = check_bracket(test)  
        print(f"check_bracket({test}) = {result}")  
