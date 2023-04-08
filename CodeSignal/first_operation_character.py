def solution(expr: str) -> int:
    """
    Finds the index of the operator in a valid arithmetic expression that needs to be computed first.

    Args:
    - expr (str): a string representing a valid arithmetic expression consisting of digits, parentheses,
                  addition and multiplication signs. It is guaranteed that there is at least one operator in it.

    Returns:
    - int: the index of the operator in the expression that needs to be computed first. If multiple operators
           have the same highest priority, the function returns the index of the leftmost one.
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
