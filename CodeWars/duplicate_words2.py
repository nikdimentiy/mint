from itertools import groupby

def remove_consecutive_duplicates(s):
    """
    Remove consecutive duplicate words from a string, leaving only the first occurrence of each word.

    Parameters:
    s (str): The input string containing words.

    Returns:
    str: A string with consecutive duplicate words removed.
    """
    # Split the input string into words and use groupby to group consecutive duplicates
    return ' '.join(k for k, _ in groupby(s.split()))

# Driver code to test the function
if __name__ == "__main__":
    # Test input string with consecutive duplicate words
    test_string = "alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta"
    
    # Call the function and print the result
    result = remove_consecutive_duplicates(test_string)
    print("Original string:")
    print(test_string)
    print("\nString after removing consecutive duplicates:")
    print(result)
