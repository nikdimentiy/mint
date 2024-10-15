def double_char(s):
    """
    This function takes a string as input and returns a new string 
    where each character in the original string is repeated twice.
    
    Parameters:
    s (str): The input string to be processed.
    
    Returns:
    str: A new string with each character from the input string repeated.
    
    Examples:
    >>> double_char("String")
    'SSttrriinngg'
    
    >>> double_char("Hello World")
    'HHeelllloo  WWoorrlldd'
    
    >>> double_char("1234!_ ")
    '11223344!!__  '
    """
    # Initialize an empty string to store the result
    res = ''
    
    # Iterate over each character in the input string
    for i in s:
        # Append the character twice to the result string
        res += i * 2
    
    # Return the final result string
    return res

# Driver code to test the function
if __name__ == "__main__":
    # Test cases
    print(double_char("String"))      # Expected output: "SSttrriinngg"
    print(double_char("Hello World"))  # Expected output: "HHeelllloo  WWoorrlldd"
    print(double_char("1234!_ "))      # Expected output: "11223344!!__  "
