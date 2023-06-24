from turtle import Turtle

class Scoreboard(Turtle):
    """A class to represent the scoreboard for a pong game."""

    def __init__(self):
        """Initialize the scoreboard with white color and zero scores."""
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0 # score for the left player
        self.r_score = 0 # score for the right player
        self.update_scoreboard()

    def update_scoreboard(self):
        """Clear the previous scores and write the current scores on the screen."""
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        """Increase the score for the left player by one and update the scoreboard."""
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        """Increase the score for the right player by one and update the scoreboard."""
        self.r_score += 1
        self.update_scoreboard()
