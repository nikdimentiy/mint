# LeetCode task: solution -> https://leetcode.com/problems/is-subsequence/description/?envType=study-plan-v2&envId=top-interview-150
# Preparig for coding interview 🎯

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)
      
s = "abc"
t = "ahbgdc"
solution = Solution()
print(solution.isSubsequence(s, t))  # Output: True

s = "axc"
t = "ahbgdc"
print(solution.isSubsequence(s, t))  # Output: False
