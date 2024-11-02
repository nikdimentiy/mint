def divisors(integer):
    """
    Calculate the divisors of a given integer.

    Parameters:
    integer (int): The integer for which to find the divisors.

    Returns:
    list: A list of divisors of the integer, excluding 1 and the integer itself.
    str: A message indicating that the integer is prime if no divisors are found.
    
    A prime number is defined as a number greater than 1 that has no positive divisors other than 1 and itself.
    """
    # Initialize an empty list to store the divisors
    a = []
    
    # Loop through all numbers from 2 to integer - 1
    for i in range(2, integer):
        # Check if i is a divisor of the integer
        if integer % i == 0:
            # If it is, append it to the list of divisors
            a.append(i)
    
    # If the list of divisors is not empty, return it; otherwise, return a message indicating the integer is prime
    return a if a else str(integer) + " is prime"

# Driver code to test the divisors function
if __name__ == "__main__":
    # Test with a composite number
    print("Divisors of 10:", divisors(10))  # Expected output: [2, 5]
    
    # Test with a prime number
    print("Divisors of 13:", divisors(13))  # Expected output: "13 is prime"
    
    # Test with another composite number
    print("Divisors of 28:", divisors(28))  # Expected output: [2, 4, 7, 14]
    
    # Test with a small prime number
    print("Divisors of 2:", divisors(2))    # Expected output: "2 is prime"

