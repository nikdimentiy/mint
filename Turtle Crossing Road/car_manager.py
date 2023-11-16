from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    """
    A class responsible for managing cars in a game.
    """
    def __init__(self):
        """
        Initializes the CarManager object with an empty list for cars and a starting speed.
        """
        self.all_cars = []  # List to store all car objects
        self.car_speed = STARTING_MOVE_DISTANCE  # Initial speed of cars

    def create_car(self):
        """
        Creates a new car with a certain probability and adds it to the list of cars.
        """
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")  # Create a new Turtle object representing a car
            new_car.shapesize(stretch_wid=1, stretch_len=2)  # Adjust the size of the car
            new_car.penup()  # Lift the pen to avoid drawing while moving
            new_car.color(random.choice(COLORS))  # Set a random color for the car
            random_y = random.randint(-250, 250)  # Randomly set the initial y-coordinate
            new_car.goto(300, random_y)  # Move the car to the starting position on the right
            self.all_cars.append(new_car)  # Add the new car to the list of all cars

    def move_cars(self):
        """
        Move all the cars in the list to the left by the current car speed.
        """
        for car in self.all_cars:
            car.backward(self.car_speed)  # Move the car backward by the current speed

    def level_up(self):
        """
        Increase the speed of the cars when the player levels up.
        """
        self.car_speed += MOVE_INCREMENT  # Increase the car speed when the player levels up
