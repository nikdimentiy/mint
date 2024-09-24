def isleflood(h: list[int]) -> int:
    """
    Calculate the total amount of water trapped after raining.

    Parameters:
    h (list[int]): A list of integers representing the heights of the bars.

    Returns:
    int: The total amount of water trapped.
    """
    # Find the position of the maximum height in the list
    maxpos = 0
    for i in range(len(h)):
        if h[i] > h[maxpos]:
            maxpos = i

    # Initialize the total water trapped variable
    ans = 0
    # Initialize the current maximum height for the left side
    nowm = 0

    # Calculate water trapped on the left side of the maximum position
    for i in range(maxpos):
        if h[i] > nowm:
            nowm = h[i]  # Update current max height if current height is greater
        ans += nowm - h[i]  # Calculate trapped water for the current position

    # Reset current maximum height for right side calculation
    nowm = 0

    # Calculate water trapped on the right side of the maximum position
    for i in range(len(h) - 1, maxpos, -1):
        if h[i] > nowm:
            nowm = h[i]  # Update current max height for the right
        ans += nowm - h[i]  # Calculate trapped water for the current position

    return ans  # Return the total trapped water


# Driver code to test the isleflood function
if __name__ == "__main__":
    # Example test cases
    heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]  # Example heights
    trapped_water = isleflood(heights)
    print(f"Trapped water for heights {heights}: {trapped_water}")
    # Expected output: 6
