# code which reads numbers from the console (one per line),
# until the sum of the entered numbers equals 0 and immediately,
# after that displays the sum of the squares of all the numbers read

a1 = int(input("Enter integer number, please: "))
s = a1
s2 = 0 + abs(a1 ** 2)
while s != 0:
    a1 = int(input())
    s = s + a1
    s2 = s2 + abs(a1) ** 2
    if s == 0:
        break
print(s2)
