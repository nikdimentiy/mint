import random

class Ghost(object):
    """
    A class representing a ghost with a randomly assigned color.

    Attributes:
        color (str): The color of the ghost, which can be one of the following:
                     "white", "yellow", "purple", or "red".
    """

    def __init__(self):
        """
        Initializes a new instance of the Ghost class.
        
        The color of the ghost is randomly selected from the predefined list
        of colors when an instance is created.
        """
        self.color = random.choice(["white", "yellow", "purple", "red"])

# Driver code to demonstrate the functionality of the Ghost class
if __name__ == "__main__":
    # Create a list to hold multiple ghost instances
    ghosts = []

    # Create 5 ghost instances and store them in the list
    for _ in range(5):
        ghost = Ghost()
        ghosts.append(ghost)

    # Print the colors of the created ghosts
    for i, ghost in enumerate(ghosts):
        print(f"Ghost {i + 1} color: {ghost.color}")
