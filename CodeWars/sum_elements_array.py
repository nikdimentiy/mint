def parts_sums(ls):
    """
    Calculates the sum of parts (suffix sums) of a given list.
    
    This function takes a list of integers and returns a new list where 
    each element at index `i` is the sum of all elements in the input list 
    from index `i` to the end. The final element of the returned list 
    is always 0, representing the sum of an empty slice.
    
    Args:
        ls (list of int): The input list of numbers.
        
    Returns:
        list of int: A list containing the cumulative suffix sums.
    """
    # Initialize the result array with zeros.
    # The length is len(ls) + 1 to account for the final empty slice sum (0).
    sums = [0] * (len(ls) + 1)
    
    # Iterate through the input list in reverse order.
    # enumerate() gives us a counter `i` (0, 1, 2...) starting from the rightmost element `e`.
    for i, e in enumerate(reversed(ls)):
        
        # Calculate the target index in the `sums` array (working right to left).
        # We add the previously calculated sum (to its right) and the current element `e`.
        current_index = len(ls) - i - 1
        previous_index = len(ls) - i
        
        sums[current_index] += sums[previous_index] + e
        
    return sums


# ==========================================
#               DRIVER CODE
# ==========================================
if __name__ == "__main__":
    
    # Test Case 1: Standard list of numbers
    input_1 = [0, 1, 3, 6, 10]
    print("Test Case 1: Standard List")
    print(f"Input:  {input_1}")
    print(f"Output: {parts_sums(input_1)}")
    # Expected: [20, 20, 19, 16, 10, 0]
    print("-" * 40)

    # Test Case 2: An empty list
    input_2 = []
    print("Test Case 2: Empty List")
    print(f"Input:  {input_2}")
    print(f"Output: {parts_sums(input_2)}")
    # Expected: [0]
    print("-" * 40)
    
    # Test Case 3: A list with identical elements
    input_3 = [5, 5, 5]
    print("Test Case 3: Identical Elements")
    print(f"Input:  {input_3}")
    print(f"Output: {parts_sums(input_3)}")
    # Expected: [15, 10, 5, 0]
    print("-" * 40)
