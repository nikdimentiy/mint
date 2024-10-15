def elevator_distance(array):
    """
    Calculate the total distance traveled by an elevator given a list of floors.

    The function computes the sum of the absolute differences between consecutive 
    floors in the provided list. This represents the total distance the elevator 
    would travel if it moved from one floor to the next in the order specified 
    by the list.

    Parameters:
    array (list of int): A list of integers representing the floors the elevator 
                         visits in order.

    Returns:
    int: The total distance traveled by the elevator.
    
    Example:
    >>> elevator_distance([1, 3, 2, 5])
    4
    """
    # Calculate the total distance by summing the absolute differences
    return sum(abs(array[i + 1] - array[i]) for i in range(len(array) - 1))

# Driver code to test the function
if __name__ == "__main__":
    # Test cases
    test_cases = [
        [1, 3, 2, 5],  # Expected distance: 4 (|3-1| + |2-3| + |5-2| = 2 + 1 + 3)
        [0, 0, 0, 0],  # Expected distance: 0 (no movement)
        [1, 2, 3, 4],  # Expected distance: 3 (|2-1| + |3-2| + |4-3| = 1 + 1 + 1)
        [5, 1, 3, 7],  # Expected distance: 8 (|1-5| + |3-1| + |7-3| = 4 + 2 + 4)
    ]

    for i, test in enumerate(test_cases):
        result = elevator_distance(test)
        print(f"Test case {i + 1}: {test} => Distance: {result}")
