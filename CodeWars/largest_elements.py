def largest(n, xs):
    """
    Returns the top n largest elements from the given list xs.

    Parameters:
    n (int): The number of largest elements to return.
    xs (list): A list of numbers from which to find the largest elements.

    Returns:
    list: A sorted list of the top n largest elements from xs.
    """
    # Sort the list in descending order and take the first n elements
    top_n = sorted(xs, reverse=True)[:n]
    # Return the top n elements sorted in ascending order
    return sorted(top_n)

# Driver code to test the largest function
if __name__ == "__main__":
    # Test case 1
    result = largest(2, [7, 6, 5, 4, 3, 2, 1])
    print(result)  # Expected output: [6, 7]

    # Test case 2
    result = largest(3, [10, 20, 30, 40, 50])
    print(result)  # Expected output: [30, 40, 50]

    # Test case 3
    result = largest(1, [5, 1, 3, 2, 4])
    print(result)  # Expected output: [5]

    # Test case 4
    result = largest(4, [1, 2, 3])
    print(result)  # Expected output: [2, 3]

    # Test case 5
    result = largest(0, [1, 2, 3])
    print(result)  # Expected output: []

