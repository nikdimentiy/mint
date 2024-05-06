def josephus(items, k):
    """
    Solves the Josephus problem for a given list of items and a step size.
    
    The Josephus problem is a classic problem where people stand in a circle and 
    every k-th person is removed until there is only one person left. This function 
    returns the sequence of eliminations based on the step size and the initial list.

    Parameters:
    - items: list of any type
      The initial list of people or items in the circle.
    - k: int
      The step size, indicating the k-th person to be removed.

    Returns:
    - list
      A list of items in the order they were removed.
    """
    if len(items) == 0:
        return []
    
    # Calculate the index of the person to be removed
    index_to_remove = (k - 1) % len(items)
    
    # Get the item to be removed
    removed_item = items[index_to_remove]
    
    # Slice the list to exclude the removed item
    # and create a new circle that continues the Josephus process
    remaining_items = items[index_to_remove + 1:] + items[:index_to_remove]

    # Recursively solve the Josephus problem with the updated list
    # and the same step size
    return [removed_item] + josephus(remaining_items, k)


# Driver code to test the josephus function
if __name__ == "__main__":
    # Test case 1: List of numbers with step size 3
    items = list(range(1, 8))  # People numbered from 1 to 7
    step_size = 3
    print("Josephus order:", josephus(items, step_size))

    # Test case 2: List of characters with step size 2
    characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    step_size = 2
    print("Josephus order:", josephus(characters, step_size))

    # Test case 3: Single item in the list with any step size
    single_item = ['X']
    step_size = 4
    print("Josephus order:", josephus(single_item, step_size))

    # Test case 4: Empty list
    empty_list = []
    step_size = 5
    print("Josephus order:", josephus(empty_list, step_size))
