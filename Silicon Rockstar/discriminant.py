# <-- This program calculates the roots of the quadratic equation
#     and displays them on the screen (in ascending order) -->

from math import sqrt


print(" *** Enter the components (coefficients) of the polynominal *** ")
print()
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a == 0:
    if b != 0:
        print(-c / b)
    if b == 0 and c == 0:
        print("Infinity number of solutions")
else:
    d = b ** 2 - 4 * a * c
    if d == 0:
        x1 = -b / (2 * a)
        print(x1)
    elif d > 0:
        x1 = (-b - sqrt(d)) / (2 * a)
        x2 = (-b + sqrt(d)) / (2 * a)
        if x1 < x2:
            print(x1, x2)
        else:
            print(x2, x1)
