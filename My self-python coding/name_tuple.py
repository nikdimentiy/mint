# Python supports a type of container like dictionaries called “namedtuple()” present in the module, “collections“. 
# Like dictionaries, they contain keys that are hashed to a particular value. 
# But on contrary, it supports both access from key-value and iteration, the functionality that dictionaries lack.

from collections import namedtuple

# mini - table of chessmasters players with name, year of birth and rating

Player = namedtuple("Chess_master", ["name", "yearOfBirth", "rating"])
players = Player("Carlsen", 1990, 2842), Player(
    "Caruana", 1992, 2822), Player("Mamedyarov", 1985, 2801)

# print(players[0].name)
p1 = Player("Carlsen", 1990, 2882)
print(p1.name)
print(p1.yearOfBirth)
print(p1.rating)
