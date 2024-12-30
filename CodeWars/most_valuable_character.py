def solve(st):
    """
    This function takes a string `st` and returns the most valuable character based on the following criteria:
    - The value of a character is the difference between the index of its last occurrence and the index of its first occurrence.
    - If there is a tie in values, the function returns the lexicographically lowest character.

    Parameters:
    st (str): The input string containing only lowercase letters.

    Returns:
    str: The most valuable character based on the criteria.

    Examples:
    solve('a') -> 'a'
    solve('ab') -> 'a'
    solve('axyzxyz') -> 'x'
    """
    # Create a dictionary where the key is the character and the value is the difference
    # between the index of its last occurrence and the index of its first occurrence
    chars = {char: abs(st.find(char) - st.rfind(char)) for char in st}

    # Find the character with the highest value. In case of a tie, return the lexicographically lowest character
    return max(sorted(chars), key=lambda x: chars[x])

# Driver code to test the function
if __name__ == "__main__":
    # Test cases
    print(solve('a'))  # Expected output: 'a'
    print(solve('ab'))  # Expected output: 'a'
    print(solve('axyzxyz'))  # Expected output: 'x'
    print(solve('zebra'))  # Expected output: 'z'
    print(solve('hello'))  # Expected output: 'l'
    print(solve('banana'))  # Expected output: 'a'

