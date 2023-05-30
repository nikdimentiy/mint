from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Removes all occurrences of 'val' from the 'nums' list in-place.
        Returns the number of elements in 'nums' that are not equal to 'val'.

        Args:
            nums (List[int]): The input list of integers.
            val (int): The value to remove from 'nums'.

        Returns:
            int: The number of elements in 'nums' that are not equal to 'val'.
        """
        # Initialize a pointer 'i' to keep track of the elements that are not equal to 'val'
        i = 0

        # Iterate through the 'nums' list using pointer 'j'
        for j in range(len(nums)):
            # If the current element is not equal to 'val'
            if nums[j] != val:
                # Move the element to the 'i'th position and increment 'i'
                nums[i] = nums[j]
                i += 1

        # Return the value of 'i' which represents the number of elements that are not equal to 'val'
        return i
