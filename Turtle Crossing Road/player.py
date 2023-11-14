from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    """A class to represent the player in a game"""

    def __init__(self):
        """Initialize the player"""
        super().__init__()  # Call the constructor of the parent class
        self.shape("turtle")  # Set the shape of the player to a turtle
        self.penup()  # Don't draw lines when moving
        self.go_to_start()  # Move the player to the starting position
        self.setheading(90)  # Set the initial heading of the player to face upwards

    def go_up(self):
        """Move the player upwards by the move distance"""
        self.forward(MOVE_DISTANCE)  # Move the player forward by the move distance

    def go_to_start(self):
        """Move the player to the starting position"""
        self.goto(STARTING_POSITION)  # Move the player to the starting position

    def is_at_finish_line(self):
        """Check if the player has reached the finish line"""
        if self.ycor() > FINISH_LINE_Y:  # If the player's y-coordinate is greater than the finish line y-coordinate
            return True  # The player has reached the finish line
        else:
            return False  # The player has not reached the finish line
