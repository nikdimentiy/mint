alien = {"color": "green", "points": 5}
print(alien["color"])
print(alien["points"])


new_points = alien["points"]
print(f"You just earned {new_points} points!")


alien = {"color": "green", "points": 5}
alien["x_position"] = 0
alien["y_position"] = 25
print(alien)


alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")


alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original x-position: {alien_0['x_position']}")

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New x-position: {alien_0['x_position']}")


alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)


favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print(favorite_languages)
print("Sarah's favorite language is " +
      favorite_languages['sarah'].title() + ".")


user = {
    'username': 'nikdimentiy',
    'first': 'Dimas',
    'last': 'Nikey',
}

for key, value in user.items():
    print("\nKey: " + key)
    print("Value: " + value)
