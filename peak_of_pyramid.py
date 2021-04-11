# the tiny code draws the pyramid of asterisks
n = int(input("Enter any number - it's peak of your pyramid: "))
stars = "*"
while len(stars) <= n:
    print(stars)
    stars += "*"
