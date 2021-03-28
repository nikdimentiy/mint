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
