import re


def solution(inputString: str) -> int:
    """
    Counts the number of primitive type elements in the input string.

    Args:
        inputString (str): A string that can contain a primitive type variable or an array (possibly multidimensional)
        that contains elements of the primitive types. A primitive type variable can be an integer number, a string,
        which is surrounded by double quotes, or a boolean, which is either "true" or "false".

    Returns:
        int: The total number of primitive type elements within the input string.

    Example:
        >>> solution("[[0, 20], [33, 99]]")
        4
    """
    return len(re.findall(r'(\"[^\"]*\"|\d+|true|false)', inputString))
