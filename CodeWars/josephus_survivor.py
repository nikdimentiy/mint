def josephus_survivor(n, k):
    """
    Calculate the position of the last survivor in the Josephus problem.

    The Josephus problem is a theoretical problem related to a certain counting-out game.
    In this game, n people stand in a circle and every k-th person is eliminated until only one person remains.

    Parameters:
    n (int): The total number of people in the circle.
    k (int): The step count for elimination (every k-th person is eliminated).

    Returns:
    int: The position of the last remaining person (1-indexed).
    """
    v = 0  # Initialize the position of the survivor
    for i in range(1, n + 1):
        v = (v + k) % i  # Update the position based on the current number of people
    return v + 1  # Convert from 0-indexed to 1-indexed

# Driver code to test the function
if __name__ == "__main__":
    # Test cases
    print(josephus_survivor(7, 3))  # Expected output: 4
    print(josephus_survivor(10, 2))  # Expected output: 5
    print(josephus_survivor(1, 1))   # Expected output: 1
    print(josephus_survivor(5, 5))   # Expected output: 1
    print(josephus_survivor(6, 3))   # Expected output: 1
