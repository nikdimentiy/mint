def calculate_new_positions(i, j):
    """
    Calculate the new positions based on the current coordinates (i, j).
    
    This function computes the positions that can be reached from the 
    current position by moving one step in each of the four cardinal 
    directions: up, right, down, and left.

    Parameters:
    i (int): The current row index.
    j (int): The current column index.

    Returns:
    list of tuples: A list containing the new positions as (row, column) tuples.
    """
    d_i = (-1, 0, 1, 0)  # Direction offsets for row (i): up, right, down, left
    d_j = (0, 1, 0, -1)  # Direction offsets for column (j): up, right, down, left
    new_positions = []  # List to store new positions

    for k in range(4):  # Iterate over the four possible directions
        new_i = i + d_i[k]  # Calculate new row index
        new_j = j + d_j[k]  # Calculate new column index
        new_positions.append((new_i, new_j))  # Append the new position to the list

    return new_positions  # Return the list of new positions

# Driver code to demonstrate the function
if __name__ == "__main__":
    i, j = 2, 2  # Starting coordinates
    positions = calculate_new_positions(i, j)  # Calculate new positions
    print("Current position:", (i, j))
    print("New positions:", positions)  # Output the new positions
