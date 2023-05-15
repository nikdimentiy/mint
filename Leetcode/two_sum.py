"""
This code implements the two sum algorithm.

Given an array of integers nums and an integer target,
find two numbers in nums such that their sum is equal to target.

The algorithm works by first creating a hash map,
where the keys are the integers in nums and the values are their indices.
Then, it iterates through the array,
and for each number num,
it checks if the target - num is in the hash map.
If it is,
the algorithm returns the indices of the two numbers.
Otherwise,
it adds the number num to the hash map.
If the algorithm reaches the end of the array without finding any two numbers whose sum is equal to target,
it returns an empty list.
"""

from typing import List


class Solution:
    """
    This class implements the two sum algorithm.
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        This method finds two numbers in nums whose sum is equal to target.

        Args:
            nums: A list of integers.
            target: An integer.

        Returns:
            A list of two integers, where the first integer is the index of the first number in nums whose sum with the second number is equal to target, and the second integer is the index of the second number.

        Raises:
            ValueError: If there are no two numbers in nums whose sum is equal to target.
        """

        if len(nums) < 2:
            raise ValueError("There must be at least two numbers in nums.")

        hash_map = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in hash_map:
                return [hash_map[diff], i]
            hash_map[num] = i

        return []


