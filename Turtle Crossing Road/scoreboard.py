from turtle import Turtle

# Define the font for the scoreboard
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    """A class to represent the scoreboard in a game"""

    def __init__(self):
        """Initialize the scoreboard"""
        super().__init__()  # Call the constructor of the parent class
        self.level = 1  # Set the initial level to 1
        self.hideturtle()  # Hide the turtle icon
        self.penup()  # Don't draw lines when moving
        self.goto(-280, 250)  # Set the initial position of the scoreboard
        self.update_scoreboard()  # Update the scoreboard with the initial level

    def update_scoreboard(self):
        """Update the scoreboard with the current level"""
        self.clear()  # Clear any previous text on the scoreboard
        self.write(f"Level: {self.level}", align="left", font=FONT)  # Write the current level on the scoreboard

    def increase_level(self):
        """Increase the level by 1 and update the scoreboard"""
        self.level += 1  # Increment the level by 1
        self.update_scoreboard()  # Update the scoreboard with the new level

    def game_over(self):
        """Display 'GAME OVER' in the center of the screen"""
        self.goto(0, 0)  # Move to the center of the screen
        self.write(f"GAME OVER", align="center", font=FONT)  # Write 'GAME OVER' in the center of the screen
