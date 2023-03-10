# CodeWars task - https://www.codewars.com/kata/5572392fee5b0180480001ae/train/python

def computer_to_phone(numbers):
    return numbers.translate(str.maketrans('123789', '789123'))
