from collections import namedtuple

Player = namedtuple("Chess_master", ["name", "yearOfBirth", "rating"])
players = Player("Carlsen", 1990, 2842), Player(
    "Caruana", 1992, 2822), Player("Mamedyarov", 1985, 2801)

# print(players[0].name)
p1 = Player("Carlsen", 1990, 2882)
print(p1.name)
print(p1.yearOfBirth)
print(p1.rating)
