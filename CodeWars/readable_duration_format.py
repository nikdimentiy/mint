def format_duration(seconds):
    """
    Convert a duration in seconds into a human-readable format.

    Parameters:
    seconds (int): The duration in seconds.

    Returns:
    str: A human-readable string representing the duration.
         If the duration is 0, returns "now".
    """
    # Define the time units in order of years, days, hours, minutes, and seconds
    words = ["year", "day", "hour", "minute", "second"]

    # If the input is 0 seconds, return "now"
    if not seconds:
        return "now"
    else:
        # Calculate the number of minutes and remaining seconds
        m, s = divmod(seconds, 60)
        # Calculate the number of hours and remaining minutes
        h, m = divmod(m, 60)
        # Calculate the number of days and remaining hours
        d, h = divmod(h, 24)
        # Calculate the number of years and remaining days
        y, d = divmod(d, 365)

        # Create a list of time components
        time = [y, d, h, m, s]

        # Initialize a list to hold the duration components
        duration = []

        # Build the duration string based on the non-zero time components
        for x, i in enumerate(time):
            if i == 1:
                duration.append(f"{i} {words[x]}")
            elif i > 1:
                duration.append(f"{i} {words[x]}s")

        # Format the output based on the number of components
        if len(duration) == 1:
            return duration[0]
        elif len(duration) == 2:
            return f"{duration[0]} and {duration[1]}"
        else:
            return ", ".join(duration[:-1]) + " and " + duration[-1]

# Driver code to test the function
if __name__ == "__main__":
    test_cases = [0, 62, 3662, 31536000, 86461, 123456789]

    for seconds in test_cases:
        print(f"{seconds} seconds is formatted as: '{format_duration(seconds)}'")
