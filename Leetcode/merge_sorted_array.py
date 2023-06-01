# Solution to LeetCode's Interview Preparation Task -> https://leetcode.com/problems/merge-sorted-array/?envType=study-plan-v2&envId=top-interview-150

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # initialize three pointers: i for nums1, j for nums2, and k for the merged array
        i = m - 1
        j = n - 1
        k = m + n - 1

        # loop from the end of both arrays and compare the elements
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                # if nums1[i] is larger, put it at the end of the merged array
                nums1[k] = nums1[i]
                # decrement i and k
                i -= 1
            else:
                # if nums2[j] is larger or equal, put it at the end of the merged array
                nums1[k] = nums2[j]
                # decrement j and k
                j -= 1
            k -= 1

        # if there are any remaining elements in nums2, copy them to the merged array
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
