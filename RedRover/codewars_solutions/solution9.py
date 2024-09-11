def is_afraid(day: str, number: int) -> bool:
    """
    Determine if the zombie is afraid based on the day of the week and a given number.

    The zombie has different fears for each day of the week:
    - Monday: Afraid of the number 12
    - Tuesday: Afraid of numbers greater than 95
    - Wednesday: Afraid of the number 34
    - Thursday: Afraid of the number 0
    - Friday: Afraid of even numbers
    - Saturday: Afraid of the number 56
    - Sunday: Afraid of the numbers 666 and -666

    Parameters:
    day (str): The day of the week
    number (int): The number to check against

    Returns:
    bool: True if the zombie is afraid, False otherwise

    Raises:
    ValueError: If an invalid day of the week is provided
    """
    day = day.lower()  # Normalize the day to lowercase for consistency
    
    # Check fear conditions for each day of the week
    if day == "monday":
        return number == 12
    elif day == "tuesday":
        return number > 95
    elif day == "wednesday":
        return number == 34
    elif day == "thursday":
        return number == 0
    elif day == "friday":
        return number % 2 == 0  # Check if the number is even
    elif day == "saturday":
        return number == 56
    elif day == "sunday":
        return number == 666 or number == -666
    else:
        raise ValueError("Invalid day of the week")

# Driver code
if __name__ == "__main__":
    # Test cases
    test_cases = [
        ("Monday", 12),
        ("Tuesday", 96),
        ("Wednesday", 34),
        ("Thursday", 0),
        ("Friday", 4),
        ("Saturday", 56),
        ("Sunday", 666),
        ("Sunday", -666),
        ("Monday", 13),
        ("Tuesday", 95),
        ("Wednesday", 35),
        ("Thursday", 1),
        ("Friday", 3),
        ("Saturday", 57),
        ("Sunday", 665)
    ]

    # Run test cases
    for day, number in test_cases:
        result = is_afraid(day, number)
        print(f"Is the zombie afraid on {day} with number {number}? {result}")

    # Test invalid day
    try:
        is_afraid("InvalidDay", 10)
    except ValueError as e:
        print(f"Error: {e}")