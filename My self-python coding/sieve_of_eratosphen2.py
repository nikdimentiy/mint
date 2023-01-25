print("This tiny code show algorithm of Eratospheve sieve: ")
number_of_limit = int(input("Enter the integer number:(limit of range) "))
A = [True] * (number_of_limit + 1)
A[0] = A[1] = False

for k in range(2, number_of_limit):
    if A[k]:
        for m in range(2 * k, number_of_limit, k):
            A[m] = False

for k in range(2, number_of_limit + 1):
    print(k, ' - ', "Prime number" if A[k] else "Complex number")
