def get_formatted_name(first_name, last_name, middle_name=''):
    """a neatly formatted full name is returned"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()


musician = get_formatted_name("jimmi", "hendrix")
print(musician)
musician = get_formatted_name("john", "hooker", "lee")
print(musician)
