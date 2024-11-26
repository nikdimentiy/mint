def largest(n, xs):
    """
    Find the n highest elements in a list.

    Args:
        n (int): The number of highest elements to find.
        xs (list): A list of elements (can be of any type that supports comparison).

    Returns:
        list: A list containing the n highest elements from the input list.
    
    Example:
        Given the input:
        n = 3
        xs = [1, 5, 3, 9, 2]
        
        The output will be:
        [5, 9]
    """
    # Sort the list in ascending order and return the last n elements
    return sorted(xs)[-n:]

# Driver code to test the largest function
if __name__ == "__main__":
    # Test case 1
    n1 = 3
    xs1 = [1, 5, 3, 9, 2]
    output1 = largest(n1, xs1)
    print("Input List:", xs1)
    print("Largest", n1, "elements:", output1)

    # Test case 2
    n2 = 2
    xs2 = [10, 20, 5, 15, 30, 25]
    output2 = largest(n2, xs2)
    print("Input List:", xs2)
    print("Largest", n2, "elements:", output2)

    # Test case 3
    n3 = 1
    xs3 = [7, 3, 9, 1, 4]
    output3 = largest(n3, xs3)
    print("Input List:", xs3)
    print("Largest", n3, "element:", output3)
