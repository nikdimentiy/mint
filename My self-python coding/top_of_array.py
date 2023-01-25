# the python code: defines the top in the array
# and output the sequence of elements in reverse order
A = [0] * 10
top = 0
x = int(input("Enter number: "))
while x != 0:
    A[top] = x
    top += 1
    x = int(input("Enter any number more: (terminate = '0'): "))
for k in range(top - 1, -1, -1):
    print(A[k])
