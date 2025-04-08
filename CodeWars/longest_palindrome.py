def longest_palindrome(s):
    """
    Function to find the length of the longest palindromic substring in a given string.

    A palindrome is a string that reads the same forward and backward. This function uses dynamic programming
    to determine the length of the longest palindromic substring within the input string.

    Parameters:
    s (str): The input string to be checked for palindromic substrings.

    Returns:
    int: The length of the longest palindromic substring.
    """
    n = len(s)
    if n == 0:
        return 0

    # Initialize a 2D list (dp table) to keep track of palindromic substrings
    dp = [[False] * n for _ in range(n)]
    
    # Every single character is a palindrome
    for i in range(n):
        dp[i][i] = True

    # Variable to keep track of the maximum length of palindromic substring found
    max_len = 1

    # Check for palindromes of length 2 and greater
    for k in range(2, n + 1):  # k is the length of the substring
        for i in range(n - k + 1):  # i is the starting index of the substring
            j = i + k - 1  # j is the ending index of the substring
            # Check if the characters at the start and end of the substring are the same
            if s[i] == s[j]:
                # If the substring length is 2 or the inner substring is a palindrome
                if k == 2 or dp[i + 1][j - 1]:
                    dp[i][j] = True  # Mark the substring as a palindrome
                    max_len = max(max_len, k)  # Update the maximum length

    return max_len

# Driver code to test the function
if __name__ == "__main__":
    test_strings = [
        "babad",      # Expected output: 3 ("bab" or "aba")
        "cbbd",       # Expected output: 2 ("bb")
        "a",          # Expected output: 1 ("a")
        "ac",         # Expected output: 1 ("a" or "c")
        "",           # Expected output: 0 (empty string)
        "racecar",    # Expected output: 7 ("racecar")
        "noon",       # Expected output: 4 ("noon")
        "abcdefg",    # Expected output: 1 (no palindromes longer than 1)
    ]

    for s in test_strings:
        print(f"Longest palindromic substring length in '{s}': {longest_palindrome(s)}")
