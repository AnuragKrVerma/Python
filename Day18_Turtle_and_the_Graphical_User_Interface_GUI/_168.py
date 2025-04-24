import turtle as t


tim = t.Turtle()
def draw(sides):
    angle = 360/sides
    for _ in range(sides):
        tim.forward(100)
        tim.right(angle)



for _ in range(1,11):
    draw(_)

screen = t.Screen()
screen.exitonclick()