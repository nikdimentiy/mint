def friend(x):
    """
    This function takes a list of names and returns a list of names that have exactly four letters.

    Parameters:
    x (list): A list of strings representing names.

    Returns:
    list: A list of strings containing names with exactly four letters.
    """
    # Use a list comprehension to filter names with exactly four letters
    return [n for n in x if len(n) == 4]

# Driver code to test the friend function
if __name__ == "__main__":
    # Sample list of names
    names = ["John", "Paul", "George", "Ringo", "Anna", "Mike", "Sara", "Tom"]
    
    # Call the friend function with the sample list
    four_letter_friends = friend(names)
    
    # Print the result
    print("Names with exactly four letters:", four_letter_friends)
