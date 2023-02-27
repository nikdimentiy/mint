# A Narcissistic Number (or Armstrong Number) is a positive number which is the sum of its own digits, 
# each raised to the power of the number of digits in a given base. In this Kata, we will restrict ourselves to decimal (base 10).

# For example, take 153 (3 digits), which is narcissistic:

#     1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153


def is_narcissistic_number(number):
    num_str = str(number)
    n = len(num_str)
    total = sum(int(digit)**n for digit in num_str)
    return total == number
