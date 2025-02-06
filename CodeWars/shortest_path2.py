def path_finder(maze):
    """
    Determines the minimum number of turns required to navigate from the top-left corner
    to the bottom-right corner of a maze represented as a string. The maze consists of 
    walls ('W') and open paths ('.'). The function returns the number of turns needed 
    to reach the destination, or False if the destination is unreachable.

    Parameters:
    maze (str): A string representation of the maze, where each line represents a row.

    Returns:
    int or bool: The number of turns to reach the bottom-right corner, or False if unreachable.
    """
    
    # Split the maze string into a list of rows
    lst = maze.split('\n')
    # Get the dimensions of the maze
    X, Y = len(lst) - 1, len(lst[0]) - 1
    
    # Initialize the set of seen positions (walls and starting point)
    seen = {(x, y) for x, row in enumerate(lst)
            for y, c in enumerate(row) if c == 'W'} | {(0, 0)}
    
    # Define the end position and initialize the bag of positions to explore
    end, bag, turn = (X, Y), {(0, 0)}, 0

    # While there are positions to explore and the end is not reached
    while bag and end not in bag:
        # Generate new positions to explore from the current bag
        bag = {(a, b) for a, b in {(x + dx, y + dy) for x, y in bag 
                                   for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0))}
               if 0 <= a <= X and 0 <= b <= Y} - seen
        
        # Mark the newly seen positions
        seen |= bag
        # Increment the turn count
        turn += 1

    # Return the number of turns if reachable, otherwise return False
    return bool(bag) and turn


# Driver code to test the path_finder function
if __name__ == "__main__":
    # Example maze
    maze = "...\n.W.\n..."
    print("Maze:")
    print(maze)
    result = path_finder(maze)
    print("Number of turns to reach the end:", result)

    # Another example with a wall blocking the path
    maze_with_wall = "...\nWWW\n..."
    print("\nMaze with wall:")
    print(maze_with_wall)
    result = path_finder(maze_with_wall)
    print("Number of turns to reach the end:", result)

    # Example where the end is unreachable
    unreachable_maze = "W..\n.W.\n..W"
    print("\nUnreachable maze:")
    print(unreachable_maze)
    result = path_finder(unreachable_maze)
    print("Number of turns to reach the end:", result)
