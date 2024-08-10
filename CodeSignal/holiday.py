from typing import List

def solution(x: int, weekDay: str, month: str, yearNumber: int) -> int:
    """
    Calculates the day of the month on which a specified occurrence of a holiday will be celebrated 
    in a given year based on the day of the week.

    Args:
    - x (int): A positive integer representing the occurrence of the day of the week within the month (1 for the first occurrence, 2 for the second, etc.).
    - weekDay (str): A string representing the name of a day of the week (e.g., "Monday", "Tuesday").
    - month (str): A string representing the name of a month (e.g., "January", "February").
    - yearNumber (int): An integer representing the year for which to calculate the holiday date.

    Returns:
    - int: The day of the month on which the holiday will be celebrated in the given year, 
           or -1 if there is no such occurrence in that month.
    """

    # Define a dictionary to map month names to their corresponding lengths.
    month_lengths = {
        "January": 31,
        "February": 28,
        "March": 31,
        "April": 30,
        "May": 31,
        "June": 30,
        "July": 31,
        "August": 31,
        "September": 30,
        "October": 31,
        "November": 30,
        "December": 31
    }

    # Define a dictionary to map day of the week names to their corresponding numerical values.
    weekDay_to_num = {
        "Monday": 0,
        "Tuesday": 1,
        "Wednesday": 2,
        "Thursday": 3,
        "Friday": 4,
        "Saturday": 5,
        "Sunday": 6
    }

    # Get the numerical value of the day of the week.
    weekDay_num = weekDay_to_num[weekDay]

    # Get the length of the month.
    month_length = month_lengths[month]

    # Check if the year is a leap year.
    is_leap_year = (yearNumber % 4 == 0 and yearNumber % 100 != 0) or yearNumber % 400 == 0

    # Adjust the length of February if it's a leap year.
    if month == "February" and is_leap_year:
        month_length = 29

    # Calculate the number of occurrences of the day of the week in the month.
    num_occurrences = 0
    for day in range(1, month_length + 1):
        if weekDay_num == (day - 1) % 7:
            num_occurrences += 1
            if num_occurrences == x:
                return day

    # If there were not enough occurrences of the day of the week, return -1.
    return -1

# Driver code to test the solution function
if __name__ == "__main__":
    # Example test cases
    print(solution(1, "Monday", "January", 2023))  # Expected output: 2 (1st Monday of January 2023)
    print(solution(2, "Wednesday", "February", 2024))  # Expected output: 14 (2nd Wednesday of February 2024)
    print(solution(3, "Friday", "March", 2023))  # Expected output: 17 (3rd Friday of March 2023)
    print(solution(5, "Sunday", "April", 2023))  # Expected output: -1 (5th Sunday of April 2023 does not exist)
