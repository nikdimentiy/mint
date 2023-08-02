# 🇺🇦 Preparation to algorithmic interview 😃

def wordsindict(dictionary, text):
    """
    Check if words in a given list are 'good words' based on a dictionary.

    This function takes a list of 'good words' (dictionary) and a list of words to check (text).
    It determines if each word in the text is a 'good word' or not based on the dictionary.

    Parameters:
        dictionary (list): A list of strings representing 'good words'.
        text (list): A list of strings representing the words to be checked.

    Returns:
        list: A list of boolean values where each element represents whether the corresponding word in the text is a 'good word' or not.

    Example:
        dictionary = ["cat", "dog", "fish"]  # List of 'good words'
        text = ["cat", "bat", "dog", "dish"]  # List of words to check
        result = wordsindict(dictionary, text)
        # result will be [True, False, True, False] as "cat" and "dog" are present in the dictionary,
        # while "bat" and "dish" are not.

    Note:
        A 'good word' is defined as a word that exists in the dictionary or can be formed by removing a single letter from a word in the dictionary.
    """
    goodwords = set(
        dictionary
    )  # Create a set of "good words" from the given dictionary list
    for word in dictionary:  # Iterate through each word in the dictionary
        for delpos in range(len(word)):  # Iterate through each letter index in the word
            goodwords.add(
                word[:delpos] + word[delpos + 1 :]
            )  # Add each variant of the word where a letter at a specific index is removed to the "good words" set
    ans = []  # Create a list for answers
    for word in text:  # Iterate through each word in the text
        ans.append(
            word in goodwords
        )  # Append True to the answer list if it is a "good word," otherwise append False
    return ans


dictionary = ["cat", "dog", "fish"]  # List of "good words"
text = ["cat", "bat", "dog", "dish"]  # List of words we want to check
result = wordsindict(dictionary, text)  # Call the function to get the list of answers
print(result)  # Print the list of answers to the screen
