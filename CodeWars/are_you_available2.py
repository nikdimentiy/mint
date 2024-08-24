def check_availability(schedule, current_time):
    """
    Check Dan's availability based on his meeting schedule.

    Args:
    schedule (list of list): A nested list where each inner list contains two elements:
                             the start and finish time of an appointment in 'hh:mm' format.
    current_time (str): A string representing the current time in 'hh:mm' 24-hour format.

    Returns:
    bool or str: 
        - Returns True if Dan is available (no appointments scheduled at current_time or no appointments for the day).
        - Returns a string with the time Dan will be available if he is currently in a meeting.
    """
    # Iterate through each appointment in the schedule
    for tb, te in schedule:
        # Check if the current time falls within the start and end time of the appointment
        if tb <= current_time < te:
            return te  # Return the end time of the current appointment

    return True  # Return True if no appointments are found for the current time

# Driver code to test the function
if __name__ == "__main__":
    # Example schedule: [(start_time, end_time), ...]
    schedule = [
        ["09:00", "10:00"],
        ["11:30", "12:30"],
        ["14:00", "15:00"]
    ]

    # Test cases
    current_time_1 = "08:30"  # Before any appointments
    current_time_2 = "09:30"  # During an appointment
    current_time_3 = "12:00"  # Between appointments
    current_time_4 = "15:30"  # After all appointments
    current_time_5 = "11:00"  # During an appointment

    print(check_availability(schedule, current_time_1))  # Expected output: True
    print(check_availability(schedule, current_time_2))  # Expected output: "10:00"
    print(check_availability(schedule, current_time_3))  # Expected output: True
    print(check_availability(schedule, current_time_4))  # Expected output: True
    print(check_availability(schedule, current_time_5))  # Expected output: "12:30"
