import random
import turtle as t

tim = t.Turtle()
screen = t.Screen()

t.colormode(255)
def random_color():
    r = random.randint(0 , 255)
    g = random.randint(0 , 255)
    b = random.randint( 0 , 255)
    random_c = (r,g,b)
    return random_c
    

def move_forwards():
    tim.color(random_color())
    tim.forward(10)

def move_backwards():
    tim.color(random_color())  
    tim.backward(10)

def turn_left():

    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
    tim.color(random_color())


tim.width(10)
screen.listen()
screen.onkey(move_forwards, "Up")
screen.onkey(move_backwards, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(clear, "c")

screen.exitonclick()
