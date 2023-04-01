def solution(bishop1: str, bishop2: str):
    """
    Computes the positions of two bishops on a chessboard after they move along the
    diagonals of the squares they occupy, such that they end up on the opposite corners
    of the rectangular area bounded by the diagonals, or stay in their original positions
    if they are not on the same diagonal.

    Args:
        bishop1 (str): The position of the first bishop in the format '<letter><number>', where
            <letter> is a lowercase letter from 'a' to 'h', and <number> is an integer from 1 to 8.
        bishop2 (str): The position of the second bishop, in the same format as bishop1.

    Returns:
        List[str]: A list of two strings representing the new positions of the bishops after
            moving along the diagonals of the squares they occupy, or the original positions
            if they are not on the same diagonal. The positions are in the same format as the
            input positions, '<letter><number>'.
    """
    result = []
    a, x, b, y = ord(bishop1[0]), ord(
        bishop1[1]), ord(bishop2[0]), ord(bishop2[1])
    if a == b or x == y:
        return sorted([bishop1, bishop2])
    for t0 in range(97, 105):
        for t1 in range(49, 57):
            if (x - y) * (t0 - a) + (b - a) * (t1 - x) == 0:
                result.append(''.join([chr(t0), chr(t1)]))
    return sorted([result[0], result[-1]])
