def duplicate_encode(word):
    """
    Create a new string where each character in the new string is '(' 
    if that character appears only once in the original word, or ')' 
    if that character appears more than once in the original word. 
    This function ignores capitalization when determining if a character 
    is a duplicate.

    Parameters:
    word (str): The input string to be processed.

    Returns:
    str: A new string with '(' and ')' based on the character frequency.
    """
    # Convert the input word to uppercase to ignore case sensitivity
    word = word.upper()
    
    # Initialize an empty result string
    result = ""
    
    # Iterate through each character in the word
    for char in word:
        # Check if the character appears more than once in the word
        if word.count(char) > 1:
            result += ")"  # Append ')' for duplicates
        else:
            result += "("  # Append '(' for unique characters

    return result

# Driver code to test the function
if __name__ == "__main__":
    test_words = ["Success", "recede", "((@", "Duplicate", "abcde"]
    
    for word in test_words:
        encoded = duplicate_encode(word)
        print(f"Original word: '{word}' -> Encoded: '{encoded}'")
