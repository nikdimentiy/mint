def solution(n, h):
    """
    Generate a pattern of stars based on the given parameters.

    The function creates a visual representation of a star pattern consisting of:
    - A top section with a fixed pattern of stars.
    - A middle section that varies based on the input parameters.
    - A bottom section that consists of a fixed pattern of stars.

    Parameters:
    n (int): The number of rows in the middle section.
    h (int): The height of the middle section. If h is even, it is adjusted to be odd.

    Returns:
    list: A list of strings representing the star pattern.
    """
    
    # Fixed top section of the star pattern
    c = ["*", "*", "***"]
    
    # Create the middle section of the star pattern
    # If h is even, increase it by 1 to make it odd
    f = ["*" * (h if h % 2 else h + 1) for _ in range(n)]
    
    # Create the bottom section of the star pattern
    b = ["*****" + "*" * ((2 * j) + (i * 2)) for i in range(n) for j in range(h)]
    
    # Combine all sections and right-align them
    return [i.rjust((len(b[-1]) // 2) + (len(i) - len(i) // 2), " ") for i in c + b + f]

# Driver code to test the solution function
if __name__ == "__main__":
    n = 3  # Number of rows in the middle section
    h = 5  # Height of the middle section
    star_pattern = solution(n, h)
    
    # Print the generated star pattern
    for line in star_pattern:
        print(line)
