import turtle

def david():
  for step in range(6):
    turtle.begin_fill()
    for i in range(3):
      turtle.forward(50)
      turtle.left(120)
    turtle.end_fill()

    turtle.forward(50)
    turtle.right(60)

turtle.shape("turtle")
turtle.shapesize(3)
turtle.color("green", "yellow")
turtle.speed(10)

david()
turtle.hideturtle()
turtle.backward(100)
turtle.shape("turtle")
turtle.shapesize(3)
turtle.color("red", "green")
turtle.speed(10)
david()
