def is_palindrome(input_string):
    """
    This function checks whether the given string is a palindrome.

    Args:
        input_string (str): The string to be checked for palindromic properties.

    Returns:
        bool: True if the input_string is a palindrome, False otherwise.
    """
    reverse_string = input_string[::-1]

    if input_string == reverse_string:
        return True
    else:
        return False

# Driver code
if __name__ == "__main__":
    string_1 = input("Enter the string to check for palindrome: ")

    if is_palindrome(string_1):
        print("YES - entered value is a palindrome!")
    else:
        print("NO - this value is not a palindrome!")
