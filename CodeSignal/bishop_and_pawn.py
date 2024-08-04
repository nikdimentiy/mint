def solution(bishop: str, pawn: str) -> bool:
    """
    Determine if a bishop can attack a pawn on a chessboard.

    A bishop moves diagonally on the chessboard. This function checks if the 
    bishop and the pawn are positioned on the same diagonal.

    Parameters:
    bishop (str): The position of the bishop in algebraic notation (e.g., 'a1', 'h8').
    pawn (str): The position of the pawn in algebraic notation (e.g., 'a1', 'h8').

    Returns:
    bool: True if the bishop can attack the pawn, False otherwise.
    """
    # Convert the bishop and pawn coordinates to column and row indices
    bishop_col, bishop_row = ord(bishop[0]), int(bishop[1])
    pawn_col, pawn_row = ord(pawn[0]), int(pawn[1])

    # Check if the bishop and pawn are on the same diagonal
    return abs(bishop_col - pawn_col) == abs(bishop_row - pawn_row)

# Driver code to test the solution function
if __name__ == "__main__":
    # Test cases
    test_cases = [
        ('a1', 'b2'),  # True: same diagonal
        ('c3', 'f6'),  # True: same diagonal
        ('h8', 'g7'),  # True: same diagonal
        ('d4', 'e5'),  # True: same diagonal
        ('a1', 'h8'),  # False: not on the same diagonal
        ('b2', 'd4'),  # False: not on the same diagonal
    ]

    # Execute test cases
    for bishop, pawn in test_cases:
        result = solution(bishop, pawn)
        print(f"Bishop at {bishop} can attack pawn at {pawn}: {result}")
