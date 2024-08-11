from typing import List

def expand(notation: str) -> str:
    """
    Replaces the digits in the notation with that number of 1s.

    Args:
    - notation: A string representing the chess board position in John's notation.

    Returns:
    A string with digits replaced with that number of 1s.
    """
    for i in range(1, 9):
        notation = notation.replace(str(i), '1' * i)
    return notation


def contract(notation: str) -> str:
    """
    Replaces a consecutive string of 1s with the length of the string.

    Args:
    - notation: A string with 1s that represent empty spaces on the chess board.

    Returns:
    A string with consecutive 1s replaced with the length of the string.
    """
    for i in list(range(1, 9))[::-1]:
        notation = notation.replace('1' * i, str(i))
    return notation


def transpose(ls: List[str]) -> List[str]:
    """
    Transposes a list of strings.

    Args:
    - ls: A list of strings representing rows on the chess board.

    Returns:
    A list of strings representing columns on the chess board.
    """
    return [''.join(ls[i][j] for i in range(len(ls)))[::-1] for j in range(len(ls[0]))]


def solution(notation: str) -> str:
    """
    Transposes and rotates the chess board position 90 degrees clockwise.

    Args:
    - notation: A string representing the chess board position in John's notation.

    Returns:
    A string representing the rotated chess board position in John's notation.
    
    Example:
    If the input notation is "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR",
    the output will be "RNBQKBNR/PPPPPPPP/8/8/8/8/pppppppp/rnbqkbnr".
    """
    # Expand notation by replacing digits with that number of 1s
    expanded = expand(notation)

    # Split notation into rows, transpose the rows, and join the columns
    transposed = transpose(expanded.split('/'))

    # Contract notation by replacing consecutive 1s with the length of the string
    contracted = contract('/'.join(transposed))

    return contracted


# Driver code to demonstrate the functionality
if __name__ == "__main__":
    # Example chess board position in John's notation
    notation = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
    
    # Print the original notation
    print("Original Notation:")
    print(notation)
    
    # Get the rotated notation
    rotated_notation = solution(notation)
    
    # Print the rotated notation
    print("\nRotated Notation:")
    print(rotated_notation)
