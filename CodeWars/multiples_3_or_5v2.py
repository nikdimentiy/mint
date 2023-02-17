# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
# Additionally, if the number is negative, return 0 (for languages that do have them).

# Note: If the number is a multiple of both 3 and 5, only count it once.


def solution(number):
    # If the number is negative, return 0
    if number < 0:
        return 0

    # Initialize the sum to 0
    sum = 0

    # Loop through all the natural numbers below the number
    for i in range(1, number):
        # If the number is a multiple of 3 or 5, add it to the sum
        if i % 3 == 0 or i % 5 == 0:
            sum += i

    # Return the sum
    return sum
