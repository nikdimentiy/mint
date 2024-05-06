def count_positives_sum_negatives(arr):
    """
    Given a list of integers, this function returns a list where the first element is the count of 
    positive numbers and the second element is the sum of all negative numbers.

    Parameters:
    - arr: list of integers
      The input list of integers which can contain both positive and negative numbers.

    Returns:
    - list of two elements
      A list where the first element is the count of positive numbers, and the second element 
      is the sum of negative numbers. If the input list is empty, an empty list is returned.
    """
    if not arr:  # Check if the list is empty
        return []  # Return an empty list if no data is available

    # Count the number of positive integers in the list
    pos_count = sum(1 for x in arr if x > 0)
    
    # Calculate the sum of all negative integers in the list
    neg_sum = sum(x for x in arr if x < 0)
    
    # Return a list with the count of positive numbers and the sum of negative numbers
    return [pos_count, neg_sum]


# Driver code to test the function with various examples
if __name__ == "__main__":
    # Test case 1: Mixed positive and negative numbers
    test_case_1 = [1, -2, 3, -4, 5, -6]
    print("Output for test case 1:", count_positives_sum_negatives(test_case_1))

    # Test case 2: All positive numbers
    test_case_2 = [10, 20, 30, 40, 50]
    print("Output for test case 2:", count_positives_sum_negatives(test_case_2))

    # Test case 3: All negative numbers
    test_case_3 = [-10, -20, -30, -40, -50]
    print("Output for test case 3:", count_positives_sum_negatives(test_case_3))

    # Test case 4: Empty list
    test_case_4 = []
    print("Output for test case 4:", count_positives_sum_negatives(test_case_4))

    # Test case 5: Mix of zeros and positive numbers
    test_case_5 = [0, 1, 0, 2, 0, 3]
    print("Output for test case 5:", count_positives_sum_negatives(test_case_5))
