number = int(input("Enter a positive number, please: "))

reversed_number = 0
tmp_original = number

while tmp_original > 0:
    reversed_number = (reversed_number * 10) + tmp_original % 10
    tmp_original = tmp_original // 10

if number == reversed_number:
    print("It's POLINDROME")
else:
    print("No Polindrome")
