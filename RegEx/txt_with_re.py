import re

file_name = "fw.txt"
with open(file_name) as file_obj:
    lines = file_obj.readlines()
    common_string = ""
    for line in lines:
        common_string += line.strip()
pattern = r'[0-9]'

new_string = re.sub(pattern, '', common_string)


with open("frequenly_english_words.txt", 'w') as file_obj:
    file_obj.write(new_string)
