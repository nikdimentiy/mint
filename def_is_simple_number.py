def is_simple_number(x):
    """ Determines if the number is prime.
        x is a positive integer.
        If simple, then it returns True, otherwise - False"""
    divisor = 2
    while divisor < x:
        if x % divisor == 0:
            return False
        divisor += 1
    return True
number = int(input("Enter the integer number, please: "))
result = is_simple_number(number)
if result == True:
    print("The entered number is simple!")
else:
    print("The number has more than two divisors!")

