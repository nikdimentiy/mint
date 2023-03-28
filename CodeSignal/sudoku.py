def solution(grid):
    # Check each row
    for row in grid:
        if len(set(row)) != 9:
            return False

    # Check each column
    for col in range(9):
        if len(set(grid[row][col] for row in range(9))) != 9:
            return False

    # Check each sub-grid
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            subgrid = [grid[x][y]
                       for x in range(i, i+3) for y in range(j, j+3)]
            if len(set(subgrid)) != 9:
                return False

    # If all checks pass, then the grid is a correct solution to Sudoku
    return True
