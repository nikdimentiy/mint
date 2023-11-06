from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    """
    The Scoreboard class manages the game score and high score display.

    Attributes:
        score (int): The player's current score.
        high_score (int): The highest score achieved in the game.
    """

    def __init__(self):
        """
        Initialize the Scoreboard object.
        """
        super().__init()
        self.score = 0
        # Read the high score from a file
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Update the scoreboard display with the current score and high score.
        """
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        """
        Reset the score and update the high score if a new high score is achieved.
        """
        if self.score > self.high_score:
            self.high_score = self.score
            # Write the new high score to a file
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        """
        Increase the player's score by 1 and update the scoreboard.
        """
        self.score += 1
        self.update_scoreboard()
