# A little child is studying arithmetic. They have just learned how to add two integers, written one below another,
# column by column. But the child always forgets about the important part - carrying.

# Given two integers, your task is to find the result that the child will get.


def solution(param1, param2):
    result = 0
    factor = 1
    while param1 > 0 or param2 > 0:
        digit1 = param1 % 10
        digit2 = param2 % 10
        result += ((digit1 + digit2) % 10) * factor
        factor *= 10
        param1 //= 10
        param2 //= 10
    return result
