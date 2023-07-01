def findmax(sequence):
    """
    Finds the maximum and second maximum elements in a sequence of numbers.

    Parameters:
    sequence (list): A list of numbers.

    Returns:
    tuple: A tuple of two numbers, the maximum and second maximum elements in the sequence.

    Raises:
    ValueError: If the sequence is empty or has only one element.
    """

    # Check if the sequence is empty
    if len(sequence) == 0:
        raise ValueError("Sequence must not be empty")

    # Check if the sequence has only one element
    if len(sequence) == 1:
        raise ValueError("Sequence must have at least two elements")

    # Initialize the maximum and second maximum elements with the first two elements of the sequence
    max_1 = max(sequence[0], sequence[1])
    max_2 = min(sequence[0], sequence[1])

    # Loop through the rest of the sequence
    for i in range(2, len(sequence)):
        # If the current element is greater than the maximum element, update both max_1 and max_2
        if sequence[i] > max_1:
            max_2 = max_1
            max_1 = sequence[i]
        # If the current element is greater than the second maximum element, update only max_2
        elif sequence[i] > max_2:
            max_2 = sequence[i]

    # Return the maximum and second maximum elements as a tuple
    return (max_1, max_2)
