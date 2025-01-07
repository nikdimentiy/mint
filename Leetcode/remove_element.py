from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Removes all occurrences of 'val' from the 'nums' list in-place.
        This method modifies the input list such that all elements that are not equal to 'val'
        are moved to the front of the list, and the elements beyond the new length are irrelevant.

        Args:
            nums (List[int]): The input list of integers.
            val (int): The value to remove from 'nums'.

        Returns:
            int: The number of elements in 'nums' that are not equal to 'val'.
        """
        # Initialize a pointer 'i' to keep track of the position to place the next valid element
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

# Driver code to test the removeElement function
if __name__ == "__main__":
    # Create an instance of the Solution class
    solution = Solution()
    
    # Example input
    nums = [3, 2, 2, 3]
    val = 3
    
    # Call the removeElement method
    new_length = solution.removeElement(nums, val)
    
    # Print the results
    print(f"New length of the array: {new_length}")
    print(f"Modified array: {nums[:new_length]}")  # Print only the relevant part of the array
