def check_pin_code():
    """The function checks the correctness of PIN code entry """

    pin_length_check = False # flag to checking of length to input (4 numbers)
    pin_code_access = False # flag to checking for correct login password
    attempt = 3
    while attempt != 0:
        pin_code = input(f"Enter your PIN code - only numbers! You have {attempt} attempts left: ")

        if len(pin_code) == 4:
            pin_length_check = True
            attempt -= 1

            if int(pin_code) == 1234:# correct PIN code
                pin_code_access = True

            if pin_length_check and pin_code_access: # conditions to access -> input in system
                print("Access done! Welcome!")
                break

        else:
            print("The pin-code must contains 4 numbers!") # condition: checking for a valid number of input attempts (while loops --> attempt != 0)
            attempt -= 1

    if attempt == 0 and not pin_code_access:
        print("Access denied!")


check_pin_code()
