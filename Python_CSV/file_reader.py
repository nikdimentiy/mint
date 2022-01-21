FILE_PATH = '/home/polo/Documents/Workspace/Python/quotes.csv'  # file path in my Linux desctop

with open(FILE_PATH) as file_object:
    for line in file_object:
        print(line.rstrip()) # strip symbol of new line after iteration of the 'for' loop
