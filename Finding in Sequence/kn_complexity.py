# This program finds the character that appears most frequently in an input sequence
# using a nested loop with a set to get unique symbols.

# Define a function that takes an input sequence as a string.
def find_most_frequent_char(s):
    """
    Find and return the most frequently occurring character in the input sequence.

    Args:
    s (str): The input sequence.

    Returns:
    str: The most frequently occurring character.
    """

    ans = ""  # Initialize an empty string to store the result.
    anscnt = 0  # Initialize a counter for the most frequently occurring character.

    # Loop through each unique symbol in the input sequence.
    for now in set(s):
        nowcnt = 0  # Initialize a counter for the current character.

        # Loop through the input sequence to count occurrences of the current character.
        for j in range(len(s)):
            if now == s[j]:
                nowcnt += 1  # Increment the counter if a matching character is found.

        # Check if the current character appears more frequently than the previous result.
        if nowcnt > anscnt:
            ans = now  # Update the result character.
            anscnt = nowcnt  # Update the counter for the most frequently occurring character.

    return ans  # Return the most frequently occurring character.

# Driver code to test the function.
if __name__ == "__main__":
    s = input("Enter a sequence: ")  # Prompt the user to enter an input sequence.
    result = find_most_frequent_char(s)  # Call the function to find the most frequent character.
    print("The most frequently occurring character is:", result)  # Print the result.
