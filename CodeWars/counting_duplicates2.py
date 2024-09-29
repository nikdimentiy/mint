def duplicate_count(s):
    """
    Count the number of distinct case-insensitive characters 
    that occur more than once in the given string.

    Args:
    s (str): The input string to check for duplicate characters.

    Returns:
    int: The number of distinct characters that appear more than once.
    """
    # Convert the string to lowercase and create a set of unique characters
    # Then, count how many of those characters appear more than once in the original string
    return len([c for c in set(s.lower()) if s.lower().count(c) > 1])

# Driver code to test the function
if __name__ == "__main__":
    # Test cases
    print(duplicate_count("abcde"))          # Expected: 0 (no duplicates)
    print(duplicate_count("aabbcde"))        # Expected: 2 (a and b are duplicates)
    print(duplicate_count("aabBcde"))        # Expected: 2 (a and b are duplicates, case insensitive)
    print(duplicate_count("indivisibility"))  # Expected: 1 (i is a duplicate)
    print(duplicate_count("Indivisibilities")) # Expected: 2 (i and s are duplicates)
    print(duplicate_count(""))                # Expected: 0 (empty string)
