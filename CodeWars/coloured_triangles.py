def triangle(row):
    """
    Generate a colored triangle from a row of colors.

    The function takes a string of colors (each being 'R', 'G', or 'B') and generates successive rows
    of colors based on the following rules:
    - If two adjacent colors are the same, the new row will have that same color.
    - If two adjacent colors are different, the new row will have the color that is not present
      among the two adjacent colors.

    The process continues until only one color remains.

    Parameters:
    row (str): A string representing the initial row of colors.

    Returns:
    str: A single character representing the final color in the triangle.
    """
    if len(row) == 1:
        return row
    else:
        temp = ""
        for i in range(len(row) - 1):
            # Check if the two adjacent colors are the same
            if row[i] == row[i + 1]:
                temp += row[i]  # Keep the same color
            # Determine the missing color when the two are different
            elif row[i] in "BG" and row[i + 1] in "BG":
                temp += "R"  # Missing color is Red
            elif row[i] in "RG" and row[i + 1] in "RG":
                temp += "B"  # Missing color is Blue
            elif row[i] in "BR" and row[i + 1] in "BR":
                temp += "G"  # Missing color is Green
        return triangle(temp)  # Recursively call triangle with the new row


# Driver code to test the triangle function
if __name__ == "__main__":
    # Example input
    initial_row = "RGBRGB"
    final_color = triangle(initial_row)
    print(f"The final color from the initial row '{initial_row}' is: {final_color}")

    # Additional test cases
    test_cases = [
        "RRGG",  # Should return 'B'
        "RGB",   # Should return 'R'
        "GGG",   # Should return 'G'
        "BRG",   # Should return 'R'
        "R",     # Should return 'R'
    ]

    for test in test_cases:
        result = triangle(test)
        print(f"The final color from the initial row '{test}' is: {result}")
