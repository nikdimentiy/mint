def disemvowel(string):
    """
    Remove all vowels from the input string.

    Parameters:
    string (str): The input string from which vowels will be removed.

    Returns:
    str: A new string with all vowels removed.
    """
    # Use a list comprehension to iterate through each character in the string
    # and include it in the result only if it is not a vowel.
    return "".join([ch for ch in string if ch not in "aeiouAEIOU"])

# Driver code to test the disemvowel function
if __name__ == "__main__":
    test_string = "This is an example string."
    result = disemvowel(test_string)
    print("Original string:", test_string)
    print("Disemvoweled string:", result)
