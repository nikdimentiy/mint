def gen_bin(M, prefix=""):
    """
    Generates binary strings of length M.

    This function recursively generates all possible binary strings of length M,
    where each digit in the binary string can be either '0' or '1'. The generated
    binary strings are printed to the console.

    Args:
        M (int): The length of the binary strings to be generated.
        prefix (str, optional): The prefix to be added to the generated binary strings.
            Used during the recursive calls. Defaults to an empty string.

    Returns:
        None

    Examples:
        >>> gen_bin(2)
        00
        01
        10
        11

    """
    if M == 0:
        # Base case: When M becomes 0, we have generated a complete binary string.
        # Print the current prefix (binary string).
        print(prefix)
        return

    # Recursive case: Generate binary strings by appending '0' and '1' to the prefix.
    # For each digit position, generate two possibilities: '0' and '1'.
    gen_bin(M-1, prefix+"0")  # Recursively generate binary strings with '0' added.
    gen_bin(M-1, prefix+"1")  # Recursively generate binary strings with '1' added.

# Example usage
gen_bin(2)  # Generates and prints all binary strings of length 2.
