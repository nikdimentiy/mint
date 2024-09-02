def openOrSenior(data):
    """
    Determines the category of each person based on their age and handicap.

    Parameters:
    data (list of tuples): A list where each tuple contains two elements:
                           - age (int): The age of the person.
                           - handicap (int): The handicap of the person.

    Returns:
    list: A list of strings where each string is either "Senior" or "Open".
          "Senior" if the person is 55 years or older and has a handicap greater than 7,
          otherwise "Open".
    """
    # List comprehension to iterate through each person in the data
    return ["Senior" if person[0] >= 55 and person[1] > 7 else "Open" for person in data]

# Driver code to test the function
if __name__ == "__main__":
    # Sample data: list of (age, handicap) tuples
    data = [
        (60, 8),   # Senior
        (45, 5),   # Open
        (55, 10),  # Senior
        (30, 6),   # Open
        (70, 7),   # Open
        (50, 9)    # Open
    ]

    # Call the function and print the results
    result = openOrSenior(data)
    print(result)  # Expected output: ['Senior', 'Open', 'Senior', 'Open', 'Open', 'Open']
