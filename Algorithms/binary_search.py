"""
This function implements a binary search algorithm.

Args:
    list: A list of sorted integers.
    value: The integer to search for.

Returns:
    The index of the value in the list, if found.
    None, if the value is not found in the list.
"""

def binarySearch(list: object, value: int) -> int:
    """Implements a binary search algorithm."""

    # Check if the list is empty.
    if not list:
        return None

    # Initialize the lower and upper bounds of the search.
    lower = 0
    high = len(list) - 1

    # Keep searching until the lower bound is greater than the upper bound.
    while lower <= high:
        # Calculate the middle index of the search range.
        middle = (lower + high) // 2

        # Check if the guess is equal to the value.
        guess = list[middle]
        if guess == value:
            return middle

        # If the guess is greater than the value, update the upper bound.
        elif guess > value:
            high = middle - 1

        # Otherwise, update the lower bound.
        else:
            lower = middle + 1

    # The value was not found in the list.
    return None


# Test the function.
my_list = [1, 3, 5, 7, 6]
print(binarySearch(my_list, 7))

