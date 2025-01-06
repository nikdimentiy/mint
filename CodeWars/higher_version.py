def solution(ver1, ver2):
    """
    Compares two version numbers given as strings and determines if the first version is greater than the second.

    Parameters:
    ver1 (str): The first version number in the format "x.y.z".
    ver2 (str): The second version number in the format "x.y.z".

    Returns:
    bool: True if `ver1` is greater than `ver2`, False otherwise.
    """
    # Split the version strings into lists of integers
    ver1_fields = list(map(int, ver1.split('.')))
    ver2_fields = list(map(int, ver2.split('.')))

    # Compare each corresponding component of the version numbers
    for i in range(len(ver1_fields)):
        if ver1_fields[i] > ver2_fields[i]:
            return True  # ver1 is greater than ver2
        elif ver1_fields[i] < ver2_fields[i]:
            return False  # ver1 is less than ver2

    # If we reach this point, both versions are equal
    return False

# Driver code to test the function
print(solution("1.2.3", "1.2.2"))  # Output: True (1.2.3 is greater than 1.2.2)
print(solution("1.0.0", "1.0.0"))  # Output: False (1.0.0 is equal to 1.0.0)
print(solution("2.0.1", "2.1.0"))  # Output: False (2.0.1 is less than 2.1.0)
