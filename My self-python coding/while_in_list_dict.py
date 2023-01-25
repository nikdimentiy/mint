unconfirmed_users = ['alice', 'phil', 'brandon', 'richard', 'brian']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)
print("\nThe following users have been confirmed: ")
for conf_users in confirmed_users:
    print(conf_users.title())


pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat', 'Guinea Pig', 'green lizard', 'parrot', 'cat']
print(len(pets))
print(pets)

while 'cat' in pets:
    pets.remove("cat")

print(len(pets))
print(pets)

responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name: ")
    response = input("Which mountain would you like to climb someday? ")

    responses[name] = response
    repeat = input("Would you like to let anther person respond? (yes / no) ")
    if repeat == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name.title() + " would like to climb " + response + "!")

