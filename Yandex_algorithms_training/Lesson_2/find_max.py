def find_max(seq):
    """
    Find the maximum value in the given sequence.

    Args:
        seq (list): A sequence of values.

    Returns:
        int: The maximum value in the sequence.
    """
    # Initialize the answer with the first element of the sequence
    ans = seq[0]

    # Iterate through the sequence
    for i in range(len(seq)):
        # Check if the current element is greater than the current maximum
        if seq[i] > ans:
            # Update the maximum value
            ans = seq[i]

    # Return the maximum value found in the sequence
    return ans


# Driver code to test the function
sequence = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
result = find_max(sequence)
print(f"The maximum value in the sequence is: {result}")
