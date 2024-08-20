def check_availability(schedule, current_time):
    """
    Check Dan's availability based on his meeting schedule.

    Args:
    schedule (list of list): A nested list where each inner list contains two elements:
                              the start and finish time of an appointment in 'hh:mm' format.
    current_time (str): The current time in 'hh:mm' 24-hour format to check availability.

    Returns:
    bool or str: 
        - Returns True if Dan is available (no appointments scheduled at current_time).
        - Returns a string with the finish time of the current appointment if he is busy.
        - Returns True if there are no appointments scheduled for the day.
    """
    
    # Iterate through each appointment in the schedule
    for t in schedule:
        start, finish = t[0], t[1]
        
        # Check if current_time falls within the start and finish time of the appointment
        if (int(start[:2]) < int(current_time[:2]) < int(finish[:2])) or \
           (int(start[:2]) == int(current_time[:2]) and int(start[3:]) <= int(current_time[3:])) or \
           (int(finish[:2]) == int(current_time[:2]) and int(current_time[3:]) < int(finish[3:])):
            return finish  # Return the finish time of the current appointment

    # If no appointments are found, return True
    return True

# Driver code to test the function
if __name__ == "__main__":
    # Example schedule: [start_time, finish_time]
    schedule = [
        ["09:00", "10:00"],
        ["11:30", "12:30"],
        ["14:00", "15:00"]
    ]
    
    # Test cases
    current_time_1 = "10:30"  # Should return True (available)
    current_time_2 = "11:45"  # Should return "12:30" (busy until 12:30)
    current_time_3 = "14:00"  # Should return "15:00" (busy until 15:00)
    current_time_4 = "08:00"   # Should return True (available)
    current_time_5 = "15:30"   # Should return True (available)

    print(check_availability(schedule, current_time_1))  # Output: True
    print(check_availability(schedule, current_time_2))  # Output: "12:30"
    print(check_availability(schedule, current_time_3))  # Output: "15:00"
    print(check_availability(schedule, current_time_4))  # Output: True
    print(check_availability(schedule, current_time_5))  # Output: True
