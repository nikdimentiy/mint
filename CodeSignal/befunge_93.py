def solution(program):

    grid = list(map(list, program))
    px, py = 0, 0
    dx, dy = 0, 1
    sin = False
    res, stack = [], [0]
    cc = 0
    while cc < 10 ** 5 and len(res) < 100:
        c = grid[px][py]
        if c == "\"":
            sin = not sin
        elif sin:
            stack.append(ord(c))
        elif c == ">":
            dx, dy = 0, 1
        elif c == "<":
            dx, dy = 0, -1
        elif c == "v":
            dx, dy = 1, 0
        elif c == "^":
            dx, dy = -1, 0
        elif c == "#":
            px += dx
            py += dy
        elif c == "_":
            if stack.pop():
                dx, dy = 0, -1
            else:
                dx, dy = 0, 1
        elif c == "|":
            if stack.pop():
                dx, dy = -1, 0
            else:
                dx, dy = 1, 0
        elif c == "+":
            if len(stack) < 2:
                stack = [0] * (2 - len(stack)) + stack
            stack.append(stack.pop() + stack.pop())
        elif c == "-":
            if len(stack) < 2:
                stack = [0] * (2 - len(stack)) + stack
            stack.append(-stack.pop() + stack.pop())
        elif c == "*":
            if len(stack) < 2:
                stack = [0] * (2 - len(stack)) + stack
            stack.append(stack.pop() * stack.pop())
        elif c == "/":
            if len(stack) < 2:
                stack = [0] * (2 - len(stack)) + stack
            a, b = stack.pop(), stack.pop()
            stack.append(b // a)
        elif c == "%":
            if len(stack) < 2:
                stack = [0] * (2 - len(stack)) + stack
            a, b = stack.pop(), stack.pop()
            stack.append(b % a)
        elif c == "!":
            if stack.pop():
                stack.append(0)
            else:
                stack.append(1)
        elif c == "`":
            if len(stack) < 2:
                stack = [0] * (2 - len(stack)) + stack
            if stack.pop() < stack.pop():
                stack.append(1)
            else:
                stack.append(0)
        elif c == ":":
            if stack:
                stack.append(stack[-1])
        elif c == "\\":
            stack[-2:] = stack[-2:][::-1]
        elif c == "$":
            stack.pop()
        elif c == ".":
            res.append(str(stack.pop()))
            res.append(" ")
        elif c == ",":
            res.append(chr(stack.pop()))
        elif "0" <= c <= "9":
            stack.append(int(c))
        elif c == "@":
            break
        px += dx
        py += dy
        px %= len(grid)
        py %= len(grid[0])
        cc += 1
    return "".join(res)[:100]
