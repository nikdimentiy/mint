def build_person(first_name, last_name):
	"""the function return dictionary with information about person"""
	person = {'first': first_name, 'last': last_name}
	return person

musician = build_person('jimi', 'hendrix')
print(musician)
