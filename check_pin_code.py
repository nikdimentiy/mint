def check_pin_code():
    """The function checks the correctness of PIN code entry """

    pin_length_check = False
    pin_code_access = False
    attempt = 3
    while attempt != 0:
        pin_code = input(f"Enter your PIN code - only numbers! You have {attempt} attempts left: ")

        if len(pin_code) == 4:
            pin_length_check = True
            attempt -= 1

            if int(pin_code) == 1234:
                pin_code_access = True

            if pin_length_check and pin_code_access:
                print("Access done! Welcome!")
                break

        else:
            print("The pin-code must contains 4 numbers!")
            attempt -= 1

    if attempt == 0 and not pin_code_access:
        print("Access denied!")


check_pin_code()
