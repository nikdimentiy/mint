from typing import List


def solution(takeOffTime: str, minutes: List[int]) -> int:
    """
    Counts the number of times you will be able to celebrate New Year's Day
    while flying across multiple time zones.

    Args:
        takeOffTime (str): The take off time in the 24-hour format "HH:MM".
            The "00:00" time corresponds to the midnight of 31st of December / 1st of January.
        minutes (List[int]): A strictly increasing list of integers.
            minutes[i] stands for the number of minutes from the take off to crossing the ith time zone border.

    Returns:
        int: The number of times you will be able to celebrate New Year's Day.

    Example:
        >>> solution("23:35", [60, 90, 140])
        3
    """
    minutes[1:] = [minutes[i]-minutes[i-1] for i in range(1, len(minutes))]
    h, m = [int(x) for x in takeOffTime.split(':')]
    t = h*60 + m
    if t == 0:
        t = 1440
    T = []
    for M in minutes:
        t += M
        T += t,
        t -= 60
        if t > 1440:
            break
    x = len([x for x in T if x >= 1440])
    if t <= 1440:
        x += 1
    return x
