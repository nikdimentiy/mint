from enum import Enum

# define an enum named Month with 12 constants for the months of the year
class Month(Enum):
    JANUARY = 31
    FEBRUARY = 28
    MARCH = 31
    APRIL = 30
    MAY = 31
    JUNE = 30
    JULY = 31
    AUGUST = 31
    SEPTEMBER = 30
    OCTOBER = 31
    NOVEMBER = 30
    DECEMBER = 31

# define a main function that runs the program
def main():
    # declare a variable of type Month and assign it the value of JANUARY
    month = Month.JANUARY
    # print out the number of days in JANUARY using the value attribute
    print("Number of days in", month.name, ":", month.value)

    # assign the value of FEBRUARY to the month variable
    month = Month.FEBRUARY
    # print out the number of days in FEBRUARY using the value attribute
    print("Number of days in", month.name, ":", month.value)

    # assign the value of MARCH to the month variable
    month = Month.MARCH
    # print out the number of days in MARCH using the value attribute
    print("Number of days in", month.name, ":", month.value)

# call the main function to run the program
if __name__ == '__main__':
    main()
