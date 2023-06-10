# LeetCode task: solution -> https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/?envType=study-plan-v2&envId=top-interview-150
# LeetCode ->  preparation for coding interview: 150 coding task

class Solution:

    """
    This class provides a function to find the first occurrence of a string in another string.
    """

    def strStr(self, haystack: str, needle: str) -> int:
        """
        Finds the first occurrence of the needle string in the haystack string.

        Args:
            haystack: The string to search.
            needle: The string to find.

        Returns:
            The index of the first occurrence of the needle string in the haystack string, or -1 if the needle string is not found.
        """

        # Check if the needle string is empty. If it is, return 0.
        if not needle:
            return 0

        # Check if the needle string is longer than the haystack string. If it is, return -1.
        if len(needle) > len(haystack):
            return -1

        # Iterate over the haystack string, starting from the beginning.
        for i in range(len(haystack) - len(needle) + 1):
            # Compare the current substring of the haystack string with the needle string.
            # If they are equal, return the index of the current substring.
            if haystack[i : i + len(needle)] == needle:
                return i

        # If the needle string is not found, return -1.
        return -1
