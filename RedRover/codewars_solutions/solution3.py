def switch_gravity(direction: str, cubes: list[int]) -> list[int]:
    """
    This function simulates the effect of gravity on a set of cubes based on the given direction.
    If the direction is 'R', the cubes are sorted in ascending order.
    If the direction is 'L', the cubes are sorted in descending order.

    Args:
        direction (str): The direction of gravity ('R' for right, 'L' for left).
        cubes (list): A list of integers representing the cubes.

    Returns:
        list: A list of integers representing the cubes sorted based on the direction of gravity.
    """
    if direction == "R":
        return sorted(cubes)
    elif direction == "L":
        return sorted(cubes, reverse=True)


# Test cases
print(switch_gravity("R", [3, 2, 1, 2]))  # Output: [1, 2, 2, 3]
print(switch_gravity("L", [1, 4, 5, 3, 5]))  # Output: [5, 5, 4, 3, 1]
