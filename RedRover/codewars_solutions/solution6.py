def smash_words(words: list) -> str:
    """
    Join a list of words into a single string, separated by spaces.

    Args:
        words (list): A list of strings to be joined.

    Returns:
        str: A single string with all words joined by spaces.
    """
    # Use the join method to concatenate all words with a space separator
    return " ".join(words)


# Driver code
if __name__ == "__main__":
    # Example usage
    words = ["hello", "world", "this", "is", "great"]

    # Call the smash_words function
    sentence = smash_words(words)

    # Print the result
    print(sentence)  # Output: 'hello world this is great'

    # Additional test cases
    print(smash_words(["coding", "is", "fun"]))  # Output: 'coding is fun'
    print(smash_words(["a", "b", "c", "d"]))  # Output: 'a b c d'
    print(smash_words([]))  # Output: '' (empty string)
