# LeetCode task: solution -> https://leetcode.com/problems/length-of-last-word/?envType=study-plan-v2&envId=top-interview-150
# 🎯 150 coding task: preparation to coding interview 🍀

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        Returns the length of the last word in a given string.

        Args:
            s (str): The input string consisting of words and spaces.

        Returns:
            int: The length of the last word. Returns 0 if no words are present.

        """

        # Trim leading and trailing spaces
        s = s.strip()

        # Split the trimmed string into a list of words
        words = s.split()

        if words:
            return len(words[-1])
        else:
            return 0


# Create an instance of the Solution class
solution = Solution()

# Call the lengthOfLastWord() method
print(solution.lengthOfLastWord("Hello World"))  # Output: 5
print(solution.lengthOfLastWord("   fly me   to   the moon  "))  # Output: 4
print(solution.lengthOfLastWord("luffy is still joyboy"))  # Output: 6


