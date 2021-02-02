flag = True
x = int(input("Enter desired number, to be checked for multiplicity: "))
k = int(input("Enter multiplicity number: "))
flag = (flag and x % k == 0)
# If the entered number is a multiple of the desired number - the result of the program is TRUE, else - FALSE
print(flag)
