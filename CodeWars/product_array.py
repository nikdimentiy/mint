# CodeWars task - https://www.codewars.com/kata/5a905c2157c562994900009d/python


def product_array(arr):
    total_product = 1
    for num in arr:
        total_product *= num
    output = []
    for num in arr:
        output.append(total_product // num)
    return output
