def get_mean(arr: list, x: int, y: int) -> float:
    """
    Calculate the mean of means for the first x and last y elements in an array.

    This function computes the mean of the first x elements and the mean of the last y elements,
    then returns the average of these two means.

    Args:
    arr (list): The input array of numbers.
    x (int): The number of elements to consider from the beginning of the array.
    y (int): The number of elements to consider from the end of the array.

    Returns:
    float: The mean of means if x and y are valid, -1 otherwise.

    Note:
    - x and y must be greater than 1 and not exceed the length of the array.
    - If the conditions are not met, the function returns -1.
    """
    # Check if x and y are within the valid range
    if x <= 1 or y <= 1 or x > len(arr) or y > len(arr):
        return -1

    # Calculate the mean of the first x elements
    mean_first_x = sum(arr[:x]) / x

    # Calculate the mean of the last y elements
    mean_last_y = sum(arr[-y:]) / y

    # Calculate the mean of the two means
    mean_of_means = (mean_first_x + mean_last_y) / 2

    return mean_of_means


# Driver code
if __name__ == "__main__":
    # Test case 1: Normal case
    arr1 = [1, 3, 2, 4]
    result1 = get_mean(arr1, 2, 3)
    print(f"Test case 1: arr = {arr1}, x = 2, y = 3")
    print(f"Result: {result1}")  # Expected output: 2.5

    # Test case 2: Invalid x (x <= 1)
    arr2 = [1, 3, 2, 4]
    result2 = get_mean(arr2, 1, 2)
    print(f"\nTest case 2: arr = {arr2}, x = 1, y = 2")
    print(f"Result: {result2}")  # Expected output: -1

    # Test case 3: Invalid y (y > len(arr))
    arr3 = [1, 3, 2, 4]
    result3 = get_mean(arr3, 2, 8)
    print(f"\nTest case 3: arr = {arr3}, x = 2, y = 8")
    print(f"Result: {result3}")  # Expected output: -1

    # Test case 4: Larger array
    arr4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result4 = get_mean(arr4, 3, 4)
    print(f"\nTest case 4: arr = {arr4}, x = 3, y = 4")
    print(f"Result: {result4}")  # Expected output: 6.0
