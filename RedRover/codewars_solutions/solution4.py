def who_ate_cookie(input_value: any) -> str:
    """
    This function determines who ate the last cookie based on the input value.
    If the input is a string, it returns 'Zach'.
    If the input is an integer or float, it returns 'Monica'.
    If the input is any other type, it returns 'the dog'.

    Args:
        input_value (any): The input value to determine the eater.

    Returns:
        str: A string indicating who ate the last cookie.
    """
    if type(input_value) == str:
        eater = "Zach"
    elif type(input_value) == int or type(input_value) == float:
        eater = "Monica"
    else:
        eater = "the dog"
    
    return f"Who ate the last cookie? It was {eater}!"

# Example usage:
print(who_ate_cookie("hi"))      # Output: Who ate the last cookie? It was Zach!
print(who_ate_cookie(3.14))      # Output: Who ate the last cookie? It was Monica!
print(who_ate_cookie([1, 2, 3])) # Output: Who ate the last cookie? It was the dog!
print(who_ate_cookie(True))     # Output: Who ate the last cookie? It was the dog!

# Driver code with boolean inputs
print(who_ate_cookie(True))     # Output: Who ate the last cookie? It was the dog!
print(who_ate_cookie(False))    # Output: Who ate the last cookie? It was the dog!