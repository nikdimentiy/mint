# CodeWars task - https://www.codewars.com/kata/5572392fee5b0180480001ae/train/python

def computer_to_phone(input_str):
    # Define a dictionary that maps computer keypad numbers to phone keypad numbers
    mapping = {
        "0": "0",
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "7": "7",
        "8": "8",
        "9": "9",
        "7": "1",
        "8": "2",
        "9": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "1": "7",
        "2": "8",
        "3": "9"
    }
    # Convert each character in the input string using the mapping dictionary
    phone_str = ""
    for char in input_str:
        phone_str += mapping[char]
    return phone_str
