from math import sqrt

""" <-- This program calculates the roots of the quadratic equation
    and displays them on the screen (in ascending order) --> """

print(" *** Enter the components (coefficients) of the polynomial *** ")
print()
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

discriminant = (b ** 2 - 4 * a * c)
if a == 0:
    if b != 0:
        print(-c / b)
    if c == 0 and b == 0:
        print("Infinity number of solution.")
elif discriminant == 0:
    x1 = -b / (2 * a)
    print(x1)
elif discriminant > 0:
    x1 = (-b + sqrt(discriminant)) / 2 * a
    x2 = (-b - sqrt(discriminant)) / 2 * a
    if x1 > x2:
        print(x2, x1)
    else:
        print(x1, x2)
