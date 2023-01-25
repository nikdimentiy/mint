# This program calculate trade commission

keep_going = 'g'
while keep_going == 'g':
    sales = float(input("Enter the volume of sales: "))
    commission_rate = float(input("Enter commission rate: "))
    commission = sales * commission_rate
    print("Result of total commission is $", format(commission, '.2f'), sep='')
    print("Would you like calculate one more operation?")
    keep_going = input("If your answer is 'YES' - press 'g' button, "
                       "If 'NO' - press any button! ")

