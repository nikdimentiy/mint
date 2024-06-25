def find_most_frequent_char(s):
    """
    Find and return the most frequently occurring character in the input sequence.

    Args:
    s (str): The input sequence.

    Returns:
    str: The most frequently occurring character.
    """
    if not s:  # Handle empty string edge case
        return ""

    char_count = {}  # Dictionary to store the frequency of each character

    # Loop through each character in the input sequence
    for char in s:
        if char in char_count:
            char_count[char] += 1  # Increment the counter if the character is already in the dictionary
        else:
            char_count[char] = 1  # Initialize the counter for a new character

    # Find the character with the maximum frequency
    most_frequent_char = max(char_count, key=char_count.get)
    
    return most_frequent_char  # Return the most frequently occurring character

# Driver code to test the function.
if __name__ == "__main__":
    s = input("Enter a sequence: ")  # Prompt the user to enter an input sequence.
    result = find_most_frequent_char(s)  # Call the function to find the most frequent character.
    print("The most frequently occurring character is:", result)  # Print the result.
