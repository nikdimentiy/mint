# 🍀 Preparation to coding -> (algorithmic) interview 🤞

def rle(s):
    """
    Perform Run-Length Encoding (RLE) on a given string.

    This function takes a string `s` and performs Run-Length Encoding (RLE) on it.
    RLE is a simple form of data compression where consecutive occurrences of the same character
    are replaced with the character followed by the number of occurrences.

    Parameters:
        s (str): The input string to be encoded using Run-Length Encoding.

    Returns:
        str: The encoded string after applying Run-Length Encoding.

    Example:
        input_string = "aaabbbbcc"
        encoded_string = rle(input_string)
        # encoded_string will be "a3b4c2" as "a" appears 3 times, "b" appears 4 times, and "c" appears 2 times.

    """

    def pack(s, cnt):
        """
        Helper function to pack a character with its count if count > 1.

        Parameters:
            s (str): The character to be packed.
            cnt (int): The count of consecutive occurrences of the character.

        Returns:
            str: The packed representation of the character with its count if count > 1, otherwise the character itself.

        """
        if cnt > 1:
            return s + str(cnt)
        return s

    lastsym = s[
        0
    ]  # Initialize the last character seen to the first character of the string
    lastpos = 0  # Initialize the last position seen to 0
    ans = []  # Create a list to store the encoded segments
    for i in range(len(s)):  # Iterate through each character in the string
        if (
            s[i] != lastsym
        ):  # Check if the current character is different from the last character seen
            ans.append(
                pack(lastsym, i - lastpos)
            )  # Pack the last character with its count and add it to the list
            lastpos = i  # Update the last position seen to the current position
            lastsym = s[i]  # Update the last character seen to the current character
    ans.append(
        pack(s[lastpos], len(s) - lastpos)
    )  # Pack the final character with its count and add it to the list
    return "".join(ans)  # Join the encoded segments to form the final encoded string


# Driver code to demonstrate the rle function

# Example 1
input_string1 = "aaabbbbcc"
encoded_string1 = rle(input_string1)
print("Example 1:")
print("Input string:", input_string1)
print("Encoded string:", encoded_string1)
# Output: a3b4c2

# Example 2
input_string2 = "abcd"
encoded_string2 = rle(input_string2)
print("\nExample 2:")
print("Input string:", input_string2)
print("Encoded string:", encoded_string2)
# Output: a1b1c1d1

# Example 3
input_string3 = "tttjjjeeeaaahhhuuu"
encoded_string3 = rle(input_string3)
print("\nExample 3:")
print("Input string:", input_string3)
print("Encoded string:", encoded_string3)
# Output: t3j3e3a3h3u3

# Example 4
input_string4 = "abbbccdeeefff"
encoded_string4 = rle(input_string4)
print("\nExample 4:")
print("Input string:", input_string4)
print("Encoded string:", encoded_string4)
# Output: a1b3c2d1e3f3
