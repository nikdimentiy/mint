import numpy

def solution(pieces):
    """
    This function simulates placing Tetris pieces on a 20x10 grid and counts the number of completed rows.

    Parameters:
    pieces (list of list of str): A list of Tetris pieces, where each piece is represented as a list of strings.
                                   Each string represents a row of the piece, with '#' indicating filled cells.

    Returns:
    int: The total number of completed rows after placing all pieces.
    """
    # Initializes variables
    res = 0  # Count of completed rows
    f = numpy.zeros((20, 10))  # The game grid initialized to zeros (empty)
    s = [0] * 20  # Row sums to track filled cells in each row

    # Loops over each piece in the input list
    for k, p in enumerate(pieces):
        w = -1  # Maximum row sum found for the current piece
        rd = -1  # Best position (column, row) to place the piece
        rs = -1  # Best rotation of the piece

        # Rotates and places each piece in the grid
        for r in range(4):  # Try all 4 rotations
            i = 0
            while i < 11 - len(p[0]):  # Iterate over possible starting columns
                c = j = 0
                while (not c) and j < 20 - len(p):  # Iterate over possible starting rows
                    j += 1
                    for n, line in enumerate(p):  # Check if the piece can be placed
                        for m, x in enumerate(line):
                            if x == '#' and f[j + n][i + m]:  # Collision check
                                c = 1  # Collision detected
                    j -= c  # Adjust row index if collision occurred
                o = sum(s[j:j + len(p)])  # Calculate the sum of filled cells in the target rows
                if o > w:  # Update best position if a better one is found
                    w, rd, rs = o, (i, j), r
                i += 1
            p = rot(p)  # Rotate the piece for the next iteration

        # Rotates the chosen piece and places it in the grid
        for _ in range(rs):
            p = rot(p)  # Apply the best rotation
        bi, bj = rd  # Best position to place the piece
        for n, line in enumerate(p):  # Place the piece on the grid
            for m, x in enumerate(line):
                if x == '#':
                    f[bj + n][bi + m] = k + 1  # Mark the grid with the piece index

        # Updates the state of the grid and counts completed rows
        s, nf = [*map(sum, f)], []  # Update row sums
        for n, s in enumerate(f):  # Check for completed rows
            if all(s):  # If the row is completely filled
                res += 1  # Increment completed rows count
            else:
                nf.append(f[n])  # Keep non-completed rows
        f = [[0] * 10 for _ in range(20 - len(nf))] + nf  # Update the grid
        s = [*map(sum, f)]  # Recalculate row sums

    # Returns the number of completed rows
    return res

# Rotates a matrix 90 degrees clockwise
def rot(m):
    return list(zip(*m[::-1]))

# Driver code to test the solution function
if __name__ == "__main__":
    # Example Tetris pieces
    pieces = [
        ["##", "##"],  # Square piece
        ["#..", "#..", "###"],  # L-shaped piece
        [".#.", "###", ".#."],  # T-shaped piece
        ["#..", "##", "..."],  # J-shaped piece
    ]

    # Call the solution function and print the result
    completed_rows = solution(pieces)
    print(f"Number of completed rows: {completed_rows}")
