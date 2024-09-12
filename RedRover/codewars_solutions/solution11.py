def to24hourtime(hour: int or str, minute: int or str, period: str) -> str:
    """
    Convert 12-hour time format to 24-hour time format.

    Parameters:
    hour (int or str): The hour in 12-hour format (1-12).
    minute (int or str): The minute (0-59).
    period (str): 'am' or 'pm' indicating the period of the day.

    Returns:
    str: The time in 24-hour format as a four-digit string.
    """
    # Convert hour and minute to integers
    hour = int(hour)
    minute = int(minute)

    # Handle the conversion based on the period
    if period.lower() == 'am':
        if hour == 12:  # 12 AM is midnight
            hour = 0
    else:  # PM case
        if hour != 12:  # 12 PM is noon
            hour += 12

    # Format the hour and minute to a four-digit string
    return f"{hour:02d}{minute:02d}"

# Example usage:
print(to24hourtime(8, 30, 'am'))  # Output: "0830"
print(to24hourtime(8, 30, 'pm'))  # Output: "2030"
print(to24hourtime(12, 0, 'am'))  # Output: "0000"
print(to24hourtime(12, 0, 'pm'))  # Output: "1200"
print(to24hourtime('8', '30', 'am'))  # Output: "0830"
print(to24hourtime('8', '30', 'pm'))  # Output: "2030"
print(to24hourtime('12', '0', 'am'))  # Output: "0000"
print(to24hourtime('12', '0', 'pm'))  # Output: "1200"