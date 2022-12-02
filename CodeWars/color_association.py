# Colour plays an important role in our lifes. Most of us like this colour better then another.
# User experience specialists believe that certain colours have certain psychological meanings for us.

# You are given a 2D array, composed of a colour and its 'common' association in each array element.
# The function you will write needs to return the colour as 'key' and association as its 'value'.


def colour_association(arr):
    return [{i[0]: i[1]} for i in arr]
