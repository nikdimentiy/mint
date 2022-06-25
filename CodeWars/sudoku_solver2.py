def update(spots, row, col, l):
    if (row, col) in spots:
        spots[(row, col)] = spots[(row, col)].difference(set(l))


def sudoku(puzzle):
    """return the solved puzzle as a 2d array of 9 x 9"""
    spots = {}
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == 0:
                spots[(row, col)] = set(range(1, 10))

    while len(spots) > 0:
        for (row, col) in spots:
            r = int(row / 3) * 3
            c = int(col / 3) * 3
            square = puzzle[r][c:c+3] + puzzle[r+1][c:c+3] + puzzle[r+2][c:c+3]
            update(spots, row, col, puzzle[row])
            update(spots, row, col, zip(*puzzle)[col])
            update(spots, row, col, square)

        for (row, col) in [(r, c) for (r, c) in spots]:
            if len(spots[(row, col)]) == 1:
                puzzle[row][col] = spots[(row, col)].pop()
                del spots[(row, col)]
    return puzzle
