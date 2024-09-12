def to_jaden_case(string: str) -> str:
    """
    Convert a string to Jaden Case.

    Jaden Case is a style where every word in a sentence is capitalized.
    This function takes a string input and returns the Jaden Cased version.

    Args:
        string (str): The input string to be converted.

    Returns:
        str: The Jaden Cased version of the input string.

    Example:
        >>> to_jaden_case("how can mirrors be real if our eyes aren't real")
        "How Can Mirrors Be Real If Our Eyes Aren't Real"
    """
    # Split the string into words
    words = string.split()

    # Capitalize each word
    capitalized_words = [word.capitalize() for word in words]

    # Join the capitalized words back together
    return " ".join(capitalized_words)


# Driver code
if __name__ == "__main__":
    # Test cases
    test_strings = [
        "How can mirrors be real if our eyes aren't real",
        "the quick brown fox jumps over the lazy dog",
        "I'm 20 and I'm still learning from my mistakes",
        "school is cool but I like to swim",
    ]

    # Process each test string
    for i, test_string in enumerate(test_strings, 1):
        jaden_cased = to_jaden_case(test_string)
        print(f"Test {i}:")
        print(f"Original: {test_string}")
        print(f"Jaden Cased: {jaden_cased}")
        print()
