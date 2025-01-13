def solution(inputArray):
    """
    Calculate the sum of house numbers encountered by a boy until he sees a house with number 0.

    Parameters:
    inputArray (list of int): A list of house numbers that the boy encounters during his walk.

    Returns:
    int: The sum of the house numbers encountered before seeing a house with number 0.
    """
    total = 0
    for num in inputArray:
        if num == 0:
            # Stop adding numbers once a house with number 0 is encountered
            break
        total += num
    return total

# Driver code to test the function
if __name__ == "__main__":
    # Test cases
    test_cases = [
        ([1, 2, 3, 0, 4, 5], 6),  # Sum of 1 + 2 + 3 = 6
        ([0, 1, 2, 3], 0),        # Sum is 0 because the first house is 0
        ([5, 6, 0, 7, 8], 11),    # Sum of 5 + 6 = 11
        ([10, 20, 30, 0, 40], 60),# Sum of 10 + 20 + 30 = 60
        ([0], 0),                 # Sum is 0 because the only house is 0
    ]

    for i, (inputArray, expected) in enumerate(test_cases):
        result = solution(inputArray)
        assert result == expected, f"Test case {i+1} failed: expected {expected}, got {result}"
        print(f"Test case {i+1} passed.")

    print("All test cases passed!")
