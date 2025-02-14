def capitalize(text, indices):
    """
    Capitalizes all letters in the given string at the specified indices.

    Args:
        text (str): The input string (lowercase with no spaces).
        indices (list): A list of integers representing the indices to capitalize.

    Returns:
        str: The modified string with characters capitalized at the specified indices.
    """
    result = ""  # Initialize an empty string to store the result
    for i, char in enumerate(text):  # Loop through each character and its index
        if i in indices:  # Check if the current index is in the list of indices
            result += char.upper()  # Capitalize the character and add it to the result
        else:
            result += char  # Add the character as is to the result
    return result  # Return the final modified string


# Driver code
if __name__ == "__main__":
    # Test cases
    print(capitalize("abcdef", [1, 2, 5]))  # Output: "aBCdeF"
    print(capitalize("abcdef", [1, 2, 5, 100]))  # Output: "aBCdeF" (ignores invalid index 100)
    print(capitalize("hello", [0, 4]))  # Output: "HellO"
    print(capitalize("world", [1, 3]))  # Output: "wOrLd"
    print(capitalize("example", []))  # Output: "example" (no indices to capitalize)
