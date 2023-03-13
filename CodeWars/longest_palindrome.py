# CodeWars task - https://www.codewars.com/kata/54bb6f887e5a80180900046b/train/python


def longest_palindrome(s):
    n = len(s)
    if n == 0:
        return 0

    # Initialize dp table
    dp = [[False] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = True

    # Find longest palindrome substring
    max_len = 1
    for k in range(2, n+1):
        for i in range(n-k+1):
            j = i + k - 1
            if s[i] == s[j]:
                if k == 2 or dp[i+1][j-1]:
                    dp[i][j] = True
                    max_len = max(max_len, k)

    return max_len
