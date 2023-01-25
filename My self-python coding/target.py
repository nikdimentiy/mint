# mini game: "Hit the target"
import turtle

# named constants
SCREEN_WIDTH = 600  # screen width
SCREEN_HEIGHT = 600  # screen height
TARGET_LLEFT_X = 100  # lower left coordinate of the 'x' target
TARGET_LLEFT_Y = 250  # lower left coordinate of the 'y' target
TARGET_WIDTH = 25  # width of target
FORCE_FACTOR = 30  # arbitrary force factor
PROJECTILE_SPEED = 1  # projectile animation speed
NORTH = 90  # north-directional angle
SOUTH = 270  # south-routing angle
EAST = 0  # east-routing angle
WEST = 180  # west-routing angle

# configuring the window
turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

# drawing a target
turtle.hideturtle()
turtle.speed(0)
turtle.penup()
turtle.goto(TARGET_LLEFT_X, TARGET_LLEFT_Y)
turtle.pendown()
turtle.setheading(EAST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(NORTH)
turtle.forward(TARGET_WIDTH)
turtle.setheading(WEST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(SOUTH)
turtle.forward(TARGET_WIDTH)
turtle.penup()

# centers the turtle
turtle.goto(0, 0)
turtle.setheading(EAST)
turtle.showturtle()
turtle.speed(PROJECTILE_SPEED)

# we get an angle and strength from the user
angle = float(input("Enter the angle of the projectile: "))
force = float(input("Enter the starting force (1 - 10): "))

# calculate the distance
distance = force * FORCE_FACTOR

# set the direction
turtle.setheading(angle)

# let's launch a projectile
turtle.pendown()
turtle.forward(distance)

# checking: if the target is hit?
if (turtle.xcor() >= TARGET_LLEFT_X and
    turtle.xcor() <= (TARGET_LLEFT_X + TARGET_WIDTH) and
    turtle.ycor() >= TARGET_LLEFT_Y and
    turtle.ycor() <= (TARGET_LLEFT_Y + TARGET_WIDTH)):
    print("The target is hitting!")
else:
    print("You missed!")
