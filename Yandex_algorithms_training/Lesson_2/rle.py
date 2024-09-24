def rle(s: str) -> str:
    """
    Perform Run-Length Encoding (RLE) on the input string.

    Run-Length Encoding is a simple form of data compression where 
    consecutive identical elements are replaced by a single element 
    followed by the count of its occurrences.

    Parameters:
    s (str): The input string to be encoded.

    Returns:
    str: The encoded string using Run-Length Encoding.
    """
    
    def pack(s: str, cnt: int) -> str:
        """
        Helper function to pack a character and its count.

        If the count is greater than 1, it appends the count to the character.
        Otherwise, it returns just the character.

        Parameters:
        s (str): The character to pack.
        cnt (int): The count of occurrences.

        Returns:
        str: The packed character with its count if cnt > 1, else just the character.
        """
        if cnt > 1:
            return s + str(cnt)
        return s

    lastsym = s[0]  # Initialize the last symbol to the first character
    lastpos = 0     # Initialize the last position to the start of the string
    ans = []        # List to hold the encoded parts

    # Iterate through the string to encode it
    for i in range(len(s)):
        if s[i] != lastsym:  # Check if the current character is different from the last
            ans.append(pack(lastsym, i - lastpos))  # Pack the last symbol and its count
            lastpos = i  # Update the last position
            lastsym = s[i]  # Update the last symbol

    # Append the last character and its count
    ans.append(pack(s[lastpos], len(s) - lastpos))
    
    return ''.join(ans)  # Join the list into a single string

# Driver code
if __name__ == '__main__':
    test_string = 'aaabbbccdaa'  # Test input string
    encoded_string = rle(test_string)  # Perform RLE encoding
    print(f'Original String: {test_string}')  # Print the original string
    print(f'Encoded String: {encoded_string}')  # Print the encoded string
