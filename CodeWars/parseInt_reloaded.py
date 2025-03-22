def parse_int(string):
    """
    Convert a string representing a number in words into an integer.

    Args:
    string (str): A string containing the number in words (e.g., "one", "twenty", "two hundred forty-six").

    Returns:
    int: The integer representation of the input string.
    
    Examples:
    >>> parse_int("one")
    1
    >>> parse_int("twenty")
    20
    >>> parse_int("two hundred forty-six")
    246
    >>> parse_int("seven hundred eighty-three thousand nine hundred and nineteen")
    783919
    """
    
    # Dictionary mapping words to their corresponding integer values
    num_dict = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
        'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13,
        'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17,
        'eighteen': 18, 'nineteen': 19, 'twenty': 20, 'thirty': 30,
        'forty': 40, 'fifty': 50, 'sixty': 60, 'seventy': 70,
        'eighty': 80, 'ninety': 90
    }

    # Replace hyphens with spaces and split the string into words
    words = string.replace('-', ' ').split()
    total = 0  # To accumulate the total value
    current = 0  # To accumulate the current value being processed

    for word in words:
        if word == 'and':
            continue  # Skip the word 'and'
        elif word == 'hundred':
            current *= 100  # Multiply current by 100
        elif word == 'thousand':
            total += current * 1000  # Add current value multiplied by 1000 to total
            current = 0  # Reset current
        elif word == 'million':
            total += current * 1000000  # Add current value multiplied by 1,000,000 to total
            current = 0  # Reset current
        else:
            current += num_dict[word]  # Add the value of the word to current

    total += current  # Add any remaining current value to total
    return total  # Return the final total


# Driver code to test the function
if __name__ == "__main__":
    test_cases = [
        "one",
        "twenty",
        "two hundred forty-six",
        "seven hundred eighty-three thousand nine hundred and nineteen",
        "four hundred and fifty-six",
        "nineteen million eight hundred and seventy-five thousand three hundred and twenty-one"
    ]

    for test in test_cases:
        result = parse_int(test)
        print(f'parse_int("{test}") = {result}')
