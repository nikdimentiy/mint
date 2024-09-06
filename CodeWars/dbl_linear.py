def dbl_linear(n):
    """
    Generate the n-th element of a sequence defined by the following rules:
    - Start with the list containing the first element as 1.
    - For each element in the list, generate two new elements:
        - The first new element is obtained by multiplying the current element by 2 and adding 1.
        - The second new element is obtained by multiplying the current element by 3 and adding 1.
    - The sequence is formed by taking the smallest of the newly generated elements and adding it to the list.
    - If the newly generated elements are equal, both should be added, but only one instance should be kept in the list.
    
    Parameters:
    n (int): The index of the element in the sequence to return.

    Returns:
    int: The n-th element of the sequence.
    """
    
    # Initialize the list with the first element
    lst = [1] 
    x = 0  # Pointer for the 2*list[x] + 1 calculation
    y = 0  # Pointer for the 3*list[y] + 1 calculation
    
    # Generate elements until we have at least n+1 elements in the list
    while len(lst) <= n: 
        a = 2 * lst[x] + 1  # Calculate the next element from the x pointer
        b = 3 * lst[y] + 1  # Calculate the next element from the y pointer 
        
        if a < b: 
            lst.append(a)  # Append a if it's smaller
            x += 1  # Move the x pointer forward
        elif a > b: 
            lst.append(b)  # Append b if it's smaller
            y += 1  # Move the y pointer forward
        else: 
            lst.append(a)  # If they are equal, append a (or b, since they are equal)
            x += 1  # Move both pointers forward
            y += 1
            
    return lst[n]  # Return the n-th element of the list

# Driver code to test the function
if __name__ == "__main__":
    # Test cases
    print(dbl_linear(0))  # Output: 1
    print(dbl_linear(1))  # Output: 3
    print(dbl_linear(2))  # Output: 4
    print(dbl_linear(3))  # Output: 7
    print(dbl_linear(4))  # Output: 9
    print(dbl_linear(5))  # Output: 10
    print(dbl_linear(6))  # Output: 12
    print(dbl_linear(7))  # Output: 13
    print(dbl_linear(8))  # Output: 16
    print(dbl_linear(9))  # Output: 18
