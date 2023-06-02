# LeetCode task: solution -> https://leetcode.com/problems/majority-element/?envType=study-plan-v2&envId=top-interview-150

def majorityElement(nums):
    """
    Returns the majority element in a list of numbers.

    A majority element is an element that appears more than n/2 times in a list of n numbers.

    Args:
        nums: A list of numbers.

    Returns:
        The majority element in nums, or any element if there is no majority.

    Raises:
        ValueError: If nums is empty.
    """

    # Initialize the candidate element and its count
    candidate = nums[0]
    count = 1

    # Loop through the rest of the list
    for i in range(1, len(nums)):
        # If the current element is equal to the candidate, increment the count
        if nums[i] == candidate:
            count += 1
        # Otherwise, decrement the count
        else:
            count -= 1

        # If the count becomes zero, update the candidate and reset the count
        if count == 0:
            candidate = nums[i]
            count = 1

    # Return the candidate element
    return candidate


nums = [2, 2, 1, 1, 1, 2, 2]
result = majorityElement(nums)
print(result)  # Output: 2
