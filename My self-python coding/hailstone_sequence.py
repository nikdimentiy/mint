# the tiny code: represent the hailstone sequence

n = int(input("Enter the integer number, for calculate the hailstone sequence: "))
cnt = 0
while n != 1:
    print(int(n))
    if n % 2 == 0:
        n = n / 2
    else:
        n = n * 3 + 1
    cnt += 1

print(int(n))
print("The total iteration of the hailstone sequence is: ", cnt)
