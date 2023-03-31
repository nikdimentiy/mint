# CodeWars task: solution --> https://www.codewars.com/kata/546e416c8e3b6bf82f0002f2/train/python


def bind(lst, func):
    """
    Maps the given function to the elements of the list and flattens the result.

    Args:
    lst -- A list of elements.
    func -- A function that takes an element of the list as input and returns a list of elements as output.

    Returns:
    A flattened list of the results of applying the function to each element of the input list.
    """
    result = []
    for x in lst:
        mapped = func(x)
        if not isinstance(mapped, list):
            raise ValueError("The function must return a list.")
        result.extend(mapped)
    return result
