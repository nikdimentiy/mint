# LeetCode task: solution -> https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """Removes duplicates from a sorted array in-place and returns the number of unique elements.

        Args:
            nums: A list of integers sorted in ascending order.

        Returns:
            An integer representing the number of unique elements in nums.

        Example:
            >>> s = Solution()
            >>> nums = [1, 1, 2]
            >>> s.removeDuplicates(nums)
            2
            >>> nums
            [1, 2]
        """
        if len(nums) == 0:  # check if the array is empty
            return 0  # return zero as the number of unique elements

        slow = 0  # slow pointer to track the unique elements
        fast = 1  # fast pointer to iterate through the array

        while fast < len(nums):  # loop until fast pointer reaches the end of the array
            if nums[fast] != nums[slow]:  # if the current element is different from the previous one
                slow += 1  # increment slow pointer
                nums[slow] = nums[fast]  # update the next unique element
            fast += 1  # increment fast pointer

        return slow + 1  # return the number of unique elements
