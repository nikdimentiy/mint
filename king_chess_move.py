#  king move in chess cell (the possibility of attack)

print("*** Enter the king coordinates ***")
r1 = int(input("Enter row of the king: "))
c1 = int(input("Enter column of the king: "))

print("*** Enter coordinates of the chess cell ***")
r2 = int(input("Enter row of the chess cell: "))
c2 = int(input("Enter column of the chess cell: "))

a_r = abs(r1 - r2)
a_c = abs(c1 - c2)

if (a_r == a_c or (((r1 == r2) and (c1 != c2)) or ((r1 != r2) and (c1 == c2)))) and (a_r == 1 or a_c == 1):
    print("YES")
else:
    print("NO")
