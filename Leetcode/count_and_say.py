# LeetCode task: solution -> https://leetcode.com/problems/count-and-say
# 🤞 Preparation to coding interview 🎯😎

class Solution:
    def countAndSay(self, n: int) -> str:
        """Returns the nth term of the count-and-say sequence.

        The count-and-say sequence is a series of strings where each term is obtained by reading the previous term and counting the number of consecutive digits. For example, the first few terms are:

        1
        11
        21
        1211
        111221
        ...

        Args:
            n: An integer representing the position of the term in the sequence.

        Returns:
            A string representing the nth term of the count-and-say sequence.
        """

        # Base case
        if n == 1:
            return "1"

        # Recursive case
        prev_sequence = self.countAndSay(n - 1)  # Get the previous term
        result = ""  # Initialize an empty string to store the result
        count = 1  # Initialize a counter to track the number of consecutive digits
        i = 0  # Initialize an index to iterate over the previous term

        while i < len(prev_sequence):
            # Count the number of consecutive digits
            while i < len(prev_sequence) - 1 and prev_sequence[i] == prev_sequence[i + 1]:
                count += 1  # Increment the counter
                i += 1  # Move to the next digit

            # Append the count and digit to the result
            result += str(count) + prev_sequence[i]

            # Reset the count for the next digit
            count = 1
            i += 1

        return result
