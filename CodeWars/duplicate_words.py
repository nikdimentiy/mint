def remove_consecutive_duplicates(text):
    """
    Remove consecutive duplicate words from a string.

    Args:
    text (str): A string containing words separated by spaces.

    Returns:
    str: A string with consecutive duplicate words removed, 
         retaining only the first occurrence of each word in a sequence.
    """
    # Split the input text into a list of words
    words = text.split()
    
    # Initialize a list to hold unique words, starting with the first word
    unique_words = [words[0]] if words else []
    
    # Iterate through the list of words starting from the second word
    for i in range(1, len(words)):
        # If the current word is not the same as the previous word, add it to the unique list
        if words[i] != words[i-1]:
            unique_words.append(words[i])
    
    # Join the unique words back into a single string and return it
    return ' '.join(unique_words)

# Driver code to test the function
if __name__ == "__main__":
    test_string = "alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta"
    result = remove_consecutive_duplicates(test_string)
    print("Original string:", test_string)
    print("Processed string:", result)
