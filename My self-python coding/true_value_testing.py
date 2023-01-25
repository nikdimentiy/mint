# Checking the "True" value for default data types
string = input("Enter a string: ")

if string:
    print("The string is {}".format(string))

number = int(input("Enter a number: "))
if number:
    print("Number is not equal to 0")
else:
    print("The number is zero")
