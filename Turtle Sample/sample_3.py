# Import the 'turtle' module and alias it as 't'
import turtle as t
import random

# Create a new Turtle object named 'tim'
tim = t.Turtle()

# List of colors to choose from
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed",
           "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

# Function to draw a shape with a given number of sides
def draw_shape(num_sides):
    angle = 360 / num_sides  # Calculate the angle for each side
    for _ in range(num_sides):
        tim.forward(100)     # Move forward by 100 units
        tim.right(angle)     # Turn right by the calculated angle

# Loop to draw shapes with different numbers of sides
for shape_side_n in range(3, 10):  # Start with a triangle (3 sides) and go up to an octagon (8 sides)
    tim.color(random.choice(colours))  # Choose a random color from the 'colours' list
    draw_shape(shape_side_n)  # Call the 'draw_shape' function to draw the current shape

# After the loop, the turtle 'tim' will have drawn filled shapes with varying numbers of sides and random colors.

