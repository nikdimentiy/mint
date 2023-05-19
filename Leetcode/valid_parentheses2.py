# LeetCode task: solution -> https://leetcode.com/problems/valid-parentheses/

class Solution:
    """A class that checks if a given string of parentheses is valid."""

    def isValid(self, s: str) -> bool:
        """A method that returns True if s is a valid string of parentheses, and False otherwise.

        Args:
            s (str): The input string.

        Returns:
            bool: The boolean value indicating the validity of s.
        """
        stack = [] # Initialize an empty list to store the opening parentheses
        for i in s: # Loop through each character in s
            if i == "(" or i == "[" or i == "{": # If the character is an opening parenthesis
                stack.append(i) # Push it to the stack
            else: # If the character is a closing parenthesis
                if not stack: # If the stack is empty
                    return False # The string is invalid
                else: # If the stack is not empty
                    if i == ')': # If the character is a closing round parenthesis
                        if stack.pop() != "(": # Pop the top element from the stack and compare it with the opening round parenthesis
                            return False # If they don't match, the string is invalid
                    elif i == "]": # If the character is a closing square parenthesis
                        if stack.pop() != "[": # Pop the top element from the stack and compare it with the opening square parenthesis
                            return False # If they don't match, the string is invalid
                    elif i == "}": # If the character is a closing curly parenthesis
                        if stack.pop() != "{": # Pop the top element from the stack and compare it with the opening curly parenthesis
                            return False # If they don't match, the string is invalid

        if stack == []: # If the stack is empty after looping through s
            return True # The string is valid
        return False # Otherwise, the string is invalid


# Driver code
solution = Solution() # Create an instance of Solution class
input_string = input("Enter a string: ") # Prompt the user to enter a string
is_valid = solution.isValid(input_string) # Call the isValid method on the input string and store the result in a variable
print("Is the string valid?", is_valid) # Print the result to the console
