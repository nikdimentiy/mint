def grabscrab(word, possible_words):
    """
    Find all words in the list that are anagrams of the given word.

    An anagram is a word formed by rearranging the letters of another word.
    
    Parameters:
    word (str): The word to find anagrams of.
    possible_words (list of str): A list of words to check against.

    Returns:
    list of str: A list of words from possible_words that are anagrams of word.
    """
    # Use a list comprehension to filter possible_words
    # Check if the sorted characters of the word match the sorted characters of each word in possible_words
    return [w for w in possible_words if sorted(word) == sorted(w)]

# Driver code to test the function
if __name__ == "__main__":
    # Example word and possible anagrams
    word = "listen"
    possible_words = ["enlist", "google", "inlets", "banana"]

    # Call the grabscrab function
    anagrams = grabscrab(word, possible_words)

    # Print the result
    print(f"Anagrams of '{word}': {anagrams}")
