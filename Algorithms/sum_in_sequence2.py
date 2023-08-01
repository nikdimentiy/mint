# 😎 Preparation to algorithmic interview 👌

import random

def twotermswithsumx(nums, x):
    """Finds a pair of numbers from a list that add up to a given sum.

    Args:
        nums (list): A list of integers.
        x (int): The target sum.

    Returns:
        tuple: A pair of integers from nums that add up to x, or (0, 0) if no such pair exists.
    """
    # Initialize a set to store the previous numbers
    prevnums = set()
    # Loop through the list of numbers
    for nownum in nums:
        # Check if the complement of the current number is in the set
        if x - nownum in prevnums:
            # Return the pair of numbers
            return nownum, x - nownum
        # Add the current number to the set
        prevnums.add(nownum)
    # Return (0, 0) if no pair is found
    return 0, 0


# Example usage of the function

# Define the length of the list and the range of values for the random numbers
length = 10
min_value = 1
max_value = 21

# Create a list of random numbers
nums = [random.randint(min_value, max_value) for _ in range(length)]

# Print the list of random numbers
print(nums)

x = 17
result = twotermswithsumx(nums, x)
print("The pair of numbers from nums that add up to ", x, " is: ", result)


# The big O of this code is O(n), where n is the length of the list nums. 
# This is because the code loops through the list once, and each lookup and insertion in the set takes constant time.
