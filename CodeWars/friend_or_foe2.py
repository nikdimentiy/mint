def friend(x):
    """
    This function takes a list of names and returns a list of names that have exactly four letters.

    Parameters:
    x (list): A list of strings representing names.

    Returns:
    list: A list containing names from the input list that have exactly four letters.
    """
    # Initialize an empty list to store names with exactly four letters
    names = []
    
    # Iterate through each name in the input list
    for name in x:
        # Check if the length of the name is exactly 4
        if len(name) == 4:
            # If true, append the name to the names list
            names.append(name)
    
    # Return the list of names with exactly four letters
    return names

# Driver code to test the function
if __name__ == "__main__":
    # Sample list of names
    name_list = ["John", "Paul", "Ringo", "George", "Anna", "Mike", "Sara"]
    
    # Call the friend function with the sample list
    four_letter_names = friend(name_list)
    
    # Print the result
    print("Names with exactly four letters:", four_letter_names)
