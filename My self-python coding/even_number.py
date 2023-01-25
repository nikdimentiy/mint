# the program to calculate an even number with functional decomposition


def main():
    number = get_int()
    result = isEven(number)
    if result == True:
        print("You entered a EVEN number✅")
    else:
        print("You entered a odd number!👍")


def get_int():
    while True:
        try:
            return int(input(" 🤠 Enter integer number, please: 🤠 "))
        except ValueError:
            print("💢💢💢 This is not a number....please enter a number: 💢💢💢")


def isEven(number):
    return number % 2 == 0


main()
