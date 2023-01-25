# The program shows: what minute right now
from datetime import datetime

A_minute_even = [] # create an empty list of the even minutes
A_minute_odd = [] # create an empty list of the odd minutes

for k in range(61): # create a loop to 60 iteration - like 60 minutes in one hour
    if k % 2 == 0:
        A_minute_even.append(k)
    else:
        A_minute_odd.append(k)
    
this_minute = datetime.today().minute

print("Now:", this_minute, "min")
if this_minute in A_minute_even:
    print("This minute is even")
else:
    print("This minute is odd!")
