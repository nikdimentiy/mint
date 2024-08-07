def solution(grid, path):
    """
    Simulates a game of 2048 based on the given grid and path of arrow key presses.

    Args:
        grid (list of lists): A 4x4 grid representing the initial state of the game.
        path (str): A string of 'U', 'D', 'L', and 'R' characters representing the sequence of arrow key presses.

    Returns:
        list of lists: The final state of the game grid after applying the given path of arrow key presses.

    Notes:
        The game is simulated by iterating over the arrow key presses in the path, applying the corresponding transformations to the grid, and merging adjacent tiles with the same value.
    """
    # iterate over the arrow key presses in the path
    for d in path:
        # if the direction is Up or Down, transpose the grid
        if d in "UD":
            grid = [list(x) for x in zip(*grid)]
        # if the direction is Right or Down, reverse each row in the grid
        if d in "RD":
            grid = [row[::-1] for row in grid]

        # create a new grid to hold the updated state
        ngrid = []
        # iterate over each row in the grid
        for row in grid:
            nrow = []
            lmerged = False
            # iterate over each tile in the row
            for t in row:
                # if the tile is not empty, add it to the new row
                if t:
                    nrow.append(t)
                    # if the last two tiles in the new row can merge, merge them
                    if not lmerged and len(nrow) >= 2 and nrow[-2] == nrow[-1]:
                        nrow.append(nrow.pop() + nrow.pop())
                        lmerged = True
                    else:
                        lmerged = False
            # add zeroes to the end of the new row to fill it out to length 4
            ngrid.append(nrow + [0 for _ in range(4 - len(nrow))])

        # if the direction is Right or Down, reverse each row in the new grid
        if d in "RD":
            ngrid = [row[::-1] for row in ngrid]
        # if the direction is Up or Down, transpose the new grid
        if d in "UD":
            ngrid = [list(x) for x in zip(*ngrid)]
        # set the new grid as the updated state of the game
        grid = ngrid
    # return the final state of the game grid
    return grid

# Driver code
grid = [
    [2, 0, 0, 0],
    [0, 2, 0, 0],
    [0, 0, 2, 0],
    [0, 0, 0, 2]
]
path = "ULDR"
print("Initial grid:")
for row in grid:
    print(row)
print("\nPath:", path)
print("\nFinal grid:")
for row in solution(grid, path):
    print(row)
