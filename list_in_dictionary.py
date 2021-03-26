# saving information for ordered pizza
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

# order description
print("You ordered a " + pizza['crust'] + "-crust pizza " +
      "with the following toppings: ")
for topping in pizza['toppings']:
    print("\t" + topping)

#-----------------------------------------------------------#

favorite_lang = {
    'jen': ['ruby', 'haskel'],
    'sarah': ['kotlin', 'c'],
    'derek': ['python', 'javascript'],
    'edward': ['java', 'python'],
    'phil': ['swift', 'scala'],
}
for name, languages in favorite_lang.items():
    print("\n" + name.title() + " favorite language are: ")
    for language in languages:
        print("\t" + language.title())

