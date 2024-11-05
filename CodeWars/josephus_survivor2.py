def josephus_survivor(n, k):
    """
    Solve the Josephus problem and find the position of the last survivor.

    The Josephus problem is a theoretical problem related to a certain counting-out game.
    In this problem, n people stand in a circle and every k-th person is eliminated until only one person remains.

    Parameters:
    n (int): The total number of people in the circle (must be greater than 0).
    k (int): The step count for elimination (must be greater than 0).

    Returns:
    int: The position of the last person remaining (1-indexed).
    """
    # Create a list of people numbered from 1 to n
    lst = [i for i in range(1, n + 1)]
    
    # Initialize the index for elimination
    x = k - 1
    
    # Continue eliminating until only one person remains
    while len(lst) != 1:
        # Calculate the index of the person to be eliminated
        x = x % len(lst)
        # Remove the person from the list
        lst.pop(x)
        # Move to the next person to eliminate
        x += k - 1
    
    # Return the position of the last remaining person
    return lst[0]

# Driver code to test the function
if __name__ == "__main__":
    # Example usage
    n = 7  # Total number of people
    k = 3  # Step count for elimination
    survivor = josephus_survivor(n, k)
    print(f"The position of the last survivor is: {survivor}")
