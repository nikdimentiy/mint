def solution(cell: str) -> int:
    """
    Given a position of a knight on the standard chessboard, returns the number of different moves the knight can perform.

    Args:
    - cell: a string consisting of 2 characters - the first character is a letter from 'a' to 'h' representing the column,
             and the second character is a digit from '1' to '8' representing the row of the knight's position on an 8 × 8 chessboard.

    Returns:
    - An integer representing the number of different moves the knight can perform from the given position.

    Constraints:
    - cell.length = 2
    - 'a' ≤ cell[0] ≤ 'h'
    - 1 ≤ cell[1] ≤ 8

    Example:
    >>> solution("e4")
    8
    >>> solution("h8")
    2
    >>> solution("a1")
    3
    """
    
    # Convert chess notation to row and column numbers
    col = ord(cell[0]) - ord('a') + 1
    row = int(cell[1])

    # Count number of valid moves
    count = 0
    for dr, dc in [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]:
        r = row + dr
        c = col + dc
        if 1 <= r <= 8 and 1 <= c <= 8:
            count += 1

    return count

# Driver code to test the solution function
if __name__ == "__main__":
    test_cases = ["e4", "h8", "a1", "d5", "b2"]
    for cell in test_cases:
        print(f"Number of moves for knight at {cell}: {solution(cell)}")
