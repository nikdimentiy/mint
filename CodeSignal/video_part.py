def solution(part: str, total: str):
    """
    Computes the fraction of a video that has been watched given the duration of the watched part and the total duration.

    Args:
        part (str): A string of the format "hh:mm:ss" representing the duration of the watched part.
        total (str): A string of the format "hh:mm:ss" representing the total duration of the video.

    Returns:
        List[int]: An array [a, b] where a / b is a reduced fraction representing the fraction of the video that has been watched.

    Raises:
        ValueError: If either part or total is not of the format "hh:mm:ss".

    """
    # split the input strings into hours, minutes, and seconds and convert to seconds
    try:
        part_hours, part_minutes, part_seconds = map(int, part.split(':'))
        total_hours, total_minutes, total_seconds = map(int, total.split(':'))
    except ValueError:
        raise ValueError(
            "Invalid input format. Expected format is 'hh:mm:ss'.")

    # compute the total number of seconds for the watched part and the total duration
    part_seconds += part_minutes * 60 + part_hours * 3600
    total_seconds += total_minutes * 60 + total_hours * 3600

    # compute the greatest common divisor of the two numbers
    gcd = find_gcd(part_seconds, total_seconds)

    # return the reduced fraction as an array
    return [part_seconds // gcd, total_seconds // gcd]


def find_gcd(a: int, b: int) -> int:
    """
    Finds the greatest common divisor of two numbers using the Euclidean algorithm.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The greatest common divisor of a and b.

    """
    if b == 0:
        return a
    return find_gcd(b, a % b)
