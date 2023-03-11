n = int(input("Enter number to calculate sum: "))
sum = 0
for num in range(0, n+1, 1):
    sum = sum+num
print("The sum of first", n, "numbers is: ", sum )
