def shortwords(words):
    """
    Returns a string containing all the shortest words from the given list of words.

    Args:
        words (list): A list of words.

    Returns:
        str: A string containing all the shortest words, separated by spaces.
    """
    # Find the length of the shortest word in the list
    minlen = len(words[0])
    for word in words:
        if len(word) < minlen:
            minlen = len(word)

    ans = ""
    # Create a string with all the words that have the minimum length
    for word in words:
        if len(word) == minlen:
            ans += word + " "

    return ans


# Driver code to test the function
word_list = ["apple", "banana", "cat", "dog", "elephant", "fish"]
result = shortwords(word_list)
print(f"The shortest words in the list are: {result}")


