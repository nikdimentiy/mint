def check(a, limit):
    """
    Check if all values in the array are less than or equal to the specified limit.

    Parameters:
    a (list): A list of numerical values.
    limit (number): The limit value to compare against.

    Returns:
    bool: True if all values in the array are less than or equal to the limit, False otherwise.
    """
    # Use the all() function to check if all elements in the array are less than or equal to the limit
    return all(value <= limit for value in a)

# Driver code to test the function
if __name__ == "__main__":
    # Test cases
    test_array1 = [1, 2, 3, 4, 5]
    limit1 = 5
    print(check(test_array1, limit1))  # Expected output: True

    test_array2 = [1, 2, 3, 6, 5]
    limit2 = 5
    print(check(test_array2, limit2))  # Expected output: False

    test_array3 = [0, -1, -2, 4]
    limit3 = 4
    print(check(test_array3, limit3))  # Expected output: True

    test_array4 = [10, 20, 30]
    limit4 = 25
    print(check(test_array4, limit4))  # Expected output: False
