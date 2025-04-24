def longest_palindrome(s):
    """
    Find the length of the longest palindromic substring in a given string.

    A palindrome is a string that reads the same forward and backward. 
    This function uses a linear time complexity approach (O(n)) to determine 
    the length of the longest palindromic substring.

    Parameters:
    s (str): The input string to be analyzed.

    Returns:
    int: The length of the longest palindromic substring.
    """
    
    maxPal, tmpPal = 0, 1  # Initialize maximum palindrome length and temporary palindrome length
    count_dct = {}         # Dictionary to count occurrences of characters
    inPal = False          # Flag to indicate if we are currently in a palindrome

    for i, l in enumerate(s):
        # Count occurrences of the current character
        count_dct[l] = count_dct.get(l, 0) + 1

        # Check if we might encounter a palindrome
        if not inPal and count_dct[l] >= 2:
            # Check for a palindrome with a double character in the middle
            if l == s[i-1]:
                inPal = True
                tmpPal = 2  # Length of palindrome is 2

            # Check for a palindrome with one "peak" character in the middle
            elif i >= 2 and l == s[i-2]:
                inPal = True
                tmpPal = 3  # Length of palindrome is 3

        # If we are still in a palindrome
        elif inPal and l == s[max(0, i-tmpPal-1)]:
            tmpPal += 2  # Extend the palindrome length

        else:  # We have exited the palindrome
            inPal = False
            tmpPal = 1  # Reset temporary palindrome length

        # Update the maximum palindrome length found
        maxPal = max(maxPal, tmpPal)

    return maxPal

# Driver code to test the function
if __name__ == "__main__":
    test_strings = [
        "babad",      # Expected output: 3 ("bab" or "aba")
        "cbbd",       # Expected output: 2 ("bb")
        "a",          # Expected output: 1 ("a")
        "ac",         # Expected output: 1 ("a" or "c")
        "racecar",    # Expected output: 7 ("racecar")
        "noon",       # Expected output: 4 ("noon")
        "abcdefg",    # Expected output: 1 (no palindromes longer than 1)
        "aabbcc",     # Expected output: 2 ("aa" or "bb" or "cc")
    ]

    for s in test_strings:
        print(f"Longest palindrome length in '{s}': {longest_palindrome(s)}")

