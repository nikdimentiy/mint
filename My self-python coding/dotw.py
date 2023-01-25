# Match Case Python: New Addition to the Language

def main():
    day_of_the_week = get_int()
    if 1 <= day_of_the_week <= 7:
        match day_of_the_week:
            case 1:
                print("Monday")
            case 2:
                print("Tuesday")
            case 3:
                print("Wednesday")
            case 4:
                print("Thursday")
            case 5:
                print("Friday")
            case 6:
                print("Saturday")
            case 7:
                print("Sunday")
    else:
        print("You entered a non-existent day of the week")


def get_int():
    while True:
        try:
            day = int(input("Enter the number of the day in week: "))
        except ValueError:
            print("You entered no integer number! Please, try again!")
        else:
            break
    return day


main()
