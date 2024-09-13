from prettytable import PrettyTable

def solve(s: str) -> int:
    """
    Calculate the highest value of consonant substrings in a given string.

    Args:
    s (str): The input string containing lowercase English letters.

    Returns:
    int: The highest value among all consonant substrings in the input string.
    """
    vowels = set("aeiou")

    def char_value(c):
        """Calculate the value of a character (a=1, b=2, ..., z=26)."""
        return ord(c) - ord("a") + 1

    def substring_value(sub):
        """Calculate the total value of a substring."""
        total_value = 0
        for c in sub:
            total_value += char_value(c)
        return total_value

    # Replace vowels with spaces and split the string into consonant substrings
    consonant_substrings = []
    current_substring = ""

    for c in s:
        if c not in vowels:
            current_substring += c
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

# Test cases with additional strings
test_cases = [
    "zodiacs",        # 7 letters
    "strength",       # 8 letters
    "cozy",           # 4 letters
    "xyzzy",          # 5 letters
    "zodiac",         # 6 letters
    "chruschtschov",  # 12 letters
    "khrushchev",     # 10 letters
    "twelfthstreet",  # 12 letters
    "mischtschenkoana" # 15 letters
]

# Calculate results for all test cases
results = []
for tc in test_cases:
    results.append(solve(tc))

# Create a PrettyTable to display results
table = PrettyTable()
table.field_names = ["Input", "Highest Consonant Substring Value"]

# Add rows to the table
for test_case, result in zip(test_cases, results):
    table.add_row([test_case, result])

# Print the table
print(table)
