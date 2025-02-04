def toJadenCase(string):
    """
    Convert a given string to Jaden Case, where the first letter of each word is capitalized.

    Parameters:
    string (str): The input string to be converted.

    Returns:
    str: A new string with each word capitalized.
    """
    # Split the input string into words
    words = string.split()
    
    # Capitalize the first letter of each word and join them back into a single string
    jaden_case_string = " ".join(w.capitalize() for w in words)
    
    return jaden_case_string

# Driver code to test the function
if __name__ == "__main__":
    test_string = "how can mirrors be real if our eyes aren't real"
    result = toJadenCase(test_string)
    print(result)  # Output: "How Can Mirrors Be Real If Our Eyes Aren't Real"
