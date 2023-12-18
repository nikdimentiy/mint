def find_rightmost_value(seq, x):
    """
    Check if the given value x is present at the rightmost position in the sequence.

    Args:
        seq (list): A sequence of values.
        x: The value to be searched for.

    Returns:
        bool: True if x is found at the rightmost position, False otherwise.
    """
    # Check if the value x is in the reversed sequence
    return x in reversed(seq)

# Driver code to test the function
sequence = [1, 2, 3, 4, 5, 4, 3, 2, 1]
value = 4
result = find_rightmost_value(sequence, value)
print(f"The value {value} is found at the rightmost position: {result}")
