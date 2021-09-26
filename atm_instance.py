def show_balance(balance):
    print(f"Current Balance: ${balance}")


def deposit(balance):
    amount = float(input("Enter amount to deposit: "))
    return balance + amount


def withdraw(balance):
    amount = float(input("Enter amount to withdraw: "))
    if balance > amount:
        return balance - amount
    else:
        return balance


def logout(name):
    print(f"Goodbye {name}!")


def check_pin_code(pin):
    """The function checks the correctness of PIN code entry """

    pin_length_check = False  # flag to checking of length to input (4 numbers)
    pin_code_access = False  # flag to checking for correct login password
    pin_to_validate = False
    attempt = 3
    while attempt != 0:
        pin_code = input(
            f"Enter your PIN code. You have {attempt} attempts left: ")

        if len(pin_code) == 4:
            attempt -= 1

            if int(pin_code) == pin:  # correct PIN code
                return True

        else:
            # condition: checking for a valid number of input attempts (while loops --> attempt != 0)
            print("The pin-code must contains 4 numbers!")
            attempt -= 1

    if attempt == 0 and not pin_code_access:
        print("Access denied!")
        return False


        from banking_pkg import account


        def atm_menu(name):
            print("")
            print("          === Automated Teller Machine ===          ")
            print("User: " + name)
            print("------------------------------------------")
            print("| 1.    Balance     | 2.    Deposit      |")
            print("------------------------------------------")
            print("------------------------------------------")
            print("| 3.    Withdraw    | 4.    Logout       |")
            print("------------------------------------------")


        print("          === Automated Teller Machine ===          ")

        # Declare 3 boolean variables for (FLag) conditions
        # Declare variable 'pin' --> which we will use as an argument for the function:
        # of checking the correctness of pin code input
        name_check_length = False
        pin_check_length = False
        pin_to_validate = False
        pin = ""

        while True:
            name = input("Enter name to register: ")
            if name == '':
                print("Please enter your name: ")
            elif len(name) <= 10:
                name_check_length = True
                break

            else:
                print("<--- The maximum name length is 10 characters --->")
        if name_check_length == True:
            while True:
                pin = (input("Enter PIN: "))
                if len(pin) == 4:
                    pin_check_length = True
                    break
                else:
                    print("PIN must contain 4 numbers")
            balance = 0
            print(f"{name.title()} has been registered with a starting balance of $" + str(balance))

            while (True):
                print("LOGIN")
                name_to_validate = input("Enter your name: ")
                if name_to_validate != name:
                    print("*** Wrong name!No registered user! ***")
                if name_to_validate == name:
                    pin_to_validate = account.check_pin_code(int(pin))

                if (name_to_validate == name) and (pin_to_validate == True):
                    print("Login successful!")
                    break
                else:
                    print("Invalid credentials!")

            while (True):
                atm_menu(name)
                option = input("Choose an option: ")
                if option == "1":
                    show_balance(balance)
                elif option == "2":
                    balance = account.deposit(balance)
                    show_balance(balance)
                elif option == "3":
                    balance = account.withdraw(balance)
                    show_balance(balance)
                elif option == "4":
                    logout(name)
                    break
