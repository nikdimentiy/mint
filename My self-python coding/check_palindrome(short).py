# the code analyzes whether the entered value is a palindrome (short version)

string_1 = input("Enter the needed value: ")
reverse_string = string_1[::-1]

if string_1 == reverse_string:
    print("YES - entered value is palindrome!")
else:
    print("NO - this value in not palindrome!")
