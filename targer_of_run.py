# funny code: improve your results every day by 10%

""" *** We all love running ***
    1. JUST DO IT - do running workout today
    2. Have a fun
    3. Running as you CAN
    4. Write down the result
    5. The more you run, the better your results
    6. Create the goal to run N miles (put a bigger goal more interesting will achieve it!)
    7. Increasing the load by 10% every day
    8. Try, do it, YOU CAN!
    9. BE PROUD OF YOURSELF!"""
x = int(input("Enter the starting distance of the race - (exception 'ZERO'): "))
y = int(input("Enter the desired goal: "))
i = x
day = 1
while i < y:
    i = i + i * 0.1
    day = day + 1
print("The goal will be achieved through: ", day)
