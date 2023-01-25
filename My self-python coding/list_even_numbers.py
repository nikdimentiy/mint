def even_numbers(number):
    return list(filter(lambda x: x % 2 == 0, range(1, number)))


num = int(input("Please enter your number: "))
print(even_numbers(num))
