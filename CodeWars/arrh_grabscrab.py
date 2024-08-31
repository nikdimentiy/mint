def grabscrab(word, possible_words):
    """
    Find all possible words that can be formed by rearranging the letters of the given word.

    Parameters:
    word (str): The word whose letters will be rearranged.
    possible_words (list of str): A list of words to check against.

    Returns:
    list of str: A list of words from possible_words that can be formed by rearranging the letters of word.
    """
    # Initialize an empty list to store matching words
    words = []
    
    # Create a dictionary to count the occurrences of each letter in the input word
    letters1 = {l: word.count(l) for l in word}
    
    # Iterate through each word in the list of possible words
    for word in possible_words:
        # Create a dictionary to count the occurrences of each letter in the current word
        letters2 = {l: word.count(l) for l in word}
        
        # If the letter counts match, it means the current word can be formed by rearranging the input word
        if letters1 == letters2:
            words.append(word)  # Add the matching word to the list
    
    return words  # Return the list of matching words

# Driver code to test the function
if __name__ == "__main__":
    input_word = "listen"
    possible_words_list = ["enlist", "google", "inlets", "banana", "silent"]
    
    # Call the grabscrab function with the input word and possible words
    result = grabscrab(input_word, possible_words_list)
    
    # Print the result
    print(f"Words that can be formed by rearranging '{input_word}': {result}")
