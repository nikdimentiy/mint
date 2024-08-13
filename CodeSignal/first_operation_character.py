def solution(expr: str) -> int:
    """
    Finds the index of the operator in a valid arithmetic expression that needs to be computed first.

    The function evaluates the expression to determine the operator with the highest priority
    that is not enclosed in parentheses. If multiple operators have the same highest priority,
    the function returns the index of the leftmost one.

    Args:
    - expr (str): A string representing a valid arithmetic expression consisting of digits, parentheses,
                  addition ('+') and multiplication ('*') signs. It is guaranteed that there is at least
                  one operator in it.

    Returns:
    - int: The index of the operator in the expression that needs to be computed first. If multiple operators
           have the same highest priority, the function returns the index of the leftmost one.

    Example:
    >>> solution("3 + 5 * (2 + 8)")
    4
    >>> solution("(1 + 2) * 3 + 4")
    1
    >>> solution("5 * (6 + 2) + 3")
    0
    """
    lvl = 0
    lvl_char = {}
    priority = {'+': 1, '*': 2}

    for i, char in enumerate(expr):
        if char == '(':
            lvl += 1
        elif char == ')':
            lvl -= 1
        elif char in priority:
            if lvl not in lvl_char:
                lvl_char[lvl] = (char, i)
            else:
                if priority[char] > priority[lvl_char[lvl][0]]:
                    lvl_char[lvl] = (char, i)

    return lvl_char[max(lvl_char.keys())][1]

# Driver code to test the solution function
if __name__ == "__main__":
    test_expressions = [
        "3 + 5 * (2 + 8)",
        "(1 + 2) * 3 + 4",
        "5 * (6 + 2) + 3",
        "2 * (3 + 4 * (5 + 6)) + 1",
        "1 + 2 * 3 + 4 * 5"
    ]

    for expr in test_expressions:
        index = solution(expr)
        print(f"The first operator to compute in '{expr}' is at index: {index}")
