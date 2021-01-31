# funny code: improve your results every day by 10%

""" *** We all love running ***
    1. JUST DO IT - do running workout today
    2. Have a fun
    3. Running as you CAN
    4. Write down the result
    5. The more you run, the better your results
    6. Create the goal to run N miles
    7. Increasing the load by 10% every day
    8. Try, do it, YOU CAN!
    9. BE PROUD OF YOURSELF!"""
x = int(input("Enter the starting distance of the race: "))
y = int(input("Enter the desired goal: "))
i = x
day_workout_goal = []
day = 1
while i < y:
    i = i + i * 0.1
    i = round(i, 2)
    day_workout_goal.append(i)
    day = day + 1
cast_day_workout_goal = str(day_workout_goal)

print("The goal will be achieved through: ", day - 1)
print()
print("The list of goals to daily running workout: ")
print(cast_day_workout_goal)