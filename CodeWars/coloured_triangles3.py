def triangle(row):
    """
    This function takes a string of colors represented by the letters 'R', 'G', and 'B'.
    It reduces the string according to specific rules defined in the `dicts` dictionary,
    where pairs of colors are combined into a single color. The process is repeated until
    only one color remains.

    Parameters:
    row (str): A string representing the initial row of colors.

    Returns:
    str: A single character representing the final color after all combinations.
    """
    # Dictionary defining the color combination rules
    dicts = {
        'GG': 'G', 'BB': 'B', 'RR': 'R', 
        'BR': 'G', 'BG': 'R', 'GB': 'R', 
        'GR': 'B', 'RG': 'B', 'RB': 'G'
    }
    
    # If the row has more than 2 colors, continue reducing it
    if len(row) > 2:
        s = ''
        for i in range(len(row) - 1):
            # Combine colors based on the rules in the dictionary
            s += dicts[row[i:i + 2]]
        row = s
        return triangle(row)  # Recursively call triangle with the new row
    elif len(row) > 1:
        # If the row has exactly 2 colors, return the combined color
        return dicts[row]
    else:
        # If only one color remains, return it
        return row

# Driver code to test the triangle function
if __name__ == "__main__":
    # Test cases
    test_cases = [
        "RGB",    # Expected output: 'G'
        "RRGGBB", # Expected output: 'R'
        "GGG",    # Expected output: 'G'
        "BRG",    # Expected output: 'B'
        "RRRR",   # Expected output: 'R'
        "BGBG",   # Expected output: 'G'
    ]

    for test in test_cases:
        result = triangle(test)
        print(f"triangle('{test}') = '{result}'")
