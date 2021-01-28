# a small program to check password
for attempt in range(3, 0, -1):
    password = int(input("Enter password - only numbers: "
                         "(you have {} attempts left): ".format(attempt)))
    if password == 12345:
        print("Access done!")
        break
else:
    print("Access denied!")
