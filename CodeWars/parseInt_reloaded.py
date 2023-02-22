# In this kata we want to convert a string into an integer.
# The strings simply represent the numbers in words.

# Examples:

# "one" => 1
# "twenty" => 20
# "two hundred forty-six" => 246
# "seven hundred eighty-three thousand nine hundred and nineteen" => 783919

def parse_int(string):
    num_dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
                'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
                'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13,
                'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17,
                'eighteen': 18, 'nineteen': 19, 'twenty': 20, 'thirty': 30,
                'forty': 40, 'fifty': 50, 'sixty': 60, 'seventy': 70,
                'eighty': 80, 'ninety': 90, 'twenty-one': 21}

    words = string.replace('-', ' ').split()
    total = 0
    current = 0
    for word in words:
        if word == 'and':
            continue
        elif word == 'hundred':
            current *= 100
        elif word == 'thousand':
            total += current * 1000
            current = 0
        elif word == 'million':
            total += current * 1000000
            current = 0
        else:
            current += num_dict[word]
    total += current
    return total
