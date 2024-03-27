def find_distance(target_x, target_y):
    """
    Find the minimum number of moves required to reach a target cell (target_x, target_y) from the origin (0, 0).

    Args:
        target_x (int): The x-coordinate of the target cell.
        target_y (int): The y-coordinate of the target cell.

    Returns:
        int: The minimum number of moves required to reach the target cell.
    """
    # Initialize the layer number to 0
    layer_number = 0

    # Initialize the previous and current layers
    previous_layer, current_layer = set(), set([(0, 0)])

    # Iterate until the target cell is found
    while (target_x, target_y) not in current_layer:
        # Create a new set for the next layer
        next_layer = set()

        # Explore all cells in the current layer
        for (x, y) in current_layer:
            # Generate all possible moves from the current cell
            for next_cell in moves(x, y):
                # Add the next cell to the next layer if it hasn't been visited before
                if next_cell not in previous_layer:
                    next_layer.add(next_cell)

        # Update the previous and current layers
        previous_layer, current_layer = current_layer, next_layer

        # Increment the layer number
        layer_number += 1

    # Return the minimum distance (layer number)
    return layer_number

def moves(x, y):
    """
    Generate all possible moves from a given cell (x, y) according to the knight's move pattern in chess.

    Args:
        x (int): The x-coordinate of the current cell.
        y (int): The y-coordinate of the current cell.

    Returns:
        list: A list of tuples representing the coordinates of cells that can be reached from (x, y) by a knight's move.
    """
    # Define the knight's move pattern
    return [(x - 2, y + 1), (x - 2, y - 1), (x - 1, y + 2), (x - 1, y - 2),
            (x + 1, y + 2), (x + 1, y - 2), (x + 2, y + 1), (x + 2, y - 1)]

# Example usage
target_x = 3
target_y = 4
print("Minimum distance:", find_distance(target_x, target_y))
