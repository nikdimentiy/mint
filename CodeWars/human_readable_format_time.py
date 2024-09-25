def format_duration(seconds):
    """
    Converts a duration in seconds to a human-readable format.

    Args:
        seconds (int): The duration in seconds.

    Returns:
        str: A string representing the duration in a human-readable format.

    Examples:
        >>> format_duration(3661)
        '1 hour, 1 minute and 1 second'
        >>> format_duration(60)
        '1 minute'
        >>> format_duration(0)
        'now'
    """

    # Define the units of time
    words = ["year", "day", "hour", "minute", "second"]

    # Handle the special case where the duration is 0 seconds
    if not seconds:
        return "now"
    else:
        # Calculate the number of years, days, hours, minutes, and seconds
        m, s = divmod(seconds, 60)  # minutes and seconds
        h, m = divmod(m, 60)  # hours and minutes
        d, h = divmod(h, 24)  # days and hours
        y, d = divmod(d, 365)  # years and days

        # Store the time units in a list
        time = [y, d, h, m, s]

        # Initialize an empty list to store the duration
        duration = []

        # Iterate over the time units and append the corresponding string to the duration list
        for x, i in enumerate(time):
            if i == 1:
                # If the unit is singular, append the unit without 's'
                duration.append(f"{i} {words[x]}")
            elif i > 1:
                # If the unit is plural, append the unit with 's'
                duration.append(f"{i} {words[x]}s")

        # Handle the cases where the duration list has 1, 2, or more elements
        if len(duration) == 1:
            # If there's only one unit, return it as is
            return duration[0]
        elif len(duration) == 2:
            # If there are two units, join them with ' and '
            return f"{duration[0]} and {duration[1]}"
        else:
            # If there are more than two units, join all but the last one with ', ' and the last one with ' and '
            return ", ".join(duration[:-1]) + " and " + duration[-1]


# Driver code
print(format_duration(3661))  # Output: 1 hour, 1 minute and 1 second
print(format_duration(60))  # Output: 1 minute
print(format_duration(0))  # Output: now
print(format_duration(31536001))  # Output: 1 year, 1 second
