def get_sum(a, b):
    sum_result = 0
    if a == b:
        return a
    if a < b:
        for i in range(a, b + 1):
            sum_result += i
        return sum_result
    if a > b:
        for i in range(b, a + 1):
            sum_result += i
        return sum_result


result = get_sum(0, -1)
print(result)
