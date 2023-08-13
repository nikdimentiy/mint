def generate_number(N: int, M: int, prefix=None):
    """
    Generate all possible numbers in N (number system) where N <= 10.

    Args:
        N: The number system.
        M: The length of the number.
        prefix: A list of digits that have already been generated.

    Returns:
        None.
    """

    # Check if the number is complete.

    if M == 0:
        print(prefix)
        return

    # Iterate over all possible digits.

    for digit in range(N):
        # Add the digit to the prefix.
        prefix.append(digit)

        # Recurse to generate the next number.
        generate_number(N, M - 1, prefix)

        # Remove the digit from the prefix.
        prefix.pop()


def gen_bin(M, prefix=''):
    """Generate all possible binary numbers of length M."""

    # This is a helper function for generate_number.

    if M == 0:
        print(prefix)
        return

    for digit in ['0', '1']:
        gen_bin(M - 1, prefix + digit)


# Example usage

print('Generate all binary numbers of length 8:')
generate_number(2, 8)

print('Generate all binary numbers of length 12:')
gen_bin(12)


