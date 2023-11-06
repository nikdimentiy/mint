from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    """
    The Snake class represents the snake in the Snake game.

    Attributes:
        segments (list): A list of Turtle objects representing the snake's body segments.
        head (Turtle): The first segment in the list, representing the snake's head.
    """

    def __init__(self):
        """
        Initialize a Snake object with the starting position and create its segments.
        """
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """
        Create the initial snake by adding segments to the segments list.
        """
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """
        Add a new segment to the snake at the specified position.

        Args:
            position (tuple): The (x, y) coordinates for the new segment's position.
        """
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """
        Extend the snake by adding a new segment at the tail of the snake.
        """
        self.add_segment(self.segments[-1].position())

    def move(self):
        """
        Move the snake by updating the position of each segment.
        """
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """
        Change the snake's direction to up, but only if it's not currently moving down.
        """
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """
        Change the snake's direction to down, but only if it's not currently moving up.
        """
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """
        Change the snake's direction to left, but only if it's not currently moving right.
        """
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """
        Change the snake's direction to right, but only if it's not currently moving left.
        """
        if self head.heading() != LEFT:
            self.head.setheading(RIGHT)
