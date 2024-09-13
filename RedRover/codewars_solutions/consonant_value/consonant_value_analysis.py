import matplotlib.pyplot as plt
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
        return sum(char_value(c) for c in sub)

    # Replace vowels with spaces and split the string into consonant substrings
    consonant_substrings = "".join(c if c not in vowels else " " for c in s).split()

    # Handle the case where there are no consonant substrings
    if not consonant_substrings:
        return 0

    # Return the maximum value among all consonant substrings
    return max(substring_value(sub) for sub in consonant_substrings) if consonant_substrings else 0

def plot_summary(test_cases, results):
    """
    Plot a bar chart of the highest consonant substring values for each test case.

    Args:
    test_cases (list): A list of strings (test cases).
    results (list): A list of integers (corresponding results).
    """
    # Create the bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(test_cases, results, color='skyblue')

    # Add labels and title
    plt.xlabel('Test Cases', fontsize=12)
    plt.ylabel('Highest Consonant Substring Value', fontsize=12)
    plt.title('Highest Consonant Substring Values for Test Cases', fontsize=14)

    # Add value labels on top of the bars
    for i, value in enumerate(results):
        plt.text(i, value + 0.5, str(value), ha='center', fontsize=10)

    # Save the plot to a file
    plt.tight_layout()
    plt.savefig('result_plot.jpg')  # Save the plot as a JPG file
    plt.close()  # Close the plot to free up memory

# Test cases with varying word lengths
test_cases = [
    "strength",   # 8 letters
    "rhythm",     # 6 letters
    "algorithm",  # 9 letters
    "a",          # 1 letter (vowel only)
    "bcdf",       # 4 letters (consonants only)
    "python",     # 6 letters
    "example",    # 7 letters
    "hello",      # 5 letters
    "world",      # 5 letters
    "testcase",   # 8 letters
    "beautiful",  # 9 letters
    "sky",        # 3 letters
    "xyz",        # 3 letters
]

# Calculate results for all test cases
results = [solve(tc) for tc in test_cases]

# Create a PrettyTable to display results
table = PrettyTable()
table.field_names = ["Input", "Highest Consonant Substring Value"]

# Add rows to the table
for test_case, result in zip(test_cases, results):
    table.add_row([test_case, result])

# Print the table
print(table)

# Plot the summary of results
plot_summary(test_cases, results)
