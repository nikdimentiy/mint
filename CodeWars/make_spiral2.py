def spiralize(size):
    """
    Generate a spiral matrix of 1s and 0s.

    The function creates a 2D list (matrix) of size `size x size` where:
        - 1 represents a path spiraling outwards from the center.
        - 0 represents empty spaces.

    The spiral is constructed by moving in a clockwise direction, turning
    when it encounters a boundary or an already filled cell. The process continues
    until no further moves are possible.

    Parameters:
    ----------
    size : int
        The size of the square matrix to generate. Must be a positive integer.

    Returns:
    -------
    list of list of int
        A 2D list representing the spiral matrix.

    Example:
    --------
    For size = 5, the output will be:
    [
        [1, 1, 1, 1, 1],
        [0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1]
    ]
    """

    # Helper function to check if a given coordinate is within the bounds of the matrix
    def on_board(x, y):
        return 0 <= x < size and 0 <= y < size

    # Helper function to check if a given coordinate contains a '1'
    def is_one(x, y):
        return on_board(x, y) and spiral[y][x] == 1

    # Helper function to determine if the next move is valid
    def can_move():
        # Ensure the next position is on the board and does not collide with existing '1's
        return on_board(x + dx, y + dy) and not (
            is_one(x + 2 * dx, y + 2 * dy) or  # Two steps ahead
            is_one(x + dx - dy, y + dy + dx) or  # Diagonal left
            is_one(x + dx + dy, y + dy - dx)  # Diagonal right
        )

    # Initialize the spiral matrix with all zeros
    spiral = [[0 for _ in range(size)] for _ in range(size)]

    # Starting position and direction
    x, y = -1, 0  # Start just outside the top-left corner
    dx, dy = 1, 0  # Initial direction: move right
    turns = 0  # Count consecutive turns (used to detect when the spiral is complete)

    # Spiral generation loop
    while turns < 2:  # Stop when two consecutive turns fail
        if can_move():  # If the next move is valid
            x += dx  # Move in the current direction
            y += dy
            spiral[y][x] = 1  # Mark the current position as part of the spiral
            turns = 0  # Reset the turn counter
        else:
            # Change direction (rotate 90 degrees clockwise)
            dx, dy = -dy, dx
            turns += 1  # Increment the turn counter

    return spiral


# Driver code to test the function
if __name__ == "__main__":
    # Test the function with different sizes
    sizes = [5, 6, 7]

    for size in sizes:
        print(f"Spiral matrix of size {size}:")
        spiral_matrix = spiralize(size)
        for row in spiral_matrix:
            print(row)
        print()  # Add a blank line between outputs
