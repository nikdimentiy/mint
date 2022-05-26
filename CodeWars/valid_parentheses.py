def valid_parentheses(string):
    stack = 0
    for c in string:
        if c == '(':
            stack += 1
        if c == ')':
            stack -= 1
        if stack < 0:
            return False
    return stack == 0
