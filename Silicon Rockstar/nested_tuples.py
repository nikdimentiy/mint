def sum_numbers_in_tuple(t):
    """
    This function takes a tuple as input and returns the sum of all numbers in the tuple.
    The function handles nested tuples as well.

    :param t: A tuple that may contain integers, floats, and nested tuples.
    :return: The sum of all numbers in the tuple.
    """
    total = 0  # Initialize the total sum to 0

    # Iterate over each element in the tuple
    for element in t:
        # If the element is a tuple, recursively call this function and add the result to the total sum
        if isinstance(element, tuple):
            total += sum_numbers_in_tuple(element)
        # If the element is an integer or a float, add it to the total sum
        elif isinstance(element, (int, float)):
            total += element

    return total  # Return the total sum

# Define a tuple with some example values
things = (1, -7.5, ("pea", (5, "Xyz"), "queue"))

# Call the function with the example tuple and store the result
result = sum_numbers_in_tuple(things)

# Print the result
print(result)  # Output will be -1.5
