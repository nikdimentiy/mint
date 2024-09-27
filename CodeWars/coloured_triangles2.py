COLORS = set("RGB")

def triangle(row):
    """
    Reduces a string of colors by applying a transformation rule until only one color remains.

    The transformation rule is as follows:
    - If two adjacent colors are the same, they remain the same.
    - If two adjacent colors are different, the resulting color is the one not present in the pair.
    
    Args:
        row (str): A string consisting of characters from the set {'R', 'G', 'B'}.

    Returns:
        str: A single character representing the final color after all transformations.
    """
    # Continue reducing the row until only one color remains
    while len(row) > 1:
        # Create a new row by applying the transformation rule to adjacent colors
        row = ''.join(
            a if a == b else (COLORS - {a, b}).pop() for a, b in zip(row, row[1:])
        )
    return row

# Driver code to test the triangle function
if __name__ == "__main__":
    # Test cases
    test_cases = [
        "RGB",      # Expected output: R
        "RRGG",     # Expected output: G
        "RGBRGB",   # Expected output: R
        "RRR",      # Expected output: R
        "GGG",      # Expected output: G
        "BBB",      # Expected output: B
        "RGRGRG",   # Expected output: R
        "RRGGBB"    # Expected output: G
    ]

    for test in test_cases:
        result = triangle(test)
        print(f"triangle('{test}') = '{result}'")
