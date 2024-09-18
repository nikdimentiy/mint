import math

def century(year):
    """
    Calculate the century for a given year.

    A century is defined as a period of 100 years. The first century 
    includes the years 1 to 100, the second century includes the years 
    101 to 200, and so on. This function takes a year as input and 
    returns the corresponding century.

    Parameters:
    year (int): The year for which to calculate the century.

    Returns:
    int: The century of the given year.
    """
    # Calculate the century by dividing the year by 100 and rounding up
    return math.ceil(year / 100)

# Driver code to test the century function
if __name__ == "__main__":
    # Test cases
    test_years = [1, 100, 101, 200, 201, 300, 999, 1000, 2000, 2023]
    
    for year in test_years:
        print(f"The year {year} is in the {century(year)} century.")
