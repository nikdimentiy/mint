
day = int(input("Enter the number of the day in week: "))

# new feature of Python 3.10 (analog swith-case in Java, C, C++)
match day:
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
 
