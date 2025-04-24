from turtle import Turtle , Screen

turtle = Turtle()
turtle.shape("turtle")
turtle.color("red")

a=4
while a>0:
    turtle.forward(100)
    turtle.right(90)
    a -= 1

screen = Screen()
screen.exitonclick()