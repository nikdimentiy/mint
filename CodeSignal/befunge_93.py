def solution(program):
    """
    Executes a Brainfuck-like program represented as a grid of characters.

    The program can manipulate a stack and navigate through a 2D grid based on specific commands.
    
    Parameters:
    program (list of str): A list of strings representing the grid of commands.

    Returns:
    str: The output generated by the program, limited to the first 100 characters.
    """
    
    # Convert the input program into a 2D grid
    grid = list(map(list, program))
    
    # Initialize position and direction
    px, py = 0, 0  # Current position in the grid
    dx, dy = 0, 1  # Initial direction (moving right)
    
    # State variables
    sin = False  # Indicates if we are in string mode
    res = []  # Output result
    stack = [0]  # Stack for operations
    cc = 0  # Command counter

    # Main execution loop
    while cc < 10 ** 5 and len(res) < 100:
        c = grid[px][py]  # Current command

        # Handle string mode
        if c == "\"":
            sin = not sin  # Toggle string mode
        elif sin:
            stack.append(ord(c))  # Push ASCII value of character onto stack
        else:
            # Handle movement and stack operations based on the command
            if c == ">":
                dx, dy = 0, 1  # Move right
            elif c == "<":
                dx, dy = 0, -1  # Move left
            elif c == "v":
                dx, dy = 1, 0  # Move down
            elif c == "^":
                dx, dy = -1, 0  # Move up
            elif c == "#":
                # Move in the current direction
                px += dx
                py += dy
            elif c == "_":
                # Conditional horizontal movement based on stack top
                dx, dy = (0, -1) if stack.pop() else (0, 1)
            elif c == "|":
                # Conditional vertical movement based on stack top
                dx, dy = (-1, 0) if stack.pop() else (1, 0)
            elif c in "+-*%/!`":
                # Arithmetic operations
                if len(stack) < 2:
                    stack = [0] * (2 - len(stack)) + stack  # Ensure at least 2 items
                if c == "+":
                    stack.append(stack.pop() + stack.pop())
                elif c == "-":
                    a, b = stack.pop(), stack.pop()
                    stack.append(b - a)
                elif c == "*":
                    stack.append(stack.pop() * stack.pop())
                elif c == "/":
                    a, b = stack.pop(), stack.pop()
                    stack.append(b // a)
                elif c == "%":
                    a, b = stack.pop(), stack.pop()
                    stack.append(b % a)
            elif c == "!":
                # Logical NOT operation
                stack.append(0 if stack.pop() else 1)
            elif c == "`":
                # Comparison operation
                if len(stack) < 2:
                    stack = [0] * (2 - len(stack)) + stack
                stack.append(1 if stack.pop() < stack.pop() else 0)
            elif c == ":":
                # Duplicate the top of the stack
                if stack:
                    stack.append(stack[-1])
            elif c == "\\":
                # Swap the top two elements of the stack
                stack[-2:] = stack[-2:][::-1]
            elif c == "$":
                # Pop the top element of the stack
                stack.pop()
            elif c == ".":
                # Output the top of the stack as a string
                res.append(str(stack.pop()) + " ")
            elif c == ",":
                # Output the top of the stack as a character
                res.append(chr(stack.pop()))
            elif "0" <= c <= "9":
                # Push numeric values onto the stack
                stack.append(int(c))
            elif c == "@":
                # End the program
                break

        # Update position and wrap around the grid
        px = (px + dx) % len(grid)
        py = (py + dy) % len(grid[0])
        cc += 1  # Increment command counter

    return "".join(res)[:100]  # Return the first 100 characters of the output
