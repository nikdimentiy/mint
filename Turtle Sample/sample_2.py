# Import the 'turtle' module and alias it as 't'
import turtle as t

# Create a new Turtle object named 'tim'
tim = t.Turtle()

# Repeat the following block of code 15 times
for _ in range(15):
    # Move the turtle forward by 10 units
    tim.forward(10)
    
    # Lift the pen up to stop drawing
    tim.penup()
    
    # Move the turtle forward by another 10 units (without drawing)
    tim.forward(10)
    
    # Put the pen down to resume drawing
    tim.pendown()

# After the loop, the turtle 'tim' will have drawn 15 pairs of lines,
# with each pair consisting of a 10-unit line segment followed by a 10-unit gap.

