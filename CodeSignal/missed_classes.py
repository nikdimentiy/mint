from typing import List


def solution(year: int, daysOfTheWeek: List[int], holidays: List[str]) -> int:
    """
    Counts the number of holidays that fall on specific days of the week in a given year.

    Args:
        year (int): The year for which to count the holidays.
        daysOfTheWeek (List[int]): A list of integers representing the days of the week to count. 
                                   Monday is 0 and Sunday is 6.
        holidays (List[str]): A list of strings representing the dates of the holidays in "MM-DD" format.

    Returns:
        int: The number of holidays that fall on the specified days of the week.

    """
    res = 0
    for date in holidays:
        m, d = map(int, date.split("-"))
        y = year
        y += m < 8
        res += weekday(y, m, d) + 1 in daysOfTheWeek
    return res
