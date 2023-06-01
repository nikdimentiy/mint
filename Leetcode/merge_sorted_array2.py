# another solution of this task 😎 
# Solution to LeetCode's Interview Preparation Task -> https://leetcode.com/problems/merge-sorted-array/?envType=study-plan-v2&envId=top-interview-150

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Merge two sorted arrays nums1 and nums2 into nums1 in non-decreasing order.

        Args:
            nums1: The first sorted array.
            m: The number of elements in nums1.
            nums2: The second sorted array.
            n: The number of elements in nums2.

        Returns:
            None. The merged array is stored in nums1 in-place.

        Note:
            This implementation modifies nums1 in-place and does not return a new array.

        """

        j = n  # Initialize pointer for nums2

        # Iterate over nums1 starting from index 0
        for i in range(m+n):
            if j == 0:
                break

            # If current element in nums1 is greater than or equal to current element in nums2,
            # insert current element from nums2 into nums1 and adjust the pointers and array lengths
            if nums1[i] >= nums2[n-j]:
                nums1.insert(i, nums2[n-j])
                j -= 1
                nums1.pop(m + (n-j))

            # If the remaining elements in nums1 are all 0 and there are more elements in nums2,
            # replace the remaining 0s in nums1 with the remaining elements from nums2
            if nums1[i] == 0 and i >= m + (n-j):
                nums1[i] = nums2[n-j]
                j -= 1
