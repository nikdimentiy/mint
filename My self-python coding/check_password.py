def check_password():
    """The function checks the correctness of password entry -
        for compliance with the sample (the right password)"""
    for attempt in range(3, 0, -1):
        password = int(input("Enter password - only numbers: "
                             "(you have {} attempts left): ".format(attempt)))
        if password == 12345:
            print("Access done!")
            break
    else:
        print("Access denied!")


check_password()
