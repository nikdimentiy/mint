# The mini-program calculates the degrees of the entered number in range
import math
n = 1
x = int(input("Enter any integer number: "))
degree = int(input("Enter the needed range of degree: "))
print()
count = 1
while count <= degree:
    print(count, "degree of the entered number is: ", pow(x, n))
    n +=1
    count +=1
print("\n")
print("Finish operation")