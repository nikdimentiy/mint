def century(year):
    """
    Calculate the century for a given year.

    A century is defined as a period of 100 years. The first century 
    includes the years 1 to 100, the second century includes the years 
    101 to 200, and so on. 

    Parameters:
    year (int): The year for which to calculate the century.

    Returns:
    int: The century of the given year.
    """
    # If the year is less than 1000, calculate the century directly
    if year < 1000:
        return year // 100 + 1
    # If the year is exactly divisible by 100, it is the last year of that century
    elif year >= 1000 and year % 100 == 0:
        return year // 100
    # For all other years, calculate the century by dividing by 100 and rounding up
    else:
        return year // 100 + 1

# Driver code to test the function
if __name__ == "__main__":
    test_years = [1, 100, 101, 200, 300, 999, 1000, 1500, 2000, 2023]
    for year in test_years:
        print(f"The year {year} is in the {century(year)} century.")
