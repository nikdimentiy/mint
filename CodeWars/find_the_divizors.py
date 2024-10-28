def divisors(integer):
    """
    Calculate the divisors of a given integer.

    This function returns a list of all divisors of the input integer that are 
    greater than 1. If the integer is prime (i.e., it has no divisors other 
    than 1 and itself), the function returns a message indicating that the 
    integer is prime.

    Parameters:
    integer (int): The integer for which to find divisors.

    Returns:
    list or str: A list of divisors greater than 1 if any exist, 
                 otherwise a message indicating the integer is prime.
    """
    # Generate a list of divisors by checking each number from 2 to integer-1
    l = [n for n in range(2, integer) if integer % n == 0]
    
    # Return the list of divisors if found, otherwise return a prime message
    return l if len(l) > 0 else "{} is prime".format(integer)


# Driver code to test the divisors function
if __name__ == "__main__":
    # Test cases for the divisors function
    test_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    
    for n in test_values:
        result = divisors(n)
        print(f"Divisors of {n}: {result}")
