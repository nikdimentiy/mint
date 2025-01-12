def high_and_low(numbers):
    """
    Given a string of space-separated numbers, this function returns a string 
    containing the highest and lowest number in the format "highest lowest".

    Parameters:
    numbers (str): A string of space-separated integers.

    Returns:
    str: A string representing the highest and lowest numbers.
    """
    # Split the input string into a list of strings and convert them to integers
    num_list = [int(num) for num in numbers.split()]
    
    # Find the highest number in the list
    highest = max(num_list)
    
    # Find the lowest number in the list
    lowest = min(num_list)
    
    # Return the result as a formatted string
    return f"{highest} {lowest}"

# Driver code to test the function
if __name__ == "__main__":
    # Test cases
    test_input = "1 2 3 4 5"
    print(f"Input: '{test_input}' => Output: '{high_and_low(test_input)}'")  # Expected: "5 1"

    test_input = "1 2 -3 4 5"
    print(f"Input: '{test_input}' => Output: '{high_and_low(test_input)}'")  # Expected: "5 -3"

    test_input = "1 9 3 4 -5"
    print(f"Input: '{test_input}' => Output: '{high_and_low(test_input)}'")  # Expected: "9 -5"

    test_input = "10 20 30 40 50"
    print(f"Input: '{test_input}' => Output: '{high_and_low(test_input)}'")  # Expected: "50 10"
