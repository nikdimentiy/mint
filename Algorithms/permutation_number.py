def generate_numbers(N: int, M: int, prefix=None):
    """
    Generate all possible numbers with N digits, where the first M digits are fixed.

    Args:
      N: The number of digits in the output numbers.
      M: The number of digits that are fixed.
      prefix: The prefix of the output numbers.

    Returns:
      A list of all possible numbers.
    """

    # This is the base case. If M is 0, then there are no more digits to choose from,
    # so we just return the current prefix as a list.

    if M == 0:
        return [prefix]

    # Initialize the prefix to None if it is not explicitly set by the user.

    prefix = prefix or []

    # Create a list to store the generated numbers.

    numbers = []

    # Iterate over all possible digits.

    for digit in range(N):
        # Generate all possible numbers with M-1 digits, where the first digit is fixed to be `digit`.
        new_numbers = generate_numbers(N, M-1, prefix + [digit])

        # Add the new numbers to the list of generated numbers.
        numbers.extend(new_numbers)

    # Return the list of generated numbers.

    return numbers

# Get user input for N and M

N = int(input("Enter the total number of digits (N): "))
M = int(input("Enter the number of fixed digits (M): "))

# Generate all possible numbers and print them

result = generate_numbers(N, M)
print(result)

# Print the total number of permutations

print(f"The total count of permutations is: {len(result)}")
