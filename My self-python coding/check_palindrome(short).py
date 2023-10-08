import string

def is_palindrome(s):
    """
    Check if a given string is a palindrome (reads the same forwards and backwards).

    Args:
        s (str): The input string to be checked for palindrome status.

    Returns:
        bool: True if the input string is a palindrome, False otherwise.
    """
    # Remove spaces and punctuation and convert to lowercase
    s = ''.join(char for char in s if char.isalnum()).lower()
    
    reverse_s = s[::-1]
    
    if s == reverse_s:
        return True
    else:
        return False

# Input validation loop
while True:
    string_1 = input("Enter a value (or 'exit' to quit): ")
    
    if string_1.lower() == 'exit':
        break
    
    if is_palindrome(string_1):
        print("YES - entered value is a palindrome!")
    else:
        print("NO - this value is not a palindrome!")

