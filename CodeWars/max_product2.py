import math
from functools import cache

def maximum_product(n):
    """
    Calculate the maximum product of integers that sum up to n.

    This function finds all possible partitions of the integer n and computes the product of the integers in each partition.
    It returns the maximum product found among all partitions.

    Parameters:
    n (int): The integer to be partitioned (must be greater than 0).

    Returns:
    int: The maximum product of integers that sum up to n.
    """
    return max(map(math.prod, partitions(n)))

@cache
def partitions(n, largest=math.inf):
    """
    Generate all partitions of the integer n.

    A partition of a number is a way of writing it as a sum of positive integers. 
    This function generates all unique partitions of n, ensuring that each partition 
    does not include any integer larger than the specified largest value.

    Parameters:
    n (int): The integer to be partitioned (must be greater than or equal to 0).
    largest (int): The largest integer that can be included in the partition (default is infinity).

    Returns:
    list: A list of lists, where each inner list represents a unique partition of n.
    """
    largest = min(n, largest)
    if not n:
        return [[]]  # Base case: the only partition of 0 is an empty partition
    res = []
    for i in range(1, largest + 1):
        rest = partitions(n - i, i - 1)  # Recursively partition the remaining value
        for r in rest:
            res.append([i] + r)  # Prepend the current integer to each partition of the remaining value

    return res

# Driver code to test the functions
if __name__ == "__main__":
    # Example usage
    n = 10  # The integer to be partitioned
    max_product = maximum_product(n)
    print(f"The maximum product of integers that sum up to {n} is: {max_product}")
