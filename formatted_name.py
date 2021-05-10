def get_formatted_name(first_name, last_name):
    """a neatly formatted full name is returned"""
    full_name = first_name + ' ' + last_name
    return full_name.title()


musician = get_formatted_name("jimmi", "hendrix")
print(musician)

