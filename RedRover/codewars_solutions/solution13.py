def drop_cap(words: str) -> str:
    """
    Capitalize words in a string that are longer than two characters.

    This function takes a string of words and capitalizes each word that has
    more than two characters. Words with two or fewer characters remain unchanged.
    The function preserves all original spacing, including leading and trailing spaces.

    Args:
        words (str): A string containing one or more words.

    Returns:
        str: A new string with applicable words capitalized.

    Examples:
        >>> drop_cap("apple")
        'Apple'
        >>> drop_cap("apple of banana")
        'Apple of Banana'
        >>> drop_cap("one   space")
        'One   Space'
        >>> drop_cap("   space WALK   ")
        '   Space Walk   '
    """
    # Split the input string into words while preserving leading and trailing spaces
    words_list = words.split(" ")

    # Capitalize words longer than 2 characters
    capitalized_words = [
        word.capitalize() if len(word) > 2 else word for word in words_list
    ]

    # Join the words back into a single string with spaces
    return " ".join(capitalized_words)


# Driver code
if __name__ == "__main__":
    # Test cases
    test_cases = [
        "apple",
        "apple of banana",
        "one   space",
        "   space WALK   ",
        "a b c d e f",
        "two    spaces",
        "ALL CAPS",
        "mixed CAPS and lower",
        "  leading and trailing spaces  ",
    ]

    # Run test cases
    for test in test_cases:
        result = drop_cap(test)
        print(f"Input: '{test}'")
        print(f"Output: '{result}'")
        print("-" * 40)
