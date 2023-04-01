def solution(bishop: str, pawn: str) -> bool:
    # Convert the bishop and pawn coordinates to column and row indices
    bishop_col, bishop_row = ord(bishop[0]), int(bishop[1])
    pawn_col, pawn_row = ord(pawn[0]), int(pawn[1])

    # Check if the bishop and pawn are on the same diagonal
    return abs(bishop_col - pawn_col) == abs(bishop_row - pawn_row)
