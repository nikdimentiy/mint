def reverse_string(string):
    """
    Reverse the characters in a given string.
    
    Args:
        string (str): The input string to be reversed.
        
    Returns:
        str: The reversed string.
    """
    reversed_string = ""  # Initialize an empty string to store the reversed string
    for char in string:  # Iterate through each character in the input string
        reversed_string = char + reversed_string  # Prepend each character to the reversed string
    return reversed_string  # Return the reversed string

# Example usage
original_string = "Hello, World!"
reversed_string = reverse_string(original_string)
print(reversed_string)
