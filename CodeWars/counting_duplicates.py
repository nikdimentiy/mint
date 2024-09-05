def duplicate_count(text):
    """
    Counts the number of characters in the input string that occur more than once.

    Args:
        text (str): The input string to be analyzed.

    Returns:
        int: The count of characters that appear more than once in the string.
    """
    # Convert the input text to lowercase to ensure case insensitivity
    text = text.lower()
    
    # Create a dictionary to count occurrences of each character
    chars = {char: text.count(char) for char in text}
    
    # Count how many characters have a count of 2 or more
    return len([char for char in chars if chars[char] >= 2])

# Driver code to test the function
if __name__ == "__main__":
    test_string = "Indivisibilities"
    result = duplicate_count(test_string)
    print(f"The number of duplicate characters in '{test_string}' is: {result}")
