import string

def toJadenCase(NonJadenStrings):
    """
    Convert a given string to Jaden Case, where the first letter of each word is capitalized.

    Jaden Case is a style of writing where each word in a sentence starts with an uppercase letter.
    
    Parameters:
    NonJadenStrings (str): The input string that needs to be converted to Jaden Case.

    Returns:
    str: The input string converted to Jaden Case.
    """
    # Use string.capwords to capitalize the first letter of each word in the input string
    return string.capwords(NonJadenStrings)

# Driver code to test the function
if __name__ == "__main__":
    # Example input string
    input_string = "how can mirrors be real if our eyes aren't real"
    
    # Convert the input string to Jaden Case
    jaden_case_string = toJadenCase(input_string)
    
    # Print the result
    print(jaden_case_string)  # Output: "How Can Mirrors Be Real If Our Eyes Aren't Real"
