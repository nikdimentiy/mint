def traj_num_with_append(N):
    """Returns the number of trajectories of length N that start at the origin and move only up or right.

    Args:
        N (int): A positive integer representing the length of the trajectory.

    Returns:
        int: The number of trajectories of length N.
    """
    # Initialize a list K to store the number of trajectories for each length.
    K = []
    
    # Initialize the first two values in the list as base cases:
    # K[0] = 0 (no trajectories of length 0), and K[1] = 1 (only one trajectory of length 1).
    K.append(0)
    K.append(1)

    # Calculate the number of trajectories for lengths from 2 to N.
    for i in range(2, N + 1):
        # The number of trajectories of length i is the sum of trajectories of length i-2 and i-1.
        K.append(K[i - 2] + K[i - 1])

    # Return the number of trajectories of length N.
    return K[N]

# Driver code to test the function
if __name__ == "__main__":
    # Test cases
    N = 0
    result = traj_num_with_append(N)
    print(f"Number of trajectories of length {N}: {result}")

    N = 5
    result = traj_num_with_append(N)
    print(f"Number of trajectories of length {N}: {result}")

    N = 10
    result = traj_num_with_append(N)
    print(f"Number of trajectories of length {N}: {result}")
