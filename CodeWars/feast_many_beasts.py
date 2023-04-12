# CodeWars task solution: https://www.codewars.com/kata/5aa736a455f906981800360d/python

def feast(beast: str, dish: str) -> bool:
    """
    Determine whether a given animal can bring a dish to the feast, based on the
    condition that the dish starts and ends with the same letters as the animal's name.

    Args:
    - beast (str): The name of the animal, which must have at least two letters.
    - dish (str): The name of the dish, which must have at least two letters and
      start and end with the same letters as the animal's name.

    Returns:
    - bool: True if the beast is allowed to bring the dish to the feast, False otherwise.

    Examples:
    >>> feast('great blue heron', 'garlic naan')
    True
    >>> feast('chickadee', 'chocolate cake')
    True
    >>> feast('lion', 'tuna sandwich')
    False
    """
    return beast[0] == dish[0] and beast[-1] == dish[-1]
