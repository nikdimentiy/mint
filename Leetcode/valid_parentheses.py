# LeetCode task: solution -> https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        """
        Determines whether a string containing brackets is valid.

        Args:
            s (str): The input string containing brackets.

        Returns:
            bool: True if the string is valid, False otherwise.
        """
        stack = []  # Initialize an empty stack to track opening brackets
        brackets = {'(': ')', '{': '}', '[': ']'}  # Mapping of opening brackets to closing brackets

        for char in s:
            if char in brackets:  # If the character is an opening bracket
                stack.append(char)  # Push it onto the stack
            elif char in brackets.values():  # If the character is a closing bracket
                if not stack:  # If the stack is empty, there is no corresponding opening bracket
                    return False
                opening_bracket = stack.pop()  # Pop the top element from the stack
                if brackets[opening_bracket] != char:  # Check if the closing bracket matches the opening bracket
                    return False

        return len(stack) == 0  # If the stack is empty, all opening brackets were closed properly
