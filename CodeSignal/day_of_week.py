def solution(bd: str) -> int:
    """
    Given a birthday date, return the number of years until the same day of the week will occur again.

    Args:
    - bd (str): A string representing the correct date in the format mm-dd-yyyy, where mm is the number of month (1-based, 
                i.e. 01 for January, 02 for February and so on), dd is the day, and yyyy is the year.

    Returns:
    - int: An integer describing the number of years until the birthday falls on the same day of the week.

    Notes:
    - This function assumes that the input date is valid and in the correct format.
    - The function uses the Gregorian calendar, which is the most widely used calendar in the world.
    """

    m, d, y = [int(i) for i in bd.split('-')]
    is_leap_day = (m == 2 and d == 29)

    def is_leap(y: int) -> bool:
        """Return True if the given year is a leap year, otherwise False."""
        return bool((not (y % 4) and y % 100) or not (y % 400))

    def days(y: int) -> int:
        """Return the number of days in the given year."""
        return 366 if (is_leap(y) and m < 3) or (is_leap(y + 1) and m > 2) else 365

    start = days(y)
    next_y = y + 1
    while start % 7 or is_leap_day:
        start += days(next_y)
        next_y += 1

        if not (start % 7) and is_leap_day and is_leap(next_y):
            break

    return next_y - y


# Driver code
if __name__ == "__main__":
    # Test cases
    test_cases = [
        ("02-29-2020", 4),  # Leap day
        ("12-25-2020", 6),  # Non-leap day
        ("01-01-2020", 5),  # Non-leap day
    ]

    for bd, expected in test_cases:
        result = solution(bd)
        print(f"Input: {bd}, Expected: {expected}, Result: {result}")
        assert result == expected, f"Test case failed: {bd}"
