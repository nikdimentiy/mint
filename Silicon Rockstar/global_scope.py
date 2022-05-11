enemies = 1  #  global scope


def increase_enemies():
    print(f"Enemies inside function: {enemies}")
    return enemies + 1  # using a global scope for returning value


enemies = increase_enemies()
print("Enemies outside function: {}".format(enemies))

