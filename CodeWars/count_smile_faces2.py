from re import findall

def count_smileys(arr):
    """
    Count the number of smiley faces in a list of strings.

    A smiley face is defined as:
    - A colon (:) or semicolon (;) followed optionally by a nose (either '-' or '~')
    - Followed by a closing parenthesis (') or a capital D (D)

    Args:
        arr (list of str): A list of strings to search for smiley faces.

    Returns:
        int: The total count of smiley faces found in the input list.
    """
    # Join the list of strings into a single string with spaces in between
    # and use regex to find all occurrences of smiley patterns
    return len(list(findall(r"[:;][-~]?[)D]", " ".join(arr))))

# Driver code to test the count_smileys function
if __name__ == "__main__":
    # Test cases
    test_cases = [
        [":)", ";(", ";)", ":-D", ":-~)", ":-)"],
        [":", ";", ":-", ":-D", ":-~D", ":-)"],
        ["", ":-)", ":-D", ":-~)", ":-~D"],
        [";D", ":~)", ":)", ";~D", ";-D"],
        [";(", ":-(", ":~D", ":D", ";)"]
    ]

    # Iterate through test cases and print the results
    for i, test in enumerate(test_cases):
        print(f"Test case {i + 1}: {test} => Smiley count: {count_smileys(test)}")
