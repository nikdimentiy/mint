from turtle import Turtle

class Paddle(Turtle):
    """A class to represent the paddle for a pong game."""

    def __init__(self, position):
        """Initialize the paddle with a square shape, white color and a given position."""
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1) # make the paddle longer and thinner
        self.penup()
        self.goto(position)

    def go_up(self):
        """Move the paddle up by 20 pixels."""
        new_y = self.ycor() + 20 # get the current y-coordinate and add 20
        self.goto(self.xcor(), new_y) # go to the new position

    def go_down(self):
        """Move the paddle down by 20 pixels."""
        new_y = self.ycor() - 20 # get the current y-coordinate and subtract 20
        self.goto(self.xcor(), new_y) # go to the new position

