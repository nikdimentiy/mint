def solution(cell: str) -> int:
    """
    Given a position of a knight on the standard chessboard, returns the number of different moves the knight can perform.

    Args:
    - cell: a string consisting of 2 letters - coordinates of the knight on an 8 × 8 chessboard in chess notation.

    Returns:
    - An integer representing the number of different moves the knight can perform from the given position.

    Constraints:
    - cell.length = 2
    - 'a' ≤ cell[0] ≤ 'h'
    - 1 ≤ cell[1] ≤ 8
    """

    # convert chess notation to row and column numbers
    col = ord(cell[0]) - ord('a') + 1
    row = int(cell[1])

    # count number of valid moves
    count = 0
    for dr, dc in [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]:
        r = row + dr
        c = col + dc
        if 1 <= r <= 8 and 1 <= c <= 8:
            count += 1

    return count
