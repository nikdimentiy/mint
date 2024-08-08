from datetime import datetime, timedelta

def solution(someTime: str, leavingTime: str) -> str:
    """
    Given a starting time of a clock and a leaving time, return the time shown on the clock at the leaving time,
    assuming that the clock goes backwards after someTime. The time format is "YYYY-MM-DD HH:MM".

    Parameters:
    someTime (str): The starting time in the format "YYYY-MM-DD HH:MM".
    leavingTime (str): The leaving time in the format "YYYY-MM-DD HH:MM".

    Returns:
    str: The time shown on the clock at the leaving time in the format "YYYY-MM-DD HH:MM".
    
    Example:
    >>> solution("2023-10-01 12:00", "2023-10-01 14:00")
    '2023-10-01 10:00'
    
    >>> solution("2023-10-01 12:00", "2023-10-02 10:00")
    '2023-10-01 22:00'
    """
    # convert input strings to datetime objects
    some_time = datetime.strptime(someTime, "%Y-%m-%d %H:%M")
    leaving_time = datetime.strptime(leavingTime, "%Y-%m-%d %H:%M")

    # calculate elapsed time in seconds
    elapsed_time = (leaving_time - some_time).total_seconds()

    # adjust elapsed time for backwards clock movement
    elapsed_time *= -1

    # adjust some_time by one day if leaving_time is before some_time
    if elapsed_time < 0:
        some_time -= timedelta(days=1)
        elapsed_time += 86400

    # subtract elapsed time from some_time to get clock time at leaving_time
    clock_time = some_time - timedelta(seconds=elapsed_time)

    # format the result as a string in the original format
    return clock_time.strftime("%Y-%m-%d %H:%M")

# Driver code to test the solution function
if __name__ == "__main__":
    # Test cases
    print(solution("2023-10-01 12:00", "2023-10-01 14:00"))  # Expected output: '2023-10-01 10:00'
    print(solution("2023-10-01 12:00", "2023-10-02 10:00"))  # Expected output: '2023-10-01 22:00'
    print(solution("2023-10-01 00:00", "2023-10-01 01:00"))  # Expected output: '2023-09-30 23:00'
    print(solution("2023-10-01 23:00", "2023-10-02 00:30"))  # Expected output: '2023-10-01 21:30'
