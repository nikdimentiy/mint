def gen_bin(number_of_digits: int, prefix=" "):
    if number_of_digits == 0:
        print(prefix)
        return
    gen_bin(number_of_digits - 1, prefix + "0")
    gen_bin(number_of_digits - 1, prefix + "1")


number = int(input("Enter an integer number - (number of binary digits): "))
(gen_bin(number))
