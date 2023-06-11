# LeetCode task: solution -> https://leetcode.com/problems/rotate-array/description/?envType=study-plan-v2&envId=top-interview-150
# Coding interview preparation 

class Solution:
    """A class that provides a method to rotate an array of integers."""

    def rotate(self, nums: List[int], k: int) -> None:
        """Rotates the array to the right by k steps in place.

        Args:
            nums: A list of integers to be rotated.
            k: An integer indicating the number of steps to rotate.

        Example:
            >>> nums = [1, 2, 3, 4, 5, 6, 7]
            >>> k = 3
            >>> Solution().rotate(nums, k)
            >>> nums
            [5, 6, 7, 1, 2, 3, 4]
        """
        # Calculate the effective number of rotations
        k = k % len(nums)

        # Reverse the entire array
        self.reverse(nums, 0, len(nums) - 1)

        # Reverse the first k elements
        self.reverse(nums, 0, k - 1)

        # Reverse the remaining elements
        self.reverse(nums, k, len(nums) - 1)

    def reverse(self, nums: List[int], start: int, end: int) -> None:
        """Reverses a sublist of the array in place.

        Args:
            nums: A list of integers to be reversed.
            start: An integer indicating the starting index of the sublist.
            end: An integer indicating the ending index of the sublist.

        Example:
            >>> nums = [1, 2, 3, 4]
            >>> start = 1
            >>> end = 2
            >>> Solution().reverse(nums, start, end)
            >>> nums
            [1, 3, 2, 4]
        """
        while start < end:
            # Swap the elements at start and end indices
            nums[start], nums[end] = nums[end], nums[start]
            # Increment the start index and decrement the end index
            start += 1
            end -= 1
