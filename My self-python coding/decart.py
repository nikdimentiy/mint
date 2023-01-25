print("Enter the coordinates of the point, please: ")
x = int(input("Enter abscissa value: "))
y = int(input("Enter ordinate value: "))

if y > 0:
    if x > 0:
        print("1 Quarter")
    else:
        print("2 Quarter")
else:
    if x < 0:
        print("3 Quarter")
    else:
        print("4 Quarter")
