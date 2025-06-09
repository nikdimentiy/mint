from typing import List

def maze_runner(maze: List[List[int]], directions: List[str]) -> str:
    """
    Navigates a maze given as a 2D array and a list of directions to follow.

    Args:
    maze: A 2D array representing the maze. Each element of the array is an integer
          representing the type of the block. The meaning of the integers is:
              0 - Safe place to walk
              1 - Wall
              2 - Start Point
              3 - Finish Point
    directions: A list of directions to follow. Each direction is represented by a
                single character: "N" for North, "E" for East, "S" for South,
                and "W" for West.

    Returns:
    A string indicating the outcome of the maze navigation. The possible values are:
        "Finish" - if the finish point is reached before all directions are used
        "Dead" - if a wall is hit or the border of the maze is exceeded
        "Lost" - if all directions are used but the finish point is not reached

    Example:
    maze = [
        [1, 1, 1, 1, 1],
        [2, 0, 0, 1, 3],
        [1, 1, 0, 1, 1],
        [1, 1, 1, 1, 1]
    ]
    directions = ["E", "E", "S"]
    result = maze_runner(maze, directions)  # result will be "Finish"
    """

    # Find the starting point (2) in the maze
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if maze[row][col] == 2:
                x, y = col, row  # Store the starting coordinates

    # Follow the given directions
    for direction in directions:
        # Update the coordinates based on the direction
        if direction == "N":
            y -= 1
        elif direction == "E":
            x += 1
        elif direction == "S":
            y += 1
        elif direction == "W":
            x -= 1

        # Check if out of bounds
        if x < 0 or x >= len(maze[0]) or y < 0 or y >= len(maze):
            return "Dead"

        # Check if hit a wall
        if maze[y][x] == 1:
            return "Dead"

        # Check if reached the finish point
        if maze[y][x] == 3:
            return "Finish"

    # If all directions are used and finish point is not reached
    return "Lost"

# Driver code to test the maze_runner function
if __name__ == "__main__":
    # Define a sample maze
    maze = [
        [1, 1, 1, 1, 1],
        [2, 0, 0, 1, 3],
        [1, 1, 0, 1, 1],
        [1, 1, 1, 1, 1]
    ]
    
    # Define directions to navigate the maze
    directions = ["E", "E", "S"]
    
    # Call the maze_runner function and print the result
    result = maze_runner(maze, directions)
    print(result)  # Expected output: "Finish"

    # Test with another set of directions
    directions = ["E", "E", "N", "N"]
    result = maze_runner(maze, directions)
    print(result)  # Expected output: "Lost"

    # Test with a direction that hits a wall
    directions = ["E", "S", "S"]
    result = maze_runner(maze, directions)
    print(result)  # Expected output: "Dead"

    # Test with directions that go out of bounds
    directions = ["N", "N"]
    result = maze_runner(maze, directions)
    print(result)  # Expected output: "Dead"
