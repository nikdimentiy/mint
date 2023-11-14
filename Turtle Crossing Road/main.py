import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Set up the game window and screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Create instances of the Player, CarManager, and Scoreboard classes
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Set up keyboard input for the player's movement
screen.listen()
screen.onkey(player.go_up, "Up")

# Start the game loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)  # Pause for a short period of time before updating the screen
    screen.update()  # Update the screen to show any changes

    car_manager.create_car()  # Create a new car at random intervals
    car_manager.move_cars()  # Move all the cars across the screen

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:  # If the player collides with a car
            game_is_on = False  # End the game
            scoreboard.game_over()  # Display the game over message on the scoreboard

    # Detect successful crossing
    if player.is_at_finish_line():  # If the player has successfully crossed the road
        player.go_to_start()  # Move the player back to the starting position
        car_manager.level_up()  # Increase the level of the game and speed of the cars
        scoreboard.increase_level()  # Update the scoreboard to show the new level

# Exit the game when the player clicks on the screen
screen.exitonclick()
