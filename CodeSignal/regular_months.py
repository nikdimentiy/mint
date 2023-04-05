from datetime import datetime


def solution(currMonth: str) -> str:
    """
    Finds the earliest regular month after the given month and returns it as a string in the format 'mm-yyyy'.

    Args:
    currMonth (str): A string representing the current month in the format 'mm-yyyy'.

    Returns:
    str: A string representing the earliest regular month after the given month in the format 'mm-yyyy'.
    """

    # Parse the current month string to get month and year integers
    d = datetime.strptime(currMonth, '%m-%Y')
    m = d.month
    y = d.year

    # Loop through each month until a regular month with a Monday is found
    while True:
        # Increment month and year as necessary
        if m % 12 == 0:
            y += 1
        m = (m % 12) + 1

        # Create a datetime object for the first day of the next month
        d = datetime(y, m, 1)

        # Check if the first day of the month is a Monday
        if d.weekday() == 0:
            # If it is, return the month and year as a formatted string
            return datetime.strftime(d, '%m-%Y')
