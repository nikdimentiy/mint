from collections import deque

SYMBOL = '.'
CHECKED_SYMBOL = 'x'

def path_finder(maze: str) -> int or bool:
    """
    Find the shortest path through a square maze represented as a string.

    Args:
        maze (str): A string representation of the maze, where '.' indicates open paths 
                    and 'x' indicates checked paths.

    Returns:
        int: The number of steps in the shortest path if a path exists.
        bool: False if no path exists from the top-left to the bottom-right corner.
    """
    # Convert maze string into a 2D list for processing
    table = list(map(list, maze.split("\n")))
    max_len = len(table[0]) - 1  # Dimension of the square maze
    
    # If the maze is a single cell, the path is trivially 0 steps
    if max_len == 0:
        return 0

    # Stack for DFS-like traversal
    stack = deque()
    stack.append([0, 0])
    
    # Dictionary to keep track of visited nodes and their predecessors
    history = {(0, 0): None}
    result = False

    # Traverse the maze using a stack
    while stack:
        element = stack.pop()
        y, x = element  # Decompose coordinates for readability

        # Check if the bottom-right corner is reached
        if element == [max_len, max_len]:
            result = True
            break

        # Skip if the current cell has already been checked
        if table[y][x] == CHECKED_SYMBOL:
            continue

        # Explore neighboring cells if within bounds and not already checked
        # Check right
        if x + 1 <= max_len and table[y][x + 1] == SYMBOL:
            stack.appendleft([y, x + 1])
            history[y, x + 1] = [y, x]

        # Check down
        if y + 1 <= max_len and table[y + 1][x] == SYMBOL:
            stack.appendleft([y + 1, x])
            history[y + 1, x] = [y, x]

        # Check up
        if y - 1 >= 0 and table[y - 1][x] == SYMBOL:
            stack.appendleft([y - 1, x])
            history[y - 1, x] = [y, x]

        # Check left
        if x - 1 >= 0 and table[y][x - 1] == SYMBOL:
            stack.appendleft([y, x - 1])
            history[y, x - 1] = [y, x]

        # Mark current cell as checked
        table[y][x] = CHECKED_SYMBOL

    # If no path was found, return False
    if not result:
        return False

    # Trace back the path from the bottom-right corner to the top-left
    current = history[max_len, max_len]
    path = [current]

    while current != [0, 0]:
        if current is None:
            break

        y, x = current
        current = history[y, x]
        path.append(current)

    # Return the number of steps in the shortest path
    return len(path)

# Driver code
if __name__ == "__main__":
    # Example maze where '.' is an open path and '#' is a wall
    maze = (
        "....\n"
        ".##.\n"
        ".##.\n"
        "...."
    )

    result = path_finder(maze)
    if result:
        print(f"The shortest path has {result} steps.")
    else:
        print("No path exists through the maze.")
