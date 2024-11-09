def naughty_or_nice(data):
    """
    Determine if the overall behavior for the year is "Naughty!" or "Nice!" based on the provided JSON data.

    Args:
    data (dict): A dictionary representing the behavior of individuals throughout the year.
                 The structure is as follows:
                 {
                     "January": { "1": "Naughty", "2": "Nice", ..., "31": "Nice" },
                     "February": { "1": "Nice", "2": "Naughty", ..., "28": "Nice" },
                     ...
                     "December": { "1": "Nice", "2": "Nice", ..., "31": "Naughty" }
                 }

    Returns:
    str: "Naughty!" if there are more "Naughty" occurrences than "Nice", 
         "Nice!" if there are more "Nice" occurrences or if they are equal.
    """
    # Initialize a counter for Naughty and Nice occurrences
    counter = {"Naughty": 0, "Nice": 0}
    
    # Iterate through each month in the data
    for month in data:
        # Iterate through each day in the month
        for day in data[month]:
            # Increment the appropriate counter based on the behavior
            if data[month][day] == "Naughty":
                counter["Naughty"] += 1
            else:
                counter["Nice"] += 1
    
    # Return "Naughty!" if there are more Naughty occurrences, otherwise return "Nice!"
    return "Naughty!" if counter["Naughty"] > counter["Nice"] else "Nice!"

# Driver code to test the function
if __name__ == "__main__":
    # Example JSON data for a year
    year_data = {
        "January": {'1': 'Naughty', '2': 'Naughty', '3': 'Nice', '4': 'Nice', '5': 'Naughty'},
        "February": {'1': 'Nice', '2': 'Naughty', '3': 'Naughty', '4': 'Nice', '5': 'Nice', '6': 'Nice', '7': 'Naughty'},
        "March": {'1': 'Nice', '2': 'Nice', '3': 'Naughty', '4': 'Naughty', '5': 'Naughty', '6': 'Nice', '7': 'Nice'},
        "April": {'1': 'Naughty', '2': 'Naughty', '3': 'Naughty', '4': 'Nice', '5': 'Nice'},
        "May": {'1': 'Nice', '2': 'Nice', '3': 'Naughty', '4': 'Naughty', '5': 'Naughty'},
        "June": {'1': 'Nice', '2': 'Nice', '3': 'Nice', '4': 'Naughty', '5': 'Naughty'},
        "July": {'1': 'Naughty', '2': 'Naughty', '3': 'Nice', '4': 'Nice', '5': 'Naughty'},
        "August": {'1': 'Nice', '2': 'Nice', '3': 'Naughty', '4': 'Naughty', '5': 'Naughty'},
        "September": {'1': 'Nice', '2': 'Nice', '3': 'Nice', '4': 'Naughty', '5': 'Naughty'},
        "October": {'1': 'Naughty', '2': 'Naughty', '3': 'Nice', '4': 'Nice', '5': 'Naughty'},
        "November": {'1': 'Nice', '2': 'Nice', '3': 'Naughty', '4': 'Naughty', '5': 'Naughty'},
        "December": {'1': 'Nice', '2': 'Nice', '3': 'Naughty', '4': 'Naughty', '5': 'Naughty'}
    }

    # Call the function and print the result
    result = naughty_or_nice(year_data)
    print(result)  # Output will depend on the data provided
