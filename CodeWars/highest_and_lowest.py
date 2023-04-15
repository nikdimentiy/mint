# CodeWars task: solution --> https://www.codewars.com/kata/554b4ac871d6813a03000035/python

def high_and_low(numbers):
    num_list = [int(num) for num in numbers.split()]
    highest = max(num_list)
    lowest = min(num_list)
    return f"{highest} {lowest}"
