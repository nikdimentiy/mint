def check_bracket(string):
    pseudo_stack = []

    bracket_dict = {
        ')': '(',
        ']': '[',
        '}': '{',
    }

    for s in string:
        if s in bracket_dict.values():
            pseudo_stack.append(s)
        else:
            if not pseudo_stack:
                return False
            else:
                if pseudo_stack[-1] == bracket_dict.get(s):
                    del pseudo_stack[-1]
                else:
                    return False

    return False if pseudo_stack else True


print(check_bracket("(([]))"))
