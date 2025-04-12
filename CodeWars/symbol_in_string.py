def count(string):
    """
    Counts the occurrences of each character in the given string.

    Args:
        string (str): The input string to count characters from.

    Returns:
        dict: A dictionary where the keys are characters and the values are their respective counts in the string.
    """
    # Create a dictionary comprehension to count each character in the string
    return {c: string.count(c) for c in string}

# Driver code to test the count function
if __name__ == "__main__":
    test_string = "hello world"
    result = count(test_string)
    print("Character count for '{}':".format(test_string))
    for char, count in result.items():
        print("Character '{}': {}".format(char, count))
