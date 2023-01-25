A = [1, 3, 6, 8, 9, 3]


def sumOfList(*args):  # variable-length argument list
    sum = 0
    for i in args:
        sum += i
    return sum


result = sumOfList(*A)  # unpacking list --> argument in function
print(result)
