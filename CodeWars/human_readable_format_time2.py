def format_duration(seconds):
    """
    Converts a duration in seconds into a human-readable format.

    Parameters:
    seconds (int): The duration in seconds to be converted.

    Returns:
    str: A string representing the duration in years, days, hours, minutes, and seconds.
    
    Example:
    >>> format_duration(3662)
    '1 hour, 1 minute and 2 seconds'
    >>> format_duration(0)
    'now'
    """
    # If the input is 0 seconds, return "now"
    if seconds == 0:
        return "now"
    
    # Define the time units and their corresponding values in seconds
    units = (
        (31536000, "year"),
        (86400, "day"),
        (3600, "hour"),
        (60, "minute"),
        (1, "second")
    )
    
    # Initialize an empty list to hold the formatted time components
    ts, t = [], seconds
    
    # Iterate over each time unit to calculate the number of each unit in the given seconds
    for unit in units:
        u, t = divmod(t, unit[0])  # Get the quotient and remainder
        # If the unit count is not zero, format it and add to the list
        if u != 0:
            ts.append("{} {}{}".format(u, unit[1], "s" if u > 1 else ""))
    
    # Join the formatted components with commas and "and" for the last element
    return ", ".join(ts[:-1]) + (" and " if len(ts) > 1 else "") + ts[-1]

# Driver code to test the function
if __name__ == "__main__":
    # Test cases
    print(format_duration(3662))  # Output: '1 hour, 1 minute and 2 seconds'
    print(format_duration(0))      # Output: 'now'
    print(format_duration(62))     # Output: '1 minute and 2 seconds'
    print(format_duration(120))     # Output: '2 minutes'
    print(format_duration(31536000)) # Output: '1 year'
    print(format_duration(31536061)) # Output: '1 year, 1 second'
