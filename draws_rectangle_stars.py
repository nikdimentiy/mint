# the code draws a rectangle of stars

row = int(input("Enter needed rows: "))
column = int(input("Enter needed columns: "))

for r in range(row + 1):
    for c in range(column + 1):
        print("*", end=" ")
    print()
