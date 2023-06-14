# LeetCode task: solution -> https://leetcode.com/problems/valid-palindrome/description/?envType=study-plan-v2&envId=top-interview-150
# 🍀 Coding task preparation -> for coding interview 🎯

import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Convert to lowercase and remove non-alphanumeric characters
        s = re.sub('[^a-zA-Z0-9]', '', s.lower())
        
        # Compare with the reversed string
        return s == s[::-1]
