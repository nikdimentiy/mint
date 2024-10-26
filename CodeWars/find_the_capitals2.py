def capitals(word):
    """
    Returns a list of indices of uppercase letters in the given word.

    Parameters:
    word (str): The input string from which to find uppercase letters.

    Returns:
    list: A list of indices where uppercase letters are found in the input string.
    """
    # Using list comprehension to iterate over the enumerated characters of the word
    return [i for (i, c) in enumerate(word) if c.isupper()]

# Driver code to test the capitals function
if __name__ == "__main__":
    test_word = "HelloWorld"
    result = capitals(test_word)
    print(f"The indices of uppercase letters in '{test_word}' are: {result}")
