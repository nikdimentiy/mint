# This program finds the character that appears most frequently in an input sequence using a dictionary.

# Define a function that takes an input sequence as a string.
def find_most_frequent_char(s):
    """
    Find and return the most frequently occurring character in the input sequence.

    Args:
    s (str): The input sequence.

    Returns:
    str: The most frequently occurring character.
    """

    anscnt = 0  # Initialize a counter for the most frequently occurring character.
    symcnt = {}  # Initialize an empty dictionary to store character counts.

    # Loop through each character in the input sequence.
    for now in s:
        # Check if the character is not in the dictionary (first occurrence).
        if now not in symcnt:
            symcnt[now] = 0  # Initialize the count for this character.

        symcnt[now] += 1  # Increment the count for the current character.

        # Check if the current character appears more frequently than the previous result.
        if symcnt[now] > anscnt:
            ans = now  # Update the result character.
            anscnt = symcnt[now]  # Update the counter for the most frequently occurring character.

    return ans  # Return the most frequently occurring character.

# Driver code to test the function.
if __name__ == "__main__":
    s = input("Enter a sequence: ")  # Prompt the user to enter an input sequence.
    result = find_most_frequent_char(s)  # Call the function to find the most frequent character.
    print("The most frequently occurring character is:", result)  # Print the result.
