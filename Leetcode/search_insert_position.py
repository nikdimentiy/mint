# LeetCode task: solution -> https://leetcode.com/problems/search-insert-position/description/
# 🎯 Preparation for coding interview 🍀

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        This function returns the index where target should be inserted in a sorted list of numbers.
        If target is already in the list, it returns the index of its first occurrence.
        It uses binary search to find the index in O(log n) time and O(1) space.

        Parameters:
        nums: A sorted list of integers
        target: An integer to be inserted or searched

        Returns:
        An integer representing the index where target should be inserted or found
        """
        # Initialize left and right pointers
        left = 0
        right = len(nums) - 1

        # Loop until left and right pointers cross
        while left <= right:
            # Find the middle index
            mid = left + (right - left) // 2

            # If target is found, return its index
            if nums[mid] == target:
                return mid
            # If target is larger than the middle element, move left pointer to the right of mid
            elif nums[mid] < target:
                left = mid + 1
            # If target is smaller than the middle element, move right pointer to the left of mid
            else:
                right = mid - 1

        # If target is not found, return the left pointer as the insertion index
        return left

# Driver code to test the function
if __name__ == "__main__":
    # Create an instance of the Solution class
    sol = Solution()

    # Test some examples
    print(sol.searchInsert([1,3,5,6], 5)) # Output: 2
    print(sol.searchInsert([1,3,5,6], 2)) # Output: 1
    print(sol.searchInsert([1,3,5,6], 7)) # Output: 4
    print(sol.searchInsert([1,3,5,6], 0)) # Output: 0
