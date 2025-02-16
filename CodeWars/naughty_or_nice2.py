def naughty_or_nice(data):
    """
    Determine if a person has been more naughty or nice throughout the year.
    
    This function analyzes a full year of behavior data in JSON format and 
    returns whether someone was predominantly "Naughty!" or "Nice!" based on
    the total count of occurrences. If there are equal numbers of naughty and
    nice days, "Nice!" is returned (Santa is generous).
    
    Args:
        data (dict): A nested dictionary containing behavioral data for the year.
                     The outer keys are month names, and the inner keys are days
                     of the month as strings. Values are either "Naughty" or "Nice".
                     
    Returns:
        str: "Nice!" if the number of nice days is greater than or equal to
             the number of naughty days, otherwise "Naughty!".
    
    Example:
        >>> year_data = {
        ...    "January": {"1": "Nice", "2": "Naughty", "3": "Nice"},
        ...    "February": {"1": "Naughty", "2": "Naughty"}
        ... }
        >>> naughty_or_nice(year_data)
        'Nice!'
    """
    nice = 0  # Counter to track the balance of nice vs naughty
    
    # Iterate through each month in the data
    for month in data:
        # Iterate through each day in the current month
        for day in data[month]:
            # Increment counter for "Nice", decrement for "Naughty"
            nice += 1 if data[month][day] == "Nice" else -1
    
    # If nice counter is non-negative, return "Nice!", otherwise "Naughty!"
    return "Nice!" if nice >= 0 else "Naughty!"


# Driver code
if __name__ == "__main__":
    # Test case 1: More nice than naughty
    test_data1 = {
        "January": {"1": "Nice", "2": "Nice", "3": "Naughty"},
        "February": {"1": "Nice", "2": "Nice"}
    }
    
    # Test case 2: More naughty than nice
    test_data2 = {
        "January": {"1": "Naughty", "2": "Naughty", "3": "Nice"},
        "February": {"1": "Naughty", "2": "Nice"}
    }
    
    # Test case 3: Equal nice and naughty
    test_data3 = {
        "January": {"1": "Nice", "2": "Naughty"},
        "February": {"1": "Nice", "2": "Naughty"}
    }
    
    # Run the tests and print results
    print("Test case 1 (more nice):", naughty_or_nice(test_data1))
    print("Test case 2 (more naughty):", naughty_or_nice(test_data2))
    print("Test case 3 (equal):", naughty_or_nice(test_data3))
    
    # Expected output:
    # Test case 1 (more nice): Nice!
    # Test case 2 (more naughty): Naughty!
    # Test case 3 (equal): Nice!
