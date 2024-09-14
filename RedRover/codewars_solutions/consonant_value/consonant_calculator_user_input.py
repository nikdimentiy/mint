from prettytable import PrettyTable

def solve(user_string: str) -> int:
    """
    Calculate the highest value of consonant substrings in a given string.

    Args:
    user_string (str): The input string containing lowercase English letters.

    Returns:
    int: The highest value among all consonant substrings in the input string.
    """
    vowels = set("aeiou")

    def char_value(char: str) -> int:
        """Calculate the value of a character (a=1, b=2, ..., z=26)."""
        return ord(char) - ord("a") + 1

    def substring_value(substring: str) -> int:
        """Calculate the total value of a substring."""
        total_value = 0
        for char in substring:
            total_value += char_value(char)
        return total_value

    # Replace vowels with spaces and split the string into consonant substrings
    consonant_substrings = []
    current_substring = ""

    for character in user_string:
        if character not in vowels:
            current_substring += character
        else:
            if current_substring:
                consonant_substrings.append(current_substring)
                current_substring = ""

    # Add the last substring if it exists
    if current_substring:
        consonant_substrings.append(current_substring)

    # Handle the case where there are no consonant substrings
    if not consonant_substrings:
        return 0

    # Calculate the maximum value among all consonant substrings
    max_value = 0
    for sub in consonant_substrings:
        sub_value = substring_value(sub)
        if sub_value > max_value:
            max_value = sub_value

    return max_value

# Get user input
user_input = input("Please enter a string of lowercase: ")

# Calculate the result for the user input
result = solve(user_input)

# Create a PrettyTable to display the result
table = PrettyTable()
table.field_names = ["Input", "Highest Consonant Substring Value"]

# Add the user input and result to the table
table.add_row([user_input, result])

# Print the table
print(table)
