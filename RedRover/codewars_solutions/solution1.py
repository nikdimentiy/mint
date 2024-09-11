def calculate_blank_pages(n: int, m: int) -> int:
    """
    This function calculates the total number of blank pages needed for a given number of classmates and paperwork pages.

    Parameters:
    n (int): The number of classmates.
    m (int): The number of paperwork pages.

    Returns:
    int: The total number of blank pages needed. If either n or m is less than 0, returns 0.
    """
    if n < 0 or m < 0:
        return 0
    else:
        return n * m


# Test cases
print(calculate_blank_pages(5, 5))  # Output: 25
print(calculate_blank_pages(-5, 5))  # Output: 0


# def calculate_blank_pages(n: int, m: int) -> int:
#     return 0 if n < 0 or m < 0 else n * m


# # Test cases
# print(calculate_blank_pages(5, 5))  # Output: 25
# print(calculate_blank_pages(-5, 5))  # Output: 0
