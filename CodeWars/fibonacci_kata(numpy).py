from numpy import matrix

def fib(n):
    """
    Calculate the nth Fibonacci number using matrix exponentiation.

    The Fibonacci sequence is defined as follows:
    F(0) = 0, F(1) = 1, and F(n) = F(n-1) + F(n-2) for n >= 2.

    This function uses matrix exponentiation to compute the nth Fibonacci number
    in O(log n) time complexity.

    Parameters:
    n (int): The index of the Fibonacci number to compute. Can be negative to
             compute Fibonacci numbers in the negative index (using the formula
             F(-n) = (-1)^(n+1) * F(n)).

    Returns:
    int: The nth Fibonacci number.
    """
    # Create the transformation matrix for Fibonacci sequence
    transformation_matrix = matrix('0 1; 1 1' if n >= 0 else '-1 1; 1 0', object)
    
    # Raise the transformation matrix to the power of |n|
    result_matrix = transformation_matrix ** abs(n)
    
    # Return the Fibonacci number from the resulting matrix
    return result_matrix[0, 1]

# Driver code to test the fib function
if __name__ == "__main__":
    # Test cases for the Fibonacci function
    test_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3, -4]
    
    for n in test_values:
        print(f"Fibonacci({n}) = {fib(n)}")
