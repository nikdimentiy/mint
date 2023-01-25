# Finds maximum occurring digit
# without using any array/string

# Simple function to count
# occurrences of digit d in x
def countOccurrences(x, d):
    count = 0  # Initialize count
    # of digit d
    while (x):

        # Increment count if current
        # digit is same as d
        if (x % 10 == d):
            count += 1
        x = int(x / 10)

    return count

# Returns the max occurring
# digit in x


def maxOccurring(x):

    # Handle negative number
    if (x < 0):
        x = -x

    result = 0  # Initialize result
    # which is a digit
    max_count = 1  # Initialize count
    # of result

    # Traverse through all digits
    for d in range(10):

        # Count occurrences of current digit
        count = countOccurrences(x, d)

        # Update max_count and
        # result if needed
        if (count >= max_count):
            max_count = count
            result = d

    return result


# Driver Code
x = 1223355
print("Max occurring digit is",
      maxOccurring(x))
