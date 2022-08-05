# the program to calculate an even number with functional decomposition

def main():
    number = get_int()
    result = isEven(number)
    if result == True:
        print("You entered a EVEN number!")
    else:
        print("You entered a odd number!")


def get_int():
    while (True):
        try:
            number = int(input("Enter integer number, please: "))
            break
        except ValueError:
            print("This is not a number. Please enter a number: ")
    return number


def isEven(number):
    return number % 2 == 0


main()
