def josephus(items, k):
    """
    The Josephus problem is a mathematical problem about a group of people standing in a circle and being eliminated one by one.

    Args:
        items: A list of items.
        k: The number of items to skip before eliminating one.

    Returns:
        A list of the items in the order in which they are eliminated.
    """

    """
    This function implements the Josephus problem algorithm.

    The algorithm works as follows:

    1. Start with a list of items.
    2. Set an index to the first item.
    3. Iterate over the list, counting k items at a time.
    4. On the kth item, remove it from the list.
    5. Repeat steps 3 and 4 until there is only one item left in the list.
    6. Return the remaining item.
    """

    result = []
    index = 0
    while len(items) > 0:
        # Count k items at a time.
        index = (index + k - 1) % len(items)

        # Remove the kth item from the list.
        result.append(items.pop(index))

    return result


# Driver code
items = ["A", "B", "C", "D", "E"]
k = 3
print(josephus(items, k))
