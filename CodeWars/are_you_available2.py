# Dan, president of a Large company could use your help. He wants to implement a system that
# will switch all his devices into offline mode depending on his meeting schedule.
#  When he's at a meeting and somebody texts him, he wants to send an automatic message informing that he's currently unavailable and the time when he's going to be back.

# What To Do

# Your task is to write a helper function checkAvailability that will take 2 arguments:

# schedule, which is going to be a nested array with Dan's schedule for a given day.
# Inside arrays will consist of 2 elements - start and finish time of a given appointment,
# currentTime - is a string with specific time in hh:mm 24-h format for which the function will check availability based on the schedule.
# If no appointments are scheduled for currentTime, the function should return true. If there are no appointments for the day, the output should also be true
# If Dan is in the middle of an appointment at currentTime, the function should return a string with the time he's going to be available.

def check_availability(schedule, current_time):
    for tb, te in schedule:
        if tb <= current_time < te:
            return te
    return True
