def even_or_odd(number: int) -> str:
    """
    This function determines whether a given number is even or odd.

    Parameters:
    number (int): The number to be checked.

    Returns:
    str: "Even" if the number is even, "Odd" otherwise.
    """
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


# Test cases
print(even_or_odd(4))  # Output: Even
print(even_or_odd(7))  # Output: Odd
print(even_or_odd(0))  # Output: Even
print(even_or_odd(-3))  # Output: Odd

# def even_or_odd(number):
#     """
#     This function determines whether a given number is even or odd.

#     Parameters:
#     number (int): The number to be checked.

#     Returns:
#     str: "Even" if the number is even, "Odd" otherwise.
#     """
#     return "Even" if number % 2 == 0 else "Odd"


# # Test cases
# print(even_or_odd(4))  # Output: Even
# print(even_or_odd(7))  # Output: Odd
# print(even_or_odd(0))  # Output: Even
# print(even_or_odd(-3))  # Output: Odd