# LeetCode task: solution -> https://leetcode.com/problems/longest-common-prefix/

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """Returns the longest common prefix among a list of strings.

        Args:
            strs: A list of strings.

        Returns:
            A string that is the longest common prefix of all the strings in strs.
            If strs is empty or there is no common prefix, returns an empty string.
        """
        if not strs: # if strs is empty
            return "" # return an empty string
        prefix = strs[0] # initialize prefix as the first string in strs
        for i in range(1, len(strs)): # loop through the rest of the strings in strs
            while strs[i].find(prefix) != 0: # while prefix is not a prefix of the current string
                prefix = prefix[:-1] # remove the last character from prefix
                if not prefix: # if prefix becomes empty
                    return "" # return an empty string
        return prefix # return the final prefix
