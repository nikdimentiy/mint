def feast(beast: str, dish: str) -> bool:
    """
    Determine whether a given animal can bring a dish to the feast, based on the
    condition that the dish starts and ends with the same letters as the animal's name.

    The function implements the following rules:
    1. The first letter of the dish must match the first letter of the beast's name
    2. The last letter of the dish must match the last letter of the beast's name
    3. The comparison is case-sensitive

    Args:
        beast (str): The name of the animal, which must have at least two letters.
                    Example: 'great blue heron', 'chickadee', 'lion'
        dish (str): The name of the dish, which must have at least two letters and
                   start and end with the same letters as the animal's name.
                   Example: 'garlic naan', 'chocolate cake', 'tuna sandwich'

    Returns:
        bool: True if the beast is allowed to bring the dish to the feast (first and last
              letters match), False otherwise.

    Examples:
        >>> feast('great blue heron', 'garlic naan')
        True
        >>> feast('chickadee', 'chocolate cake')
        True
        >>> feast('lion', 'tuna sandwich')
        False
        >>> feast('bear', 'bark')
        True
        >>> feast('bear', 'beef')
        False
    """
    # Extract first and last letters from both strings and compare them
    # This is more efficient than slicing the entire strings
    return beast[0] == dish[0] and beast[-1] == dish[-1]


# Driver code to test the function
if __name__ == "__main__":
    # Test cases
    test_cases = [
        ('great blue heron', 'garlic naan'),
        ('chickadee', 'chocolate cake'),
        ('lion', 'tuna sandwich'),
        ('bear', 'bark'),
        ('dolphin', 'dark chocolate'),
        ('eagle', 'eggplant lasagne'),
        ('panda', 'potato soup'),
        ('seal', 'sugar cookie'),
    ]

    # Run tests and print results
    print("Testing feast function:")
    print("-" * 50)
    for beast, dish in test_cases:
        result = feast(beast, dish)
        print(f"Beast: {beast}")
        print(f"Dish: {dish}")
        print(f"Allowed to bring dish: {result}")
        print("-" * 50)
