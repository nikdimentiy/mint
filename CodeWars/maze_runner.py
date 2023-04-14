# CodeWars task: solution --> https://www.codewars.com/kata/58663693b359c4a6560001d6/train/python

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

    Raises:
    None
    """

    # find starting point
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if maze[row][col] == 2:
                x, y = col, row

    # follow directions
    for direction in directions:
        if direction == "N":
            y -= 1
        elif direction == "E":
            x += 1
        elif direction == "S":
            y += 1
        elif direction == "W":
            x -= 1

        # check if out of bounds
        if x < 0 or x >= len(maze[0]) or y < 0 or y >= len(maze):
            return "Dead"

        # check if hit a wall
        if maze[y][x] == 1:
            return "Dead"

        # check if reached finish
        if maze[y][x] == 3:
            return "Finish"

    return "Lost"
