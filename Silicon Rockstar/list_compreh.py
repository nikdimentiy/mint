# This code creates a list of tuples (x, y) where x and y are integers ranging from 0 to 2, 
# with the condition that y is greater than or equal to x.

# Define a list comprehension to generate the desired list of tuples.
z = [(x, y) for x in range(3) for y in range(3) if y >= x]

# Print the resulting list.
print(z)

# another way -->

def generate_z():
    """
    Generate a list of tuples (x, y) where y is greater than or equal to x,
    for all values of x and y in the range [0, 2].

    Returns:
        list: A list of tuples (x, y) where y >= x.

    """
    z = []  # Create an empty list to store the tuples (x, y)

    # Iterate over the range of x values
    for x in range(3):
        # Iterate over the range of y values
        for y in range(3):
            # Check if y is greater than or equal to x
            if y >= x:
                # Append the tuple (x, y) to the list z
                z.append((x, y))

    return z


# Call the function to generate the list z
z = generate_z()

# Print the resulting list z
print(z)
