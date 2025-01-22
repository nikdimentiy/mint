def solution(statues):
    """
    Calculate the minimum number of additional statues needed to arrange
    the given statues in a sequence where each statue is exactly 1 unit
    larger than the previous one.

    Parameters:
    statues (list of int): A list of non-negative integers representing the sizes of the statues.

    Returns:
    int: The minimum number of additional statues required.
    """
    # Sort the array of statue sizes in ascending order
    statues.sort()
    
    # Initialize a counter for additional statues needed
    count = 0
    
    # Set the previous statue size to the first statue in the sorted list
    prev_statue = statues[0]
    
    # Iterate through the sorted list starting from the second statue
    for i in range(1, len(statues)):
        curr_statue = statues[i]  # Current statue size
        diff = curr_statue - prev_statue  # Difference between current and previous statue sizes
        
        # If the difference is greater than 1, we need additional statues
        if diff > 1:
            count += diff - 1  # Add the number of additional statues needed
        
        # Update the previous statue size to the current one for the next iteration
        prev_statue = curr_statue
    
    return count  # Return the total count of additional statues needed

# Driver code to test the solution function
if __name__ == "__main__":
    # Example test cases
    test_cases = [
        [6, 2, 3, 8],  # Expected output: 3 (need statues of sizes 4, 5, 7)
        [0, 3],        # Expected output: 2 (need statues of sizes 1, 2)
        [5, 4, 6],     # Expected output: 0 (already consecutive)
        [1, 2, 3],     # Expected output: 0 (already consecutive)
        [1],           # Expected output: 0 (only one statue)
        [],            # Expected output: 0 (no statues)
    ]

    for statues in test_cases:
        print(f"Statues: {statues} => Additional statues needed: {solution(statues)}")
