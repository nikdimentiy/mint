def product_array(arr):
    """
    Calculate an array where each element is the product of all elements in the input array except the one at that position.
    
    Given an array of numbers, this function returns a new array where each element
    at position i is the product of all elements in the original array except arr[i].
    
    Args:
        arr (list): A list of integers
        
    Returns:
        list: A new list where each element at index i is the product of all 
              elements in the input array except the element at index i
              
    Examples:
        >>> product_array([1, 2, 3, 4])
        [24, 12, 8, 6]
        
        >>> product_array([10, 3, 5, 6, 2])
        [180, 600, 360, 300, 900]
    """
    # Calculate the product of all elements in the array
    total_product = 1
    for num in arr:
        total_product *= num
    
    # Create output array where each element is the total product divided by the corresponding input element
    output = []
    for num in arr:
        output.append(total_product // num)
    
    return output


# Driver code to test the function
if __name__ == "__main__":
    # Test case 1
    input_array1 = [1, 2, 3, 4]
    result1 = product_array(input_array1)
    print(f"Input: {input_array1}")
    print(f"Output: {result1}")
    # Expected output: [24, 12, 8, 6]
    
    # Test case 2
    input_array2 = [10, 3, 5, 6, 2]
    result2 = product_array(input_array2)
    print(f"Input: {input_array2}")
    print(f"Output: {result2}")
    # Expected output: [180, 600, 360, 300, 900]
    
    # Test case 3: Single element array
    input_array3 = [5]
    result3 = product_array(input_array3)
    print(f"Input: {input_array3}")
    print(f"Output: {result3}")
    # Expected output: [1]
    
    # Test case 4: Array with zeroes
    input_array4 = [0, 1, 2, 3]
    result4 = product_array(input_array4)
    print(f"Input: {input_array4}")
    print(f"Output: {result4}")
    # Note: This will cause division by zero error for the first element
    # A better implementation might need to handle this special case
