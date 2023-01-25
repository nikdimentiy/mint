# If the name parameter is not specified, then name - "Dmitriy"

def hello(name='Dmitriy'):
    print('Hello, ', name, '!', sep='')

hello('Python')
hello()