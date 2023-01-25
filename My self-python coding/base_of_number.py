primary_list = []
base = int(input("Enter needed numerical system: "))
n = int(input("Enter the number: (for convert) "))
number = n
while number > 0:
    digit = number % base
    number //= base
    primary_list.append(digit)

result_list = primary_list[::-1]
result_list = [str(x) for x in result_list]
result_number = ''.join(result_list)
print("The result of operation: a number {0} in numerical system by base {1} = ".format(n, base), result_number)
