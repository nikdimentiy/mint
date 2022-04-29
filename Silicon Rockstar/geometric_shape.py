"""Select the needed shape of geometric figure like: rectangle, circle, triangle"""

import math

print("Enter the type of geometric shape (you need select the appropriate number): ")
print('''SELECT:
    1. Rectangle
    2. Circle
    3. Triangle
''')

shape = input()

if shape == "1":
    a = float(input("Enter the length of the rectangle: "))
    b = float(input("Enter the width of the rectangle: "))

    areaRectangle = a * b
    print("The area of the rectangle is: ", areaRectangle)

elif shape == "2":
    r = float(input("Enter circle radius: "))
    p = 3.14

    areaCircle = p * (pow(r, 2))
    print("The area of circle is: ", areaCircle)

elif shape == "3":
    a = float(input("Enter the length of first side: "))
    b = float(input("Enter the length of second side: "))
    c = float(input("Enter the length of third side: "))

    half_of_perimetr = (a + b + c) / 2

    p1 = half_of_perimetr - a
    p2 = half_of_perimetr - b
    p3 = half_of_perimetr - c

    areaTriangle = math.sqrt(half_of_perimetr * p1 * p2 * p3)
    print("The area of triangle is: ", areaTriangle)


