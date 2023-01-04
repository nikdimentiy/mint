def print_prime_factors(number):
    # Start with two, which is the first prime
    factor = 2
    # Keep going until the factor is larger than the number
    while factor <= number:
        # Check if factor is a divisor of number
        if number % factor == 0:
            print(factor)
            number = number / factor
        else:
            # If it's not, increment the factor by one
            factor += 1


print_prime_factors(37)
