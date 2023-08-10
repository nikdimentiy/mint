def print_prime_factors(number):
    """
    Prints the prime factors of a given number.

    This function takes an integer 'number' as input and prints its prime factors.

    Parameters:
    number (int): The number for which prime factors need to be printed.

    Returns:
    None
    """

    # Start with the smallest prime factor, which is 2
    factor = 2

    # Keep looping until the factor becomes larger than the number
    while factor <= number:

        # Check if the current factor is a divisor of the number
        if number % factor == 0:

            # If it is a divisor, print it as a prime factor
            print(factor)

            # Divide the number by the current factor to reduce it
            number = number / factor
        else:
            # If the current factor is not a divisor, move to the next one
            factor += 1

# Call the function with an example number
print_prime_factors(37)

