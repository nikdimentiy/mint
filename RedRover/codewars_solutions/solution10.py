# Predefined NATO phonetic alphabet dictionary
LETTERS = {
    'A': 'Alpha', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo',
    'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel', 'I': 'India', 'J': 'Juliett',
    'K': 'Kilo', 'L': 'Lima', 'M': 'Mike', 'N': 'November', 'O': 'Oscar',
    'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango',
    'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'X-ray', 'Y': 'Yankee',
    'Z': 'Zulu'
}

def nato(word: str) -> str:
    """
    Convert a word to its NATO phonetic alphabet representation.

    Args:
        word (str): The input word to be converted.

    Returns:
        str: A string containing the NATO phonetic alphabet representation of the input word.

    Examples:
        >>> nato("hi")
        'Hotel India'
        >>> nato("abc")
        'Alpha Bravo Charlie'
    """
    # Convert the word to uppercase and map each letter to its NATO equivalent
    # Ignore non-alphabetic characters
    return ' '.join(LETTERS[letter.upper()] for letter in word if letter.isalpha())

# Driver code
if __name__ == "__main__":
    # Test cases
    test_words = ["hi", "abc", "babble", "Banana", "Hello123"]
    
    for word in test_words:
        result = nato(word)
        print(f"Input: {word}")
        print(f"NATO: {result}")
        print()  # Add a blank line for readability