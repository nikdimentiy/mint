def disemvowel(s):
    """
    Removes all vowels from a given string.

    Args:
        s (str): The input string.

    Returns:
        str: The input string with all vowels removed.

    Examples:
        >>> disemvowel("Hello World")
        'Hll Wrld'
        >>> disemvowel("AEIOU")
        ''
    """
    # Iterate over each vowel (both lowercase and uppercase)
    for i in "aeiouAEIOU":
        # Replace each vowel with an empty string, effectively removing it
        s = s.replace(i, '')
    # Return the resulting string with all vowels removed
    return s

# Driver code
if __name__ == "__main__":
    # Test the function with some examples
    print(disemvowel("Hello World"))  # Expected output: 'Hll Wrld'
    print(disemvowel("AEIOU"))  # Expected output: ''
    print(disemvowel("This is a test"))  # Expected output: 'Ths s  tst'
