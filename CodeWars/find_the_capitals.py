def capitals(word):
    """
    This function takes a string as input and returns a list of indices 
    where the uppercase letters are located in the string.

    Parameters:
    word (str): The input string to be analyzed.

    Returns:
    list: A list of indices corresponding to the positions of uppercase letters in the input string.
    """
    inds = []  # Initialize an empty list to store indices of uppercase letters
    i = 0  # Initialize a counter for the index

    # Iterate through each character in the input string
    for l in word:
        if l.isupper():  # Check if the character is uppercase
            inds.append(i)  # If it is, append the index to the list
        i += 1  # Increment the index counter

    return inds  # Return the list of indices


# Driver code to test the capitals function
if __name__ == "__main__":
    test_word = "Hello World! This is a Test."
    result = capitals(test_word)
    print(f"The indices of uppercase letters in '{test_word}' are: {result}")
