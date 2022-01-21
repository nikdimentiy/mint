FILE_PATH = '/home/polo/Documents/Workspace/Python/quotes.csv'

with open(FILE_PATH) as file_object:
    for line in file_object:
        print(line.rstrip())
