def find_outlier(arr):
    """
    Finds the outlier integer in an array of integers.

    The array is either entirely comprised of odd integers or entirely comprised of even integers,
    except for a single outlier integer N. This function identifies and returns N.

    Args:
        arr (list): An array of integers with at least 3 elements.

    Returns:
        int: The outlier integer N.
    """
    # Separate the array into two lists: one for odd numbers and one for even numbers
    odds = [x for x in arr if x % 2 != 0]  # List of odd numbers
    evens = [x for x in arr if x % 2 == 0]  # List of even numbers

    # Determine which list has only one element (the outlier) and return it
    return odds[0] if len(odds) < len(evens) else evens[0]


# Driver code
if __name__ == "__main__":
    # Test cases
    print(find_outlier([2, 4, 6, 8, 10, 3]))  # Output: 3 (outlier is odd)
    print(find_outlier([1, 3, 5, 7, 9, 10]))  # Output: 10 (outlier is even)
    print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))  # Output: 160 (outlier is even)
    print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))  # Output: 11 (outlier is odd)
