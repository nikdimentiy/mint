def normalize(line: str) -> str:
    """Remove duplicate and space characters from a string.

    Parameters
    ----------
    line : str
        The input string.

    Returns
    -------
    str
        The normalized string.

    Examples
    --------
    >>> normalize("RRReeedddRRRooovvveeerrr...sssccchhhoooooolll")
    'RedRover...school'
    """


# The string to be processed
line: str = "RRReeedddRRRooovvveeerrr...sssccchhhoooooolll"

normal: str = ""  # The processed string, without repeating characters and with "oo" instead of the second to last character

for i in range(len(line)):  # Iterate over each character in the line string
    # If the current character is different from the previous one or it is the first character
    if i == 0 or line[i] != line[i - 1]:
        # Add it to the normal string
        normal += line[i]

# Replace the second to last character in the normal string with "oo"
normal = normal.replace((normal[-2]), "oo")

# Remove any spaces from the normal string
normal = normal.replace(" ", "")

print(normal)  # Print the processed string
