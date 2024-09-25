from typing import List, Tuple

def openOrSenior(data: List[Tuple[int, int]]) -> List[str]:
    """
    Determine the category of participants based on their age and handicap.

    Parameters:
    data (List[Tuple[int, int]]): A list of tuples where each tuple contains two integers:
                                    - The first integer represents the age of the participant.
                                    - The second integer represents the handicap of the participant.

    Returns:
    List[str]: A list of strings where each string is either "Senior" or "Open".
                "Senior" indicates that the participant is 55 years or older and has a handicap greater than 7.
                "Open" indicates that the participant does not meet the criteria for "Senior".
    """
    res = []  # Initialize an empty list to store the results
    for i in data:  # Iterate through each participant's data
        # Check if the participant meets the criteria for "Senior"
        if i[0] >= 55 and i[1] > 7:
            res.append("Senior")  # Append "Senior" if criteria are met
        else:
            res.append("Open")  # Append "Open" if criteria are not met
    return res  # Return the list of results

# Driver code to test the function
if __name__ == "__main__":
    # Sample data: List of tuples (age, handicap)
    participants = [
        (45, 5),   # Open
        (55, 8),   # Senior
        (60, 6),   # Open
        (70, 10),  # Senior
        (30, 7),   # Open
        (50, 9)    # Open
    ]
    
    # Call the function with the sample data
    results = openOrSenior(participants)
    
    # Print the results
    print(results)  # Output: ['Open', 'Senior', 'Open', 'Senior', 'Open', 'Open']
