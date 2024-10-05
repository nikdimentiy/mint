def elevator_distance(array):
    """
    Calculate the total distance traveled by an elevator given a list of floors.

    Parameters:
    array (list of int): A list of integers representing the floors the elevator visits.

    Returns:
    int: The total distance traveled by the elevator, calculated as the sum of the 
         absolute differences between consecutive floors.
    """
    dist = 0  # Initialize the distance variable to zero
    # Loop through the array, stopping before the last element
    for i in range(len(array) - 1):
        # Calculate the absolute difference between the current floor and the next floor
        dist += abs(array[i] - array[i + 1])
    return dist  # Return the total distance traveled

# Driver code to test the function
if __name__ == "__main__":
    # Example list of floors the elevator visits
    floors = [1, 3, 5, 2, 8]
    # Calculate the distance traveled by the elevator
    total_distance = elevator_distance(floors)
    # Print the result
    print(f"The total distance traveled by the elevator is: {total_distance}")
